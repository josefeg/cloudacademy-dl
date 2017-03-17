#!/usr/bin/env python3
'''
Downloads the video lectures for the given CloudAcademy course.

Usage:
    cloudacademy-dl --help
    cloudacademy-dl --email=<email> [--password=<pass>] [--res=<resolution>]
        [--out=<output_dir>] <url>

Options:
    --help              Shows this screen.
    --email=<email>     The login email address for your CloudAcademy account.
    --password=<pass>   The password for your CloudAcademy account. If this is
                        not passed in as a command line argument it will be
                        asked for before the download can start.
    --res=<resolution>  The required video resolution. Allowed values are 360,
                        720, and 1080 [default: 1080].
    --out=<output_dir>  The directory where the videos are saved
                        [default: courses].
    url                 The URL for the course page.
'''

import os
import re
import unicodedata

import requests

from getpass import getpass
from urllib.parse import urlparse

from docopt import docopt
from bs4 import BeautifulSoup


def get_course_contents(course_url, cookies):
    resp = requests.get(course_url, cookies=cookies)
    soup = BeautifulSoup(resp.text, 'lxml')
    course_contents = dict()
    for div in soup.findAll('div', {'id': 'course-contents'}):
        index = 1
        for link in div.findAll('a'):
            href = link['href']
            if href.startswith('#'):
                continue
            title = '%02d-%s.mp4' % (index, sanitize(link['title']))
            if href == 'javascript:void(0);':
                course_contents[title] = course_url
            elif href.endswith('.html'):
                course_contents[title] = 'https://cloudacademy.com' + href
            index += 1
    return course_contents


def sanitize(name):
    value = unicodedata.normalize('NFKD', name)
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value


def get_course_dir(base_dir, course_url):
    o = urlparse(course_url)
    return base_dir + o.path


def get_video_url(video_page_url, cookies, resolution):
    resp = requests.get(video_page_url, cookies=cookies)
    soup = BeautifulSoup(resp.text, 'lxml')
    source = soup.find('source', {'type': 'video/mp4',
                                  'data-res': '{}p'.format(resolution)})
    return source['src']


def download_file(url, dest_filaneme):
    resp = requests.get(url, stream=True)
    with open(dest_filaneme, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=4096):
            f.write(chunk)


def download_course(course_url, username, password, video_res, output_dir):
    login_resp = requests.post('https://cloudacademy.com/login/',
                               data={'email': username, 'password': password})
    auth_cookies = login_resp.cookies

    print('Downloading course:', course_url)
    course_contents = get_course_contents(course_url, auth_cookies)
    course_dir = get_course_dir(output_dir, course_url)
    os.makedirs(course_dir, exist_ok=True)
    for filename, video_page_url in course_contents.items():
        full_filename = os.path.join(course_dir, filename)
        video_url = get_video_url(video_page_url, auth_cookies, video_res)
        download_file(video_url, full_filename)
    print('Done!')


def main():
    args = docopt(__doc__)

    video_res = args['--res']
    if video_res not in ['360', '720', '1080']:
        exit('Invalid value for --res. Supported values are 360, 720 or 1080')

    username = args['--email']
    password = args['--password']
    if password is None:
        password = getpass('Password: ')

    output_dir = args['--out']
    course_url = args['<url>']

    download_course(course_url, username, password, video_res, output_dir)


if __name__ == '__main__':
    main()
