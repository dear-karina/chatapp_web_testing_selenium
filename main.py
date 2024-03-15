import sys
from behave.__main__ import main as behave_main

if __name__ == "__main__":
    output_file = "logging/logging.txt"

    # Redirect console output to the file
    with open(output_file, "w") as f:
        sys.stdout = f
        sys.stderr = f

        # Run Behave with the @negative tag
        behave_main(["--tags=@negative-case", "tests/login"])
