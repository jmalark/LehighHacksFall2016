


def baker(townName, bakerCount):
    print("You arrive at the bakery.")

    if bakerCount == 0:
        print("\"Hi! Welcome to ", townName, "'s one and only bakery. I would love to offer you some of our delicious desserts.\"")
        input()
        print("\"Unfortunately we're all out of sugar, so I can't make any more at the moment.\"")
        input()
        print("\"Hey wait a second! Would you mind doing me a favor and buying me some more sugar?\"")
        input()
        print("\"I'll give you some money and you can go to the store and buy me 13 pounds of sugar so I won't run out again before the parade.\"")
        input()
        print("He hands you money to buy sugar.")
        input()
        print("\"Thank you for your help!\"")
        input()

        bakerCount+=1


    elif bakerCount == 1:
        print("\"Hi! Have you bought the sugar?\"")
        input()
        print("\"Oh. You haven't? I can't make any more desserts until you bring me more sugar.\"")
        input()


    elif bakerCount == 2:
        print("\"Hi! Have you bought the sugar?\"")
        input()
        print("\"Oh dear. That doesn't seem to be enough sugar.\"")
        input()
        print("\"You're going to have to return that sugar to the store and buy the right amount.\"")
        input()
        print("\"Remember, I need 13 pounds of sugar. Try to buy the sugar in amounts that add up to exactly 13 pounds.\"")
        input()

    elif bakerCount == 3:
        print("\"Hi! Have you bought the sugar?\"")
        input()
        print("\"Oh dear. You seem to have bought too much sugar.\"")
        input()
        print("\"I don't have enough room for all of that. \"")
        input()
        print("\"You're going to have to return that sugar and buy the right amount.\"")
        input()
        print("\"Remember, I need 13 pounds of sugar. Try to buy the sugar in amounts that add up to exactly 13 pounds.\"")
        input()

    elif bakerCount == 4:
        print("\"Hi! Have you bought the sugar?\"")
        input()
        print("\"You have? Oh that's wonderful. Thank you so much! I'll start making the desserts for the parade right now.\"")
        input()

        bakerCount+=1


    elif bakerCount == 5:
        print("You hear someone bustling in the kitchen. They seem to be humming cheerfully. You go unnoticed.")
        input()

        #so it only updates mayorCount once
        bakerCount += 1

    elif bakerCount == 6:
        print("You hear someone bustling in the kitchen. They seem to be humming cheerfully. You go unnoticed.")
        input()

    return bakerCount











