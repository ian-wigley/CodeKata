import csv
from pathlib import Path

from birthday import get_birthdays
from faker import Faker


class GenerateCsv:
    def __init__(self):
        self.done = True

    def create_fakes(self):
        fake = Faker()

        Faker.seed(0)
        birthdays = []
        for _ in range(100):
            name = fake.name()
            email = fake.email()
            dob = str(fake.date_of_birth())
            birthdays.append(
                [
                    name,
                    email,
                    dob
                ]
            )

        with open('birthdays.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(birthdays)
        self.done = False


if __name__ == "__main__":
    generate_csv = GenerateCsv()
    if not generate_csv.done:
        generate_csv.create_fakes()
    csv_path = str(Path(__file__).parents[1] / "assets/birthdays.csv")
    rusty_df = get_birthdays(csv_path, "1973-04-24")
    print(rusty_df)
