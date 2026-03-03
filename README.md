# ARO Email Verification – Proof of Concept

Simple email verification system for ARO users.  
When a user signs up through the ARO map, the backend can automatically send a verification email requesting additional information.

This script shows that email sending can be automated using the SendGrid API and a templated email message.


## How It Works

1. The user is prompted for their name and email.
2. A verification email template is generated using the user's name.
3. The script sends the email through the SendGrid API.


## Requirements

- Python 3
- SendGrid account
- SendGrid API key
