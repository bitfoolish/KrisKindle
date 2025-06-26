import random

ogGifter = ['lisa', 'ann', 'mary'] # names of people involved in secret santa
ogGiftee = ogGifter.copy()  # ['lisa', 'ann', 'mary']

gifter = ogGifter.copy()
giftee = ogGiftee.copy()

gifts = len(gifter)

pairs = {}
x = 0
while(x < gifts):
    buy = (random.choice(gifter))
    rcvr = (random.choice(giftee))

    if buy != rcvr:
        gifter.remove(buy)
        giftee.remove(rcvr)

        pairs[buy] = rcvr
        x += 1
    
    elif ( (buy == rcvr) and (gifts - x == 1)):
        x = 0
        gifter = ogGifter.copy()
        giftee = ogGiftee.copy()

        print("mistakes were made, we go again")

for gifter, giftee in pairs.items():
    print(gifter, " buys for ---> ", giftee)