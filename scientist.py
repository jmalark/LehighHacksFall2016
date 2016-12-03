__author__ = 'Alexandra'

def scientist(scientistCount):
    if scientistCount == 0:
        #print("\"Oh no! The parade is going to be ruined! It's supposed to go by the river, but ",
              #"the river is a mess!\"")
        input("\"Oh no! The parade is going to be ruined! I'm supposed to make the float, but the river is a mess!\"")
        input("\"I can't focus until the river problem is solved! I don't know what's wrong with it.\"")
        #print("The scientist looks up at you, eyes filled with hope.", " \"Do you think...\"")
        input("The scientist looks up at you, eyes filled with hope. \"Do you think...\"")
        scientistCount+=1
    if scientistCount == 1 or scientistCount == 2:
        #print("\"Do you think you could go figure out what's wrong with the river?")
        input("\"Do you think you could go figure out what's wrong with the river?")
        print("Do you:\na: nod, agreeing to check out the river, and exit\nor\nb: slowly back away from the hopeful "
              "scientist before running out the door?")
        resp = checkInput(input())
        scientistCount=2
        return scientistCount
    elif scientistCount == 3:
        input("You tell the scientist what was going on with the river and the farmer. A look of relief washes over the scientist's face.")
        input("\"Wow, that little contaminated stream was really messing up the ecosystem of the river. It just goes to show that "
              "a little pollution is a big problem. Thanks for figuring out what was wrong; your observations and reasoning really saved the day!\"")
        input("\"Oh, but I should start working on that float! Thanks again for your help!\"")
        input("The scientist heads into the back room to start working of the float, and you head to the front door to go somewhere else.")
        scientistCount+=1
        return scientistCount
    elif scientistCount == 4:
        input("You can only see glimpses of the float, but it looks great. You leave the scientist to their work, and go somewhere else.")
        return scientistCount



def checkInput(string):
    string = string.strip().lower()
    while string not in ['a', 'b']:
        string = input("Please answer a or b: ").strip().lower()
    return string


