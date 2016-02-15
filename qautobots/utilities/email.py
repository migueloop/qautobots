from __future__ import unicode_literals

import imaplib

from qautobots.framework.qanfig import get_config


def read_email(subject, deleted=True):
    """Read Email from server and delete it"""
    config = get_config()['email']
    mail = imaplib.IMAP4_SSL(config['incoming'])
    mail.login(config['username'], config['password'])
    mail.select(config['folder'])
    search_result = mail.search(None, '(SUBJECT "{0}")'.format(subject))
    mail_id = search_result[1][0]
    if mail_id == '':
        email_body = None
    else:
        email_content = mail.fetch(mail_id, '(BODY.PEEK[TEXT])')
        email_body = email_content[1][0][1]
        if deleted:
            mail.store(mail_id, '+FLAGS', '(\Deleted)')
            mail.expunge()
    mail.logout()
    return email_body
