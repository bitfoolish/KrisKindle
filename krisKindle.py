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
    numTokens = len(TOKENS) 
    partEmail = TOKENS[numTokens-1].lower()
    jointName = " ".join(TOKENS[:numTokens-1])

    if ( (names.get(jointName.capitalize()) == None) and (partEmail not in names.values()) ) : # if that name doesnt already exist, puts each inputted name in standardised form: joHn => John
        names[jointName.capitalize()] = partEmail
        #print(names)
    
    elif ( (names.get(jointName.capitalize()) != None) and ((partEmail not in names.values()))): # Non-Unique name, Unique email
        print("name??")
        print(f"That name {jointName.capitalize()} is already entered! Please enter a unique name")
    
    elif ( (partEmail in names.values()) and (names.get(jointName.capitalize()) == None)): # Non-Unique email, Unique name
        print("email??")
        print(f"That email {partEmail} is already entered! Please enter a unique email of your own")
    
    else: # Non-Unique name and Non-unique email
        print(f"{jointName, partEmail} have already been added")

    participant = input()

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
        # print("mistakes were made, we go again")
        # print(names)
        # print(names[buy], names[rcvr])


msg = EmailMessage()
msg['Subject'] = "Your Kris Kindle !!"
msg['From'] = senderEmail

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # 465 is the port number for SSL
    server.login(senderEmail, senderPassword)
    for gifter, giftee in pairs.items():
        rcvrEmail = names[gifter]
        msg['To'] = rcvrEmail
        msg.set_content(f"You {gifter} got {giftee} !!")
        server.send_message(msg) 
        del msg['To']
        print(f"Email sent to {rcvrEmail}!")
            