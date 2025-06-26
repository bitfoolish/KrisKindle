import random

ogGifter = ['lisa', 'ann', 'mary']
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
#        print(buy, "gets: ",  rcvr)
        gifter.remove(buy)
        giftee.remove(rcvr)

        pairs[buy] = rcvr
        x += 1
    
    elif ( (buy == rcvr) and (gifts - x == 1)):
        x = 0
#        print(gifter) same person as giftee
#        print(giftee)
        gifter = ogGifter.copy()
        giftee = ogGiftee.copy()

#        print("gifter: " , gifter)
 #       print("giftee: ", giftee)
        print("mistakes were made, we go again")
##        break


print(pairs)