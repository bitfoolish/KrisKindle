# This version will allow for an email to be sent to each person for who they will have to buy for

import random

import smtplib, ssl
from email.message import EmailMessage

import os
from dotenv import load_dotenv

load_dotenv() # load environment variables

senderEmail = os.getenv("SENDER_EMAIL")
senderPassword = os.environ.get("PASSWORD") 

#rcvrEmail = os.environ.get("RCVR_EMAIL")
names = {}

participant = input()
while participant != "end": # take in User's name + email
    TOKENS = participant.split()
    if (names.get(TOKENS[0].capitalize()) == None) : # if that name doesnt already exist, puts each inputted name in standardised form: joHn => John
        names[TOKENS[0].capitalize()] = TOKENS[1]
    else: # name already added to the pot
        print(f"That name {TOKENS[0].capitalize()} is already entered! Please enter a unique name")
    
    participant = input()

#print(names) 

msg = EmailMessage()
msg['Subject'] = "Your Kris Kindle !!"
msg['From'] = senderEmail

ogGifter = list(names.keys())# E.g. ['lisa', 'ann', 'mary'] => names of people involved in secret santa
ogGiftee = ogGifter.copy()  # ['lisa', 'ann', 'mary']

gifter = ogGifter.copy()
giftee = ogGiftee.copy()


gifts = len(gifter)
pairs = {}
x = 0
while(x < gifts):
    buy = (random.choice(gifter))
    rcvr = (random.choice(giftee))

#    print(names[buy], names[rcvr])
    if names[buy] != names[rcvr]: # if their email is not their own, i.e. avoid people buying for themselves
        gifter.remove(buy)
        giftee.remove(rcvr)

        pairs[buy] = rcvr
        x += 1
    
    elif ( (names[buy] == names[rcvr]) and (gifts - x == 1)):
        x = 0
        gifter = ogGifter.copy()
        giftee = ogGiftee.copy()
        print("mistakes were made, we go again")
        print(names)
        print(names[buy], names[rcvr])

for gifter, giftee in pairs.items():
    msg.set_content(f"You {gifter} got {giftee} !!")
    #print(gifter, " buys for ---> ", giftee)
    rcvrEmail = names[gifter]
    print("send this to " , rcvrEmail)

    context = ssl.create_default_context()
### RESHUFFLE this?
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # 465 is the port number for SSL
        server.login(senderEmail, senderPassword)
        msg['To'] = rcvrEmail
        server.send_message(msg) 
        del msg['To']
        