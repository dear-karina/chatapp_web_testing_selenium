import unittest
from test_cases.test_login import LoginTestCase


def run_test():
    test_suite = unittest.TestSuite()

    login_test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
    test_suite.addTest(login_test_case)

    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    run_test()
