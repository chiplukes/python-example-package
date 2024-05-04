# Import the simple submodule
from . import simple_submodule

# Import the subpackage_module
from .complex_submodule import complex_submodule1a, complex_submodule1b


def python_example_package_function():
    print(f"within: {__file__} - fun()")

    simple_submodule.simple_fun()

    complex_submodule1a.fun()
    complex_submodule1b.fun()

    return True
