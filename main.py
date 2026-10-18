# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
data = pandas.read_csv("birthdays.csv",)
data_dic = data.to_dict(orient="records")
print(data_dic)
for person in data_dic:
    if person["month"] == month and person["day"] == day:
        birthday_person = person["name"]
        print(birthday_person)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_numb = random.randint(1, 3)
        print(letter_numb)
        with open(f"letter_templates/letter_{letter_numb}.txt") as letter_file:
            msg = letter_file.read()
            msg = msg.replace("[NAME]", birthday_person)




# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="saricpython@yahoo.com",
                                msg=f"Subject:Happy Birthday\n\n{msg}")
