from faker import Faker
from time import time


class DataGenerator:
    @staticmethod
    def generate_username():
        time_stamp = str(int(time()))
        return f"tester_{time_stamp}"

    @staticmethod
    def generate_fullname():
        return Faker().name()

    @staticmethod
    def generate_password(length: int):
        password = Faker().password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)
        return password

    @staticmethod
    def choose_random(choices: tuple):
        return Faker().random_element(choices)


if __name__ == "__main__":
    print(DataGenerator.generate_fullname())
    print(DataGenerator.generate_password(8))
    print(DataGenerator.choose_random(("male", "female")))
