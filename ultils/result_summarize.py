import re


class ResultSummary:
    def __init__(self, passed_scenarios: int = 0, failed_scenarios: int = 0, skipped_scenarios: int = 0,
                 time: str = "Undefined", failed_scenario_names: tuple = None):
        self.passed_scenarios = passed_scenarios
        self.failed_scenarios = failed_scenarios
        self.skipped_scenarios = skipped_scenarios
        self.time = time
        self.failed_scenario_names = failed_scenario_names

    @classmethod
    def get_result_summary(cls, data_str: str):
        patterns = {
            'time': r'Took (\S+)s',
            'failed_scenario_names': r'Failing scenarios:\n(.*?)(?:\n\n|$)',
            'summary': r'(\d+) scenarios passed, (\d+) failed, (\d+) skipped'
        }
        results = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, data_str, re.DOTALL)
            if match:
                if key == 'time':
                    results[key] = match.group(1)

                elif key == 'failed_scenario_names':
                    failing_scenarios_text = match.group(1)
                    failing_scenarios = re.findall(r'\s+(\S+)\s+(.*?)\n', failing_scenarios_text)
                    results[key] = [scenario[1] for scenario in failing_scenarios]

                elif key == 'summary':
                    results['passed_scenarios'] = int(match.group(1))
                    results['failed_scenarios'] = int(match.group(2))
                    results['skipped_scenarios'] = int(match.group(3))

        return cls(**results)

    def calculate_total(self):
        total_scenarios = self.passed_scenarios + self.failed_scenarios
        return total_scenarios

    def calculate_percentage(self):
        try:
            return round((float(self.passed_scenarios) / float(self.calculate_total())) * 100, 2)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        output = f'Passed case(s): {self.passed_scenarios}/{self.calculate_total()} => {self.calculate_percentage()}%'
        return output

    def decide_overall(self):
        if self.calculate_percentage() >= 80:
            return "ACCEPTABLE"
        else:
            return "UNACCEPTABLE"
