from django.core.mail import BadHeaderError, send_mail, send_mass_mail

# send single email - can be used to send admin(s)/host(s) 
def send_email(from_email, to_email, subject, message):
    send_mail(
        subject,
        message,
        from_email,
        to_email
    )

#test
send_email('example@example.com', 'ngodarian@gmail.com', 'test', 'test')

# send mass email - used for sending invitees email notifications