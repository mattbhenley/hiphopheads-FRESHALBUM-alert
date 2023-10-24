import praw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Reddit API configuration
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Email configuration
smtp_server = 'your_smtp_server'
smtp_port = 587  # Change to your SMTP port
email_address = 'your_email@gmail.com'
email_password = 'your_email_password'
recipient_email = 'your_recipient_email@gmail.com'

# Subreddit and search query
subreddit = reddit.subreddit('hiphopheads')
search_query = "[FRESH ALBUM]"

def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, msg.as_string())
    server.quit()

def check_new_posts():
    for submission in subreddit.new(limit=10):  # Adjust limit as needed
        if search_query in submission.title:
            subject = submission.title
            message = submission.url
            send_email(subject, message)

if __name__ == '__main__':
    check_new_posts()
