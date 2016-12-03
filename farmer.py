__author__ = 'Alexandra'

def farmer(scientistCount):
    print("You arrive at the farm.")
    if scientistCount < 2:
        input("The farmer doesn't seem to be home. Maybe she'll be back later. Hit enter to go somewhere else.")
        return scientistCount
    elif scientistCount == 2:
        input("The farmer is outside, watching her cows in the pasture. You notice a little stream that runs right through"
              "the pasture down to the river. It's banks are bare; only dirt and rocks surround it - except for the occasional cow patty.")
        print()
        input("You mention this to the farmer, who looks surprised. \"Oh! I'd better fix that by redirecting this stream "
              "to prevent the manure from contaminating the water. It'll be pretty dull work, but since you're here you can make it more fun by"
              " answering my riddles as I work!\"")
        print()
        print("\"I am a type of animal\nSome say that I have a long face\nI'm very good at running fast\nSo people ride me in a race.\"")
        print("\"What am I?\"")
        resp = input("Enter your response: ")
        checkInput(resp, 'horse')
        input("\"Nice! You worked that out really well! Let's do another one.\"")
        print()
        print("\"This animal gives us meat\nOn which you sometimes dine\nIt gives us tasty bacon\nAnd it's sometimes known as swine.\"")
        print("\"What am I?\"")
        resp = input("Enter your response: ")
        checkInput(resp, 'pig')
        input("\"Wow, that was some great reasoning you did there! And I'm done redirecting the stream. It might not clear up quickly,"
              "but it will get better eventually.\"")
        scientistCount+=1
        input("\"It was great talking to you, kid, but I have to go tend my crops. See you later at the parade!\"")
        input("The farmer walks off, and you head somewhere else.")
        return(scientistCount)
    elif scientistCount > 3:
        input("The farmer is still off tending her fields. You should go somewhere else.")
        return scientistCount





def checkInput(string, ans):
    string = string.strip().lower()
    while ans not in string:
        print("\"Sorry, that's not it. Try again!\"")
        string = input("Enter your response: ").strip().lower()
