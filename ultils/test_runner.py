import subprocess
from ultils.result_summarize import ResultSummary


class TestRunner:
    @staticmethod
    def run():
        # run function: login
        login_suite = TestSuite(
            "login", "../tests")
        login_result = login_suite.execute_by_tags(
            '--tags=@login')
        print(f"Feature Login: {login_result}")
        print("Overall result:")
        print(login_result.decide_overall())


class TestSuite:
    def __init__(self, name: str, feature_dir: str):
        self.name = name
        self.feature_dir = feature_dir

    def execute_by_tags(self, tags_option: str):
        command = ["behave", tags_option, "--junit", "--junit-directory=../reports",
                   "--no-skipped", self.feature_dir]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        output_str = output.decode('utf-8')

        results = ResultSummary.get_result_summary(output_str)
        return results


if __name__ == "__main__":
    TestRunner.run()
