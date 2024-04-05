#Q1: The user is going to enter their full name from the keyboard (Assume that consists of 3 names: first, middle, last).They will all be entered on the same line. Write a program that displays the monogram of the persons name. Your program should continually ask for people’s names until a blank name is entered.

print("This program will ask you to enter your full name and will display your monogram.")
#asks the user their full name

while True:
  #loops the program
   
  name = input("Enter your full name (first, middle, last): ")
  #asks the user to enter their full name
    
  if name == "":
      #if the user enters nothing, the program stops
      
      break
      #stops the program
    
  name = name.split()
  #splits the full name into a list
   
  first = name[0][0].lower()
  #takes the first letter of the first name and makes it uppercase
   
  middle = name[1][0].lower()
  #takes the first letter of the middle name and makes it uppercase
   
  if len(name) >= 3:
    last = name[2][0].upper()
  else:
    last = ""
  #takes the first letter of the last name and makes it uppercase
    
  print("Your monogram is:", first, last, middle)
  #prints the monogram

#------------------------------------------------------------------------------------------#

#Q2: Write a program that asks the user to enter values from the keyboard. The user can enter any number of numbers that they want. All the numbers will be entered on 1 line, separated by spaces. Store those values in a list. Output the sorted list (sorted from lowest to highest). You cannot use a built in sorting function that might exist in python. 

print("This program will ask you to enter values from the keyboard. It will then sort the values from lowest to highest.")
#tells the user what the program does

values = input("Enter any values from the keyboard (numbers only, separated by spaces): ")
#asks the user to enter values from the keyboard

values_list = values.split()
#splits the values into a list

for index in range(1, len(values_list)):
  # loops the program

  value = values_list[index]
  # takes the value from the list
  i = index - 1
  # takes the index of the list

  while i >= 0 and value < values_list[i]:
    # loops the program again

    values_list[i + 1] = values_list[i]
    # swaps the values

    i -= 1
    # subtracts 1 from the index

  values_list[i + 1] = value
  # assigns the value to the sorted position

print(values_list)
# prints the sorted list

#------------------------------------------------------------------------------------------#

#Q3: A little kid has been given directions on how to get to school from his house. Unfortunately he lost the paper that tells him how to get home from school. Being that you are such a nice person, you are going to write a program to help him. Suppose his mother gave him a note that said the following: "This means that to get to his house from he had to turn RIGHT on King Street, Right on John, and Left to Home." The input for the program consists of the direction and the street to turn onto. The direction is entered first as L or R. The name of the street is entered next on a separate line of input. The input keeps going until SCHOOL is entered as the street name.

print(
  "This program will ask you to enter the directions to get from HOME to SCHOOL. It will then tell you how to get HOME from SCHOOL.")
#tells the user what the program does

originalDirection = input("What are the directions to get to school from home? ")
#asks the user to enter the directions to get to school from home

originalDirection = originalDirection.split()
#splits the directions into a list

index = len(originalDirection) - 1
#takes the index of the list

counter = 0
#sets the counter to 0

directions = []
#creates a list for directions

streets = []
#creates a list for streets

while counter <= index:
#loops the program
  
  if originalDirection[counter] == "R":
    #if the direction is right, it will add the street name to the list

    directions.append("L")
    #adds the direction to the list
    
    counter += 1
    #adds 1 to the counter
  
  elif originalDirection[counter] == "L":
    #if the direction is left, it will add the street name to the list
    
    directions.append("R")
    #adds the direction to the list
    
    counter += 1
    #adds 1 to the counter
    
  else:
    #if the direction is not right or left, it will add the street name to the list
    
    streets.append(originalDirection[counter])
    #adds the street name to the list
    
    counter += 1
    #adds 1 to the counter

print("To get home, follow these directions")
#tells the user to follow these directions

newCounter = 0
#sets the new counter to 0

streets.reverse()
#reverses the list

while newCounter < len(directions) and newCounter < len(streets):
  #loops the program
  
  print(directions[newCounter])
  #prints the direction
  
  print(streets[newCounter])
  #prints the street
  
  newCounter += 1
  #adds 1 to the new counter
  
print("Home")
#prints home

#------------------------------------------------------------------------------------------#

#Q4 Bonus: Create a program that will count exactly how many words "the" exist in the following: "The weather is nice outside in the day. The other day, when I went outside, it felt so nice to just breathe."

print("This program will count the number of times 'the' appears in the following sentence: 'The weather is nice outside in the day. The other day, when I went outside, it felt so nice to just breathe.'")
#tells the user what the program does

sentence = "The weather is nice outside in the day. The other day, when I went outside, it felt so nice to just breathe"
#the sentence

numThe = sentence.count("the") + sentence.count("The")
#counts the number of times 'the' appears in the sentence

print("The number of times 'the' appears in the sentence is", numThe)
#prints the number of times 'the' appears in the sentence
