import subprocess

if __name__ == "__main__":
    # Run Behave and capture the output
    command = ["behave", "--tags=@negative-case", "--junit", "--no-skipped", "tests/login"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    # Get the last 10 lines of the output using tail command
    tail_command = ["tail", "-n", "10"]
    tail_process = subprocess.Popen(tail_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    last_10_lines, _ = tail_process.communicate(input=output)

    # Convert the last 10 lines to a string
    last_10_lines_string = last_10_lines.decode()

    print("Last 10 lines:")
    print(last_10_lines_string)
