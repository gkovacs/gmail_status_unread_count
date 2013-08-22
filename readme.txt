A script to set your gmail status based on the number of unread messages in your gmail inbox.

Github: http://github.com/gkovacs/gmail_status_unread_count
Author: Geza Kovacs http://gkovacs.github.com

To use:

1) Install xmpppy http://xmpppy.sourceforge.net/
If you're on Ubuntu, you can run:
sudo apt-get install python-xmpp

2) Provide your gmail credentials:
Create a file 'gmail_username.txt' containing your gmail username
Create a file 'gmail_password.txt' containing your gmail password

3) Run the script:
python gmail_status_unread_count.py

You can supply a custom message in the first argument, and a refresh interval with the second argument. For example, the defaults are:
python gmail_status_unread_count.py 'NUM_UNREAD new messages in my inbox. See http://github.com/gkovacs/gmail_status_unread_count if you want to be cool like me.' 10

