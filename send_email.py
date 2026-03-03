import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

to_email = input("Enter email: ")
name = input("Enter name: ")

template = """
Hi {name}
...
"""

def send_verification_email(to_email, name):
    message = Mail(
        from_email = "noreply@example.com",
        to_emails = to_email,
        subject = "ARO Verification",
        plain_text_content = template.format(name=name)
        )

    try: 
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)

        print("Email sent!")
        print("Status code:", response.status_code)

    except Exception as e:
        print("Error sending email:", e)
    
send_verification_email(to_email, name)