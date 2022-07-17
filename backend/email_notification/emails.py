import json
# gets all eamails from users and returns as a list
def get_emails_from_users(users):
    emails = []
    for user in users:
        emails.append(user['email'])
    return emails
