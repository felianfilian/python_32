# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import pandas

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("File not found")
else:
    data.to_dict()
    print(data)

#for row in data:
print(data[row]["year"])

my_email = "peter@poto.lib"

now = dt.datetime.now()
print(now)

