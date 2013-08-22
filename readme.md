gmail_status_unread_count.py
-----

A script to set your gmail status based on the number of unread messages in your gmail inbox.

*Github*: http://github.com/gkovacs/gmail_status_unread_count

*Author*: Geza Kovacs http://gkovacs.github.com

Usage
-----

1) Download the script:

    wget https://raw.github.com/gkovacs/gmail_status_unread_count/master/gmail_status_unread_count.py

2) Install [xmpppy](http://xmpppy.sourceforge.net/). If you're on Ubuntu, you can run:

    sudo apt-get install python-xmpp

3) Create a pair of files, 'gmail_username.txt' and 'gmail_password.txt', containing your gmail credentials:

    echo 'my_gmail_username' > gmail_username.txt
    echo 'my_gmail_password' > gmail_password.txt

3) Run the script:

    python gmail_status_unread_count.py

You can supply a custom message in the first argument, and a refresh interval with the second argument. For example:

    python gmail_status_unread_count.py 'NUM_UNREAD new messages in my inbox.' 10

FAQ
---

*Q*: Who in their right mind would use this?

A: People with [Type-A personality](http://en.wikipedia.org/wiki/Type_A_personality). You're reading this, so you must be one of them. Welcome to the club!

*Q*: What on earth is this useful for?

*A*: Good question. Ask the people who use it.

*Q*: I'd like you to add a kitchen sink, and a unicorn.

*A*: [Patches welcome](https://github.com/gkovacs/gmail_status_unread_count/pulls)


