#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element
# in the list, one at a time.
names = ["Alice", "Bob", "Charlie"]
print(names[0], names[1], names[2])

#Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name
names = ["Alice", "Bob", "Charlie"]
print(f"Hello, {names[0]}! How are you?")
print(f"Hello, {names[1]}! How are you?")
print(f"Hello, {names[2]}! How are you?")

#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several
# examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
transport = ["Honda Car", "Honda Motorcycle", "Honda Boat"]
print(f"I would like to own a {transport[0]}.")
print(f"I would like to own a {transport[1]}.")
print(f"I would like to fly in a {transport[2]}.")

#Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes
#at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guests = ["Alice", "Bob", "Charlie"]
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

#Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of
#invitations. You’ll have to think of someone else to invite.
print(f"Unfortunately, {guests[1]} can't make it to dinner.")
guests[1] = "Dave"
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

#More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner
print("Great news! We found a bigger dinner table.")
guests.insert(0, "Eve")
guests.insert(2, "Frank")
guests.append("Grace")
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")
print(f"Dear {guests[3]}, you are invited to dinner.")
print(f"Dear {guests[4]}, you are invited to dinner.")
print(f"Dear {guests[5]}, you are invited to dinner.")

#Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
guests = ["Eve", "Alice", "Frank", "Bob", "Charlie", "Grace"]
print("Unfortunately, we can invite only two people for dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, we can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")

del guests["Eve"]
del guests["Alice"]
print(guests)

#Seeing the World: Think of at least five places in the world you’d like to visit
places = ["Amsterdam", "Paris", "New York", "Rome", "Berlin"]

print("Original order:", places)
print("Alphabetical order:", sorted(places))
print("Original order still:", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Original order still:", places)
places.reverse()
print("Reversed order:", places)
places.reverse()
print("Back to original order:", places)
places.sort()
print("Alphabetical order:", places)
places.sort(reverse=True)
print("Reverse alphabetical order:", places)

#Dinner Guests: Working with one of the programs from Exercises 4 through 7 (page 42), use len() to print a message
#indicating the number of people you are inviting to dinner.
guests = ["Alice", "Bob", "Charlie"]

print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

print(f"I am inviting {len(guests)} people to dinner.")

#Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers,
#countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
#and then uses each function introduced in this chapter at least once
languages = ["Python", "JavaScript", "C++", "Java", "Ruby"]

languages.append("Go")
languages.insert(2, "Swift")
print("List:", languages)
languages.sort()
print("Sorted:", languages)
languages.reverse()
print("Reversed:", languages)
print("Length:", len(languages))
print("Pop:", languages.pop())
print("New_List:", languages)

#Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change
#an index in one of your programs to produce an index error. Make sure you correct the error before closing the program
languages = ["Python", "JavaScript", "C++", "Java", "Ruby"]
print=(languages[10])