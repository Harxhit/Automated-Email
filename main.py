import smtplib
import random
import datetime as dt
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
email = "pariharharshit760@gmail.com"
password = "gvja rnuz zvxe payx"

try:
    # Load birthdays data from CSV into a DataFrame
    data = pd.read_csv(r"C:\Users\Welcome\OneDrive\Desktop\Python\Mini Project\Birthday-Wisher\birthdays.csv")

    # Get today's month and day
    today = (dt.datetime.now().month, dt.datetime.now().day)

    # Create a dictionary of birthdays
    birthdays_dict = {(row["month"], row["day"]): row for index, row in data.iterrows()}

    # Check if today's date matches any birthday in the dictionary
    if today in birthdays_dict:
        birthday_person = birthdays_dict[today]
        file_path = f"C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\Birthday-Wisher\\letter-template\\letter_{random.randint(1,3)}.txt"

        with open(file_path, encoding='utf-8') as letter:
            content = letter.read()
            content = content.replace("[NAME]", birthday_person["name"])

        # Construct the email message
        message = MIMEMultipart()
        message["From"] = email
        message["To"] = birthday_person["email"]
        message["Subject"] = "Birthday Wish"
        message.attach(MIMEText(content, "plain"))

        # Add SPF and DKIM headers
        message.add_header('Sender', email)
        message.add_header('Reply-To', email)
        message.add_header('Return-Path', email)

        # Connect to Gmail's SMTP server with TLS
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)

            # Send the email
            connection.sendmail(
                from_addr=email,
                to_addrs=birthday_person["email"],
                msg=message.as_string()
            )
            print(f"Birthday wish sent to {birthday_person['name']} at {birthday_person['email']}")
    else:
        print("No birthdays today.")

except smtplib.SMTPAuthenticationError:
    print("SMTP Authentication Error: Please check your Gmail credentials.")
except smtplib.SMTPException as e:
    print(f"SMTP Exception occurred: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
