import subprocess
from ultils.result_summarize import ResultSummary


class TestRunner:
    @staticmethod
    def run():
        print("Start testing...")
        # run function: login
        login_suite = TestSuite(
            "login", "tests")
        login_result = login_suite.execute_by_tags(
            '--tags=@login')
        print(f"Feature Login: {login_result}")
        # run function: signup
        signup_suite = TestSuite(
            "signup", "tests")
        signup_result = signup_suite.execute_by_tags(
            '--tags=@signup')
        print(f"Feature Login: {signup_result}")

        overall_result = ResultSummary(passed_scenarios=login_result.passed_scenarios + signup_result.passed_scenarios,
                                       failed_scenarios=login_result.failed_scenarios + signup_result.failed_scenarios)
        print(f"Overall result: {overall_result}")
        print(overall_result.decide_overall())


class TestSuite:
    def __init__(self, name: str, feature_dir: str):
        self.name = name
        self.feature_dir = feature_dir

    def execute_by_tags(self, tags_option: str):
        command = ["behave", tags_option, "--junit", "--junit-directory=reports",
                   "--no-skipped", self.feature_dir]
        # command = ["behave", tags_option,
        #            "--no-skipped", self.feature_dir]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        output_str = output.decode('utf-8')

        results = ResultSummary.get_result_summary(output_str)
        return results
