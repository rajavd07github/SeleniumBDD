import os
import sys
from behave.__main__ import main as behave_main

# Custom options for Behave
options = '--tags=@important'  # Example: run only tests with the @important tag


def run_test():
    # Ensure the current directory is the project root
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # run behave with custom option
    sys.exit(behave_main(options))


if __name__ == "__main__":
    run_test()
