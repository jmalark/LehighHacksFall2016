

def mayor(mayorCount, townName):
    print("You walk up to the mayor.")
    if mayorCount == 0:
        print("Your mom is", townName,"'s mayor.")
        input()
        print("Today she is preparing for the annual parade.")
        input()
        print("\"Hmmm... We seem to be a bit behind schedule. I wonder what's holding everyone up.\"")
        input()
        print("\"Could you go and check up on everyone?\"")
        input()

        mayorCount += 1

    elif mayorCount < 5:
        print("\"Some people still aren't ready. Could you go try to help them?\"")
        input()

    elif mayorCount == 5:
        print("Your mom gives you a hug.")
        input()
        print("\"Thank you so much! Everyone I've talked to has said that you were a big help.\"")
        input()
        print("\"You're the real reason the parade can start on time.\"")
        input()
        print("\"Here, do you want to sit up on the float with me?\"")
        input()
        print("\"Have a cookie. They're fresh from the bakery and they are delicious.\"")
        input()
        print("As you sit on the float you wave at the smiling townspeople. Everyone seems excited.")
        input()
        print("Even the scientist seems less stressed out than usual.")
        input()
        print("The End.")
        input()
        print("Thanks for playing! You really made ",townName, "'s parade a success.")
        mayorCount += 1

    return mayorCount
