# Copy and paste this online python compiler address
# https://repl.it/languages/python3

# Then Copy and paste this code to that window's
# editor and hit run >

#pythonConversation 12/9/2019
print ("####################")
print ("#Python Convesation#")
print ("####################")
conversation = 1

while conversation < 2:
  print("------------------------------")
  print("You find yourself standing in a room.")
  print("You see two people there talking.")
  print("From here you can LISTEN to them.")
  action = input("WHAT NOW?:")
  print("------------------------------")
  print("You chose to "+(action)+".")
  if action == "listen":
    print("You hear the man sitting on the ground say, 'Hi Steve, how are you?'")

  if action == "help":
    print("You can LISTEN.")
#print(name)

