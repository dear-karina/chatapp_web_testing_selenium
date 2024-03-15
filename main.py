import subprocess

if __name__ == "__main__":
    output_file = "logging/logging.txt"

    with open(output_file, "w") as f:
        subprocess.run(["behave", "--tags=@negative-case", "--junit", "--no-skipped",
                        "tests/login"], stdout=f, stderr=subprocess.STDOUT)
