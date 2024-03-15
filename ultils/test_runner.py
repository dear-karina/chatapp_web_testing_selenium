import subprocess
from ultils.result_summarize import ResultSummary


class TestRunner:
    @staticmethod
    def run():
        # run function: login
        # run must-pass
        login_suite = TestSuite(
            "login", "../tests/login")
        login_must_passed_result = login_suite.execute_by_tags(
            '--tags=@must-passed')
        print("Must-passed: ")
        print(login_must_passed_result)

        # run remaining
        login_remaining_result = login_suite.execute_by_tags(
            '--tags=~@must-passed')
        print("Total: ")

        total_passed_scenarios = (
                login_must_passed_result.passed_scenarios +
                login_remaining_result.passed_scenarios
        )

        login_result = ResultSummary(passed_scenarios=total_passed_scenarios,
                                     failed_scenarios=login_must_passed_result.calculate_total() + login_remaining_result.calculate_total())
        print(login_result)
        print("Overall result:")
        print(login_result.decide_overall())


class TestSuite:
    def __init__(self, name: str, feature_dir: str):
        self.name = name
        self.feature_dir = feature_dir

    def execute_by_tags(self, tags_option: str):
        command = ["behave", tags_option, "--junit",
                   "--no-skipped", self.feature_dir]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        output_str = output.decode('utf-8')

        results = ResultSummary.get_result_summary(output_str)
        return results


if __name__ == "__main__":
    TestRunner.run()
