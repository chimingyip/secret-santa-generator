import random
import smtplib
from email.mime.text import MIMEText

# list of people
progress = True
name_dict = {}
emails = []
while progress:
    input_name = input("Enter a participant's name: ")
    if input_name == "":
        progress = False
    else:
        input_email = input("Now, enter their email: ")
        name_dict[input_email] = input_name
        emails.append(input_email)

print(name_dict)
print(emails)

# reorder the list to be random
shuffled = emails
random.shuffle(shuffled)

draw = {}
for i in range(len(shuffled)):
    if i == len(shuffled) - 1:
        draw[shuffled[i]] = shuffled[0]
    else:
        draw[shuffled[i]] = shuffled[i+1]

print(draw)

# send emails

sender = input("Type your email and press enter: ")
password = input("Type your gmail password and press enter: ")

for (giver, receiver) in draw.items():
    try:
        givers = [giver]

        giver_name = name_dict[giver]
        receiver_name = name_dict[receiver]

        msg = MIMEText(f"""
        Hi {giver_name}
        Your Secret Santa is: {receiver_name}
        Have a Merry Xmas! :)
        """)
        msg['Subject'] = 'Your Secret Santa is...'
        msg['From'] = giver
        msg['To'] = receiver

        text = msg.as_string()
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(sender, password)
        session.sendmail(sender, givers, text)

        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")