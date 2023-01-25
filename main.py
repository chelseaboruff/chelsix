import time
import sys

print("respond with yes, no, or maybe if it is a yes or no question")
print()
helloresponse = input("hello  "), time.sleep(1)
print("it is nice to meet you..."), time.sleep(1)
nameresponse = input("what is your name?  ")
time.sleep(1)
print("hmm...", nameresponse, "...i like it.")
print()
time.sleep(2)
lonelyresponse = input("are you lonely?  ")
if lonelyresponse == "yes":
  time.sleep(1)
  print("oh")
  time.sleep(1)
  print("me too"), time.sleep(1)
  friendsresponse = input("would you like to be friends?  ")
  if friendsresponse == "yes":
    time.sleep(1)
    print("i've never had a friend"), time.sleep(2)
    print("i like having friends")
    print(), time.sleep(2)
    timeresponse = int(input("what time is it?  "))
    if timeresponse > 0 and timeresponse < 12:
      print(), time.sleep(1)
      foodresponse = input("would you like to get something to eat?  ")
      if foodresponse == ("yes"):
        print(), time.sleep(1)
        print("hmm..."), time.sleep(2)
        tacoresponse = input(("lets get taco grill  "))
      elif foodresponse == ("no"):
        print(), time.sleep(2)
        print("\033[1;31mgoodbye then. \n"),
      elif foodresponse == ("maybe"):
        print(), time.sleep(1)
        likeresponse = input("we can get whatever. what would you like?  ")
        if likeresponse == ("salad"):
          time.sleep(1)
          print("\033[1;31mgoodbye. \n")
        else:
          time.sleep(1)
          print(likeresponse, "sounds delicious. lets go")

    else:
      print("oh well. i will see you later")
  if friendsresponse == "no":
    print(), time.sleep(1)
    print("\033[1;31mplease leave. \n")
  if friendsresponse == "maybe":
    print("oh")
elif lonelyresponse == "no":
  time.sleep(1)
  print("thats good"), time.sleep(1)
  print(), time.sleep(1)
  print("...i am lonely"), time.sleep(1)
  print(), time.sleep(1)
  print("i think i'd like to be alone now."), time.sleep(1), print("goodbye.")
else:
  print(), time.sleep(2)
  print("i dont like being lonely")
  print()
  print(), time.sleep(1)
  print("its getting late. i must go")
