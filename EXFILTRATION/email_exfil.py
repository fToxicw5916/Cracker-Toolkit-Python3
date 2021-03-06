'''
A script that sends data via email.
'''
# Import needed packages
import smtplib  # Used for emails
import time
import win32com.client  # Used for Windows Outlook

smtp_server = '<SMTP server address here!>'  # The SMTP server
smtp_port = <SMTP server port here!>  # SMTP server port
smtp_acct = '<Email account here!>'  # Account name
smtp_password = '<Email password here!>'  # Account password
tgt_accts = ['<List of accounts you are going to send to here!>']  # List of accounts you are going to send to


def plain_email(subject, contents):
    '''
    Just send a email.
    '''
    message = f'Subject: {subject}\nFrom {smtp_acct}\n'
    message += f'To: {tgt_accts}\n\n{contents.decode()}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_acct, smtp_password)

    # server.set_debuglevel(1)
    server.sendmail(smtp_acct, tgt_accts, message)
    time.sleep(1)
    server.quit()


def outlook(subject, contents):
    '''
    Specially designed for the Outlook application on Windows
    '''
    outlook = win32com.client.Dispatch("Outlook.Application")  # Open Outlook application
    message = outlook.CreateItem(0)
    message.DeleteAfterSubmit = True
    message.Subject = subject
    message.Body = contents.decode()
    message.To = 'boodelyboo@boodelyboo.com'
    message.Send()


if __name__ == '__main__':
    plain_email('<Subject here!>', '<Content here!>')
