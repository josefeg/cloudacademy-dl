# CloudAcademy Downloader

[![Latest version on PyPI](https://img.shields.io/pypi/v/cloudacademy-dl.svg)](https://pypi.python.org/pypi/cloudacademy-dl)
[![Downloads from PyPI](https://img.shields.io/pypi/dm/cloudacademy-dl.svg)](https://pypi.python.org/pypi/cloudacademy-dl)

This script can be used to download
[CloudAcademy](http://www.cloudacademy.com) lecture videoes so that they can
be viewed offline. This inspiration for this script came from the
[Coursera Downloader](https://github.com/coursera-dl/coursera-dl/).

## Disclaimer

This tool is meant to be used only if your CloudAcademy account supports
lecture downloads.

## Installation instructions

This script requires Python 3 and a CloudAcademy account. The preferred way to
install this script is to use `pip` as this will download the latest version
from [PyPI](http://pypi.python.org) and all the necessary dependencies.
```
pip install cloudacademy-dl
```

Alternatively, one can clone this repository and install the dependencies
manually or using `pip` via
```
pip install -r requirements.txt
```

## Usage Instructions

To download a course, all you need to do is run the script specifying your
CloudAcademy.com username, and the URL of the course that you would like to
download:
```
cloudacademy-dl --email=<CloudAcademy login email> <course url>
```
The script will then ask you for you CloudAcademy account password before it
can start the download.

The optional command line arguments for the script are:
```
--help              Prints out the list of command line arguments.
--password=<pass>   The password for your CloudAcademy account. If this is not
                    passed in as a command line argument it will be asked for
                    before the download can start.
--res=<resolution>  The required video resolution. Allowed values are 360,
                    720, and 1080. The default value for this argument is
                    1080.
--out=<output_dir>  The directory where the videos are saved. If this command
                    line argument is not specified, then they will be saved in
                    current directory under courses/.
```

## Contact information

Please report any bugs and issues on
[github](https://github.com/josefeg/cloudacademy-dl).
Additionaly I can also be reached on twitter under the handle
[@josefgalea](http://twitter.com/josefgalea).
