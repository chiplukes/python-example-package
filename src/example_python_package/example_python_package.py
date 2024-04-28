
# Import the simple subpackages/helpers from the current folder "."
from . import simple_submodule

# Import the subpackage_module
from .complex_submodule import complex_submodule1a,complex_submodule1b

def example_python_package_function():

    print('example_python_package_main')

    simple_submodule.simple_fun()

    complex_submodule1a.fun()
    complex_submodule1b.fun()

    return True

