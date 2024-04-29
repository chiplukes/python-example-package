# python-example-package

[![Tests](https://github.com/chiplukes/python-example-package/actions/workflows/test.yml/badge.svg)](https://github.com/chiplukes/python-example-package/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/chiplukes/python-example-package?include_prereleases&label=changelog)](https://github.com/chiplukes/python-example-package/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/chiplukes/python-example-package/blob/main/LICENSE)

This is a simple project that can be used to start new python package.

## Installation

Install this library using `pip`:
```bash
pip install git+https://github.com/chiplukes/python-example-package
```
## Usage

* throughout project rename ```python-example-project``` with your actual hyphenated project name.
* throughout project rename ```python_example_project``` with your actual underscored project name.
* throughout project rename ```chiplukes``` with your actual github username.
* in source folder rename folders and files to match name of your package
    * if package does not include any submodules or extra python files, just delete those.
* add correct imports into relevant ```__init__.py``` files

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd python-example-package
python -m venv .venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:
```bash
python -m pip install -e .

# maybe?
pip install -e '.[test]'
```

Running main package
```bash
python -m python_example_package
```

To run the tests:
```bash
pytest
```
