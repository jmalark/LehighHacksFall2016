__author__ = 'Alexandra'

def river(scientistCount):
    print("You arrive at the river.")
    if scientistCount == 0:
        input("The river looks very dirty and smells bad. You don't really want to be here.")
        input("Hit enter to go somewhere else.")
    elif scientistCount == 1 or scientistCount == 2:
        input("The river looks very dirty and smells bad, but you stay and look around for what may be the cause.")
        input("Up the hill you see a farm, from which there is a small, filthy stream of water flowing into the river.")
        input("It looks like manure or pesticides are getting into the water supply - you should talk to someone about that.")
        input("Hit enter to go somewhere else")
        scientistCount=2
    elif scientistCount >= 3:
        input("The river looks very dirty and smells bad, but you know that it will eventually clear up."
              " Maybe after the parade you can organize a clean up. For now, though, you head somewhere else.")
    return scientistCount