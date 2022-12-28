# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
from datetime import datetime
import pandas
import random

MY_MAIL = "peter@poto.lib"

today = datetime.now()
today = (today.month, today.day)

test_date = (12,21)

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("File not found")
else:
    data.to_dict()

new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if test_date in new_dict:
    birth_person = new_dict[test_date]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birth_person["name"])
        print(contents)



