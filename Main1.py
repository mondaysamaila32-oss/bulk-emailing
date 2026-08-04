import datetime
import smtplib
import csv
import time
from email.message import EmailMessage # 1. Import the library
GMAIL_ADDRESS = "mondaysamaila32@gmail.com"
# 3. Retrieve the credentials securely
# The names inside the quotes MUST match exactly what you typed in the .env file
sender_email = GMAIL_ADDRESS
print("Connecting to email server...")

with smtplib.SMTP("localhost", 1025) as server:
    with open("error_file.text", 'a', encoding = 'utf-8') as lof_file:
        with open("mailpit test_1.csv", 'r', encoding = 'utf_8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                CUSTOMER_EMAIL = row['Email']
                CUSTOMER_NAME = row['Name']

                body = f"""HELLO, {CUSTOMER_NAME},

                Welcome aboard we are thrilled to have you with us.
                if you have any question feel free to reply directly to this email.

                Besst regards,
                The Python Script Test Team"""
                msg=EmailMessage()
                msg["Subject"] = f"Welcome Aboard, {CUSTOMER_NAME}!"
                msg["From"] = sender_email
                msg["To"] = CUSTOMER_EMAIL
                msg.set_content(body)
                print(f"SUccessfully send Email to: {CUSTOMER_NAME}")
                try:
                    server.send_message(msg)
                except Exception as e:
                    print(f"Error sending email: {e}")
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Error occurred at {current_time}")
        
    # ... rest of your email loop continues here ...