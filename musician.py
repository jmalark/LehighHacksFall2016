

def musician(musicianCount, townName):
    print("You arrive at the musician's house.")
    if musicianCount == 0:
        print("You walk into a building littered with music sheets and various instruments.")
        input()
        print("\"W-why hello. Sorry I'm a bit frazzled right now, I'm very busy preparing for the parade.\"")
        input()
        print("The musician waves his arms around anxiously as he speaks. Suddenly a stack of music sheets falls over.")
        input()
        print("\"Oh no! The parade music was in that pile and I still have to get the instruments ready.\"")
        input()
        print("\"Could you help me out and put these back in order?\"")
        input()
        print("He hands you five sheets of paper.")
        input()
        print("\"This is a song about the history of ", townName,".\"")
        input()
        print("Anyway I'll leave you to it. Thanks!")
        input()
        musicianCount += 1
        musicianCount = orderStory(musicianCount)



    elif musicianCount == 1:
        print("\"You came back! Ready to try again?\"")
        input()
        musicianCount = orderStory(musicianCount)

    if musicianCount == 2:
        print("\"Thanks for putting those back in order for me. You really helped me out.\"")
        input()
        print("\"Do you think you could do one more thing before you go?\"")
        input()
        print("\"Could you help me figure out rhyming words to use in my song?\"")
        input()
        musicianCount += 1


    if musicianCount == 3:
        print("\"Ready to help me with my rhyme scheme?\"")
        input()
        musicianCount = rhyme(musicianCount)

    if musicianCount == 4:
        print("\"My song will be so much better now that I've figured out which words rhyme!\"")
        input()
        print("\"Thank you for your help!\"")
        input()


    if musicianCount == 5:
        print("You've already helped the musician. Now he needs time to perfect his song.")
        input()

    return musicianCount


def orderStory(musicianCount):
    answer = ""
    gotWrong = False
    while musicianCount == 1 and answer != "quit":
        if gotWrong:
            print("That doesn't look quite right. Try again.")

        print("Put the story in order. Type your answer like this: a b c d e except in the right order.")
        print("Or if you want to quit, type quit. ")
        print("a: The farmer worked hard to try to grow more food.")
        print("b: When the town first started out we only had a few houses and a farm.")
        print("c: Once there were more people living here, someone opened a store to sell things to those people.")
        print("d: And now today we have a farm, a store, and a bakery. Every year we celebrate our progress with a parade.")
        print("e: Then because the farm produced more food, more people we able to live here.")
        answer = input("Your answer: ").lower().strip()
        if answer == "b a e c d":
            musicianCount += 1
        else:
            gotWrong = True


    return musicianCount

def rhyme(musicianCount):
    answer = ""
    answerCount = 0
    gotWrong = False
    while answerCount == 0 and answer != "quit":
        if gotWrong:
            print("I don't think that rhymes. Try again.")
        print("\"What does few rhyme with?\"")
        print("a: foul")
        print("b: music")
        print("c: grew")
        answer = input("Type a, b, or c. You can quit by typing quit. ").strip().lower()
        if answer == "c":
            answerCount += 1
        else:
            gotWrong = True
    gotWrong = False
    while answerCount == 1 and answer != "quit":
        if gotWrong:
            print("I don't think that rhymes. Try again.")
        print("\"What does cake rhyme with?\"")
        print("a: sugar")
        print("b: bake")
        print("c: car")
        answer = input("Type a, b, or c. You can quit by typing quit. ").strip().lower()
        if answer == "b":
            answerCount += 1
        else:
            gotWrong = True

    gotWrong = False
    while answerCount == 2 and answer != "quit":
        if gotWrong:
            print("I don't think that rhymes. Try again.")
        print("\"What does store rhyme with?\"")
        print("a: more")
        print("b: money")
        print("c: sew")
        answer = input("Type a, b, or c. You can quit by typing quit. ").strip().lower()
        if answer == "a":
            answerCount += 1
        else:
            gotWrong = True

    if answerCount == 3:
        musicianCount += 1

    return musicianCount
