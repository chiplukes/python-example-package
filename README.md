# example-python-package

[![Tests](https://github.com/chiplukes/example-python-package/actions/workflows/test.yml/badge.svg)](https://github.com/chiplukes/example-python-package/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/chiplukes/example-python-package?include_prereleases&label=changelog)](https://github.com/chiplukes/example-python-package/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/chiplukes/example-python-package/blob/main/LICENSE)

This is a simple project that can be used to start new python package.

## Installation

Install this library using `pip`:
```bash
pip install git+https://github.com/chiplukes/example-python-package
```
## Usage

* throughout project rename ```example-python-project``` with your actual hyphenated project name.
* throughout project rename ```example_python_project``` with your actual underscored project name.
* throughout project rename ```chiplukes``` with your actual github username.
* in source folder rename folders and files to match name of your package
    * if package does not include any submodules or extra python files, just delete those.
* add correct imports into relevant ```__init__.py``` files

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd example-python-package
python -m venv .venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
