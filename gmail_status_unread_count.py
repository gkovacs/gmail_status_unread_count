#!/usr/bin/env python
# A script to set your gmail status based on the number of unread messages in your gmail inbox.
# Github: http://github.com/gkovacs/gmail_status_unread_count
# Author: Geza Kovacs http://gkovacs.github.com

status_message_template = 'NUM_UNREAD new messages in my inbox. See http://github.com/gkovacs/gmail_status_unread_count if you want to be cool like me.'
gmail_username = open('gmail_username.txt').read().strip().lower().replace('@gmail.com', '')
gmail_password = open('gmail_password.txt').read().strip()
refresh_interval = 10.0 # number of seconds to wait until re-checking

import sys

if len(sys.argv) > 1:
  status_message_template = sys.argv[1]
if len(sys.argv) > 2:
  refresh_interval = float(sys.argv[2])

import imaplib
import warnings
warnings.filterwarnings('ignore') # silence DeprecationWarning messages
from xmpp import *
import imaplib

def set_status(username, password, message, message_type='default'):
  # username: your gmail username, no @gmail.com
  # password: your gmail password
  # message: what you want to set your gmail status to
  # message_type: either 'dnd' (do not disturb) or 'default' (available)
  cl=Client(server='gmail.com',debug=[])
  if not cl.connect(server=('talk.google.com',5222)):
    raise IOError('Can not connect to server.')
  if not cl.auth(username, password, 'gmail.com'):
    raise IOError('Can not auth with server.')
  cl.send(Iq('set','google:shared-status', payload=[
    Node('show',payload=[message_type]),
    Node('status',payload=[message])
  ]))
  cl.disconnect()

def get_num_unread_messages(username, password):
  # username: your gmail username, no @gmail.com
  # password: your gmail password
  imap_obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
  imap_obj.login(gmail_username, gmail_password)
  imap_obj.select()
  return len([x for x in imap_obj.search(None, 'UnSeen')[1][0].split(' ') if x.strip() != ''])

from time import sleep

while True:
  num_unread_messages = get_num_unread_messages(gmail_username, gmail_password)
  status_message = status_message_template.replace('NUM_UNREAD', str(num_unread_messages))
  if num_unread_messages == 1:
    status_message = status_message.replace('messages', 'message')
  print status_message
  set_status(gmail_username, gmail_password, status_message)
  sleep(refresh_interval)

