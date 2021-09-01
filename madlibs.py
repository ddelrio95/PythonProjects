#string concatenation (how to put strings together)
#suppose we want to create a string that says "subscribe to_____"
youtuber = "Dario del Rio " #some string variable

#a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlip = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlip)