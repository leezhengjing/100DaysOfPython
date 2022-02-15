##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas


data = pandas.read_csv("birthdays.csv")
birthdays_records = data.to_dict(orient="records")
# Below is how the the course went through this coding challenge
# new_birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
birthdays_dict = {
    (birthdays_records[n]["month"], birthdays_records[n]["day"]): birthdays_records[n] for n in range(len(birthdays_records))
}

today = dt.datetime.now()
today_month = today.month
today_day = today.day

my_gmail = "REDACTED"
my_ymail = "REDACTED"
gmail_password = "REDACTED"
yahoo_password = "REDACTED"

if (today_month, today_day) in birthdays_dict:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        content = file.read()
        birthday_person_name = birthdays_dict[(today_month, today_day)]["name"]
        birthday_person_mail = birthdays_dict[(today_month, today_day)]["email"]
        content = content.replace("[NAME]", birthday_person_name)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_ymail, password=yahoo_password)
        connection.sendmail(
            from_addr=my_ymail,
            to_addrs=birthday_person_mail,
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )