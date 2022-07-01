'''
A script that uploads data to pastebin.com
'''
# Import needed packages
from win32com import client

import os
import random
import requests  # Crawler
import time

# Your pastebin account
username = '<Pastebin account here!>'
password = '<Pastebin password here!>'
api_dev_key = '<Pastebin API key here!>'


def plain_paste(title, contents):
    '''
    Just paste some data.
    '''
    login_url = 'https://pastebin.com/api/api_login.php'  # API login URL
    login_data = {
        'api_dev_key': api_dev_key,
        'api_user_name': username,
        'api_user_password': password,
    }
    r = requests.post(login_url, data=login_data)  # Request to login
    api_user_key = r.text

    paste_url = 'https://pastebin.com/api/api_post.php'
    paste_data = {
        'api_paste_name': title,
        'api_paste_code': contents.decode(),
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_option': 'paste',
        'api_paste_private': 0,
        }
    r = requests.post(paste_url, data=paste_data)  # Request to paste data
    print(r.status_code)  # Accept or not
    print(r.text)  # Response content


def wait_for_browser(browser):
    '''
    Detec whether the browser is ready or not
    '''
    while browser.ReadyState != 4 and browser.ReadyState != 'complete':
        time.sleep(0.1)


def random_sleep():
    '''
    Random sleep for a while so that the website don't ban you.
    '''
    time.sleep(random.randint(5,10))  # Randomly waits


def login(ie):
    '''
    Login pastebin
    '''
    full_doc = ie.Document.all
    for elem in full_doc:
        if elem.id == 'loginform-username':
            elem.setAttribute('value', username)
        elif elem.id == 'loginform-password':
            elem.setAttribute('value', password)

    random_sleep()
    if ie.Document.forms[0].id == 'w0':
        ie.document.forms[0].submit()
    wait_for_browser(ie)


def submit(ie, title, contents):
    '''
    Submit data.
    '''
    full_doc = ie.Document.all
    for elem in full_doc:
        if elem.id == 'postform-name':
            elem.setAttribute('value', title)

        elif elem.id == 'postform-text':
            elem.setAttribute('value', contents)

    if ie.Document.forms[0].id == 'w0':
        ie.document.forms[0].submit()
    random_sleep()
    wait_for_browser(ie)


def ie_paste(title, contents):
    ie = client.Dispatch('InternetExplorer.Application')
    ie.Visible = 1

    ie.Navigate('https://pastebin.com/login')
    wait_for_browser(ie)
    login(ie)

    ie.Navigate('https://pastebin.com/')
    wait_for_browser(ie)
    submit(ie, title, contents.decode())

    ie.Quit()

# Execute
if __name__ == '__main__':
    ie_paste('<Paste title here!>', 'Paste content here!')
