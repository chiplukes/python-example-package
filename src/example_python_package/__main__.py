
# Import the main package
import example_python_package
import argparse
import importlib.metadata

if __name__ == "__main__":

    print(f"within package: {importlib.metadata.packages_distributions()}")
    print(f"{__file__}:__main__")

    parser = argparse.ArgumentParser()

    # Optional argument flag which defaults to False
    parser.add_argument("-d", "--debug", action="store_true", default=False)

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=importlib.metadata.version('example_python_package')))

    args = parser.parse_args()

    solved = example_python_package.example_python_package_function()
