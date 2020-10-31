from math import *

#      |____this a module
# print function, open and close parenthesis = (), String = ""
# code gets executed in order (Top to Bottom)
print("Hello Friend")

# three types of data : String, Numbers, Boolean
# character_name is an example of a variable
# use _ when using 2 words in a variable (use character_name, not charactername or character name)
character_name = "John"
character_age = 30
is_male = False
is_female = True

# you can use ,, or ++ to concatenate
print("Hello World")
print("There was once a man called " + character_name + ", ")

# you cant concatenate strings with numbers
# so convert it to the same data type
print("he was", str(character_age), "years old")

print("he really likes the name george")
print("he didn't like being 70")

# create a new line
print("Hello\nBoi")

# you cant just print a quotation. use backslash(called escape character) to render to literally
print("hi\"hi")
# or a slash
print("hi\\hi")

# variable is basically just a container where we can store data values
# you can print variables
phrase = "Python"
print(phrase)

# concatenation
print(phrase + " is cool")

# some common functions
# .lower function will convert all the string to lower case
print(phrase.lower())
# .upper will convert all string to upper case
print(phrase.upper())
# check to see if the string is entirely upper case or lower case
# will give a true or false value
print(phrase.islower())
print(phrase.isupper())
# clarification
phrase2 = "HELLO"
print(phrase2.isupper())

# you can use functions in combination with each other
# first it will convert to upper then check is the string is all upper case
phrase3 = "hello world"
print(phrase3.upper().isupper())

# len(string) will check the amount of characters in the string, it will count spaces as well
example = "hello Friend"
print(len(example))

# you can grab individual characters from a string, the index starts with ZERO
# use SQUARE brackets to grab certain characters
print(example[0])

# index function, it will tell us where a specific character OR string is located inside our string
# if a certain character or string is repeated it will give the index of the first place it appears
print(example.index("F"))
#                    |_this is a parameter
# you can put words or pieces of words as the parameter
print(example.index("hello"))
print(example.index("Fri"))

# replace function, replaces certain letters or strings with other ones, Needs two parameters
print(example.replace("hello", "New"))

# if there are two, both will be replaced
print(example.replace("e", "f"))

# google more python functions

# Numbers/ uses bodmas
print(4), print(3.4), print(-3), print(1 + 3), print(2 * 4), print(4 / 5)
print(3 * 4 + 5), print(3 * (4 + 5))
# modulus function, Divide the first number by the second number and spit out the remainder
# read as 10 mod 3
print(10 % 3)

# convert number to string so that you can concatenate with other strings
my_num = 5
print(str(my_num) + " is my lucky number")

# a function is a collection of code that does something
# common math functions
# abs - gives the absolute value of a number
my_num2 = -4
print(abs(my_num2))

# pow - can enter two parameters/ can enter two pieces of information,
# first is going to be the number and the second is the power that you want to take the number to
print(pow(3, 2))

# max - its going to return the larger number of the two numbers
print(max(5, 8))

# min - return the smaller number of the two
print(min(6, 1))

# round - rounds a number, follows standard rounding rules
print(round(3.6))
print(round(3.1))

# if you want to access specific math functions you can import them, but it should be at the top of the code
# floor - grab the lowest number, rounds the number to the smallest number
print(floor(3.7))

# ceil - does the opposite of floor, round the number to the largest number
print(ceil(4.1))

# sqrt - gives the square root of a number
print(sqrt(25))

# there are many math functions, just google

# getting information/input from user, then storing it in a variable then printing it
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

# building a calculator
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
answer = num1 + num2
print(answer)
# oops you get a wrong answer because by default python takes in input as string
# you need to convert it to integer
# you can use the int function only on a whole number
answer = int(num1) + int(num2)
print(answer)
# therefore use float function, it can take in decimal values unlike int
answer = float(num1) + float(num2)
print(answer)

# XXX MAD LIBS GAME WAS EXCLUDED XXX

# when dealing with large amounts of data, lists are used
# lists are essentially just a structure where we can store information
# when you use square brackets python knows that this is a list
# you can store data of any type inside a list
friends = ["Kevin", "Karen", "Jim"]
# index pos =0/-3     1/-2    2/-1
# you can just print a list
print(friends)
# if you want to print out a specific element inside this list
# you need the index position of the particular element you want to print
print(friends[0])
print(friends[-2])
# accessing portions
# lets say we want to access the last two elements in friends
print(friends[1:])
#              |_this here tells us the bounds(from here to here)
# leaving a space means it will go to the end of the list

# new list for better illustration
new_friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#                 0        1       2       3        4
print(new_friends[1:3])
#                  |_ this grabbed all elements from 1 upto 3 but not including 3
# you can also modify elements
# lets say we want to modify Karen to Mike
new_friends[1] = "Mike"
# |_ this will automatically update the list where it is no longer Karen but Mike

# LIST FUNCTIONS
lucky_numbers = [4, 8, 15, 16, 23, 42]
people = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# Extend function = allow you to take a list and append(add) another list to it
people.extend(lucky_numbers)
# |_this will update the people list, so the next time you print people, it will have lucky numbers in its list too
print(people)

# Append function = add individual elements to a list
people.append("Creed")
print(people)

# Insert function = takes two parameters, the first parameter will be the index where you want to insert the item
# the second parameter is what you want to add to that particular index position,
# all the other items after that index will be pushed to the right
people.insert(1, "Kelly")
print(people)

# Remove function = basically removes that item
people.remove("Jim")
print(people)

# Clear function = if you want to remove all data in a list and reset it
people.clear()
print(people)

# Pop function = it will pop out a item from the list/ removes the last element from the list
new_numbers = [1, 2, 3, 4, 5]
new_numbers.pop(2)
print(new_numbers)

# index function = to find the index position of a element
print(new_numbers.index(1))
# this gives you 0 because the element 1 is in the index position 1

# count function = tells you how many times it appears in the list
count_explained = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]
print(count_explained.count(8))

# sort function = sorts the list in ascending order (alphabetical order or numerical order)
sort_explained = [3, 4, 2, 8, 9, 7]
sort_explained2 = ["Robert", "Neva", "Aaron", "Jim"]
sort_explained.sort()
sort_explained2.sort()
print(sort_explained)
print(sort_explained2)

# reverse function = basically reverses the list, first becomes last and so on
reverse_explained = [1, 2, 5, 7, 4, 2]
reverse_explained.reverse()
print(reverse_explained)

# copy function = you can copy all the elements in a list to another list
copy_explained = [1, 2, 5, 4, 8, 4, 2]
copy_explained2 = copy_explained.copy()
print(copy_explained2)

# TUPLES
# it is a type of data structure which means its a container where we can store different values
# similar to a list but it has key differences
# how to create a tuple, uses parenthesis
# a tuple is immutable(cant be changed or modified)
coordinates = (4, 5)
# you can access elements in a tuple
print(coordinates[1])


# use tuples on data that will never change

# functions in python
# a function is basically a collection of code that performs a specific task
# how to create a function
# saying hi
# automatically indented(tells us that it belongs to the same function)
def say_hi():
    print("Hello Friend")


# the code inside a function doesn't automatically execute we have to call it
say_hi()


# |_ that is how you call a function


# look at this
def say_hi2():
    print("Hello Friend")


print("Top")
say_hi2()
print("Bottom")


# when naming functions use all lowercase

# giving information/ parameter(information that we give to the function)
def say_hi3(name3):
    print("Hello " + name3)


say_hi3("Neva")
say_hi3("Steve")


# another more advanced example
def say_hi4(name4, age4):
    print("Hello " + name4 + " you are " + age4)


say_hi4("Neva", "17")


# ANOTHER ONE
def say_hi5(name5, age5):
    print("Hello " + name5 + " you are " + str(age5))


say_hi5("Mike", 3)


# RETURN statement
# sometimes when we call a function we want to get information back from that function


# here it doesn't  display a answer, even if we use the print statement
def cube(num123):
    num123 * num123 * num123


print(cube(3))


# corrected version
def cube_correct(num_correct):
    return num_correct * num_correct * num_correct


print(cube_correct(3))
# therefore the return function basically allows us to return a value back to caller
# you cant put code under a return keyword, it basically ends the function


# IF statements
# special structure in python where we can help our programs make decisions
# you can execute code when certain conditions are true
is__male = True

if is__male:
    print("You are male")

# using ELSE statement
is_18 = False

if is_18:
    print("You are 18")
else:
    print("You are not 18")

# more advanced
# using OR
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("you are neither male nor tall")

# using AND
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall or both")
else:
    print("you are either not male or not tall or not both")

# using ELIF and NOT
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall or both")
elif is_male and not is_tall:
    print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male but you are tall")
else:
    print("you are not male and not tall")


# if statements and comparisons
# getting true or false values using comparisons
def max__num(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_1 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3


print(max__num(400, 1000, 900))

# basic comparison operators
# |_____ == checks to see if both values are equal
# |_____ != this says not equal
# |_____ >, <, <=, >=

# building a better calculator

num1 = float(input("Enter First Number: "))
operator = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")

# dictionaries
# is a special structure where we can store information called key value pairs
# ___dictionary name
# |
month_corrections = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
#    |__Keys   |___Values


# there are different ways to access entries in a dictionary
# this
print(month_corrections["Jan"])

# we use get when we want a answer and not a error to when there is no entry like that in the dictionary
# we can set a default value if the key is not found
print(month_corrections.get("Dec", "Not a valid key"))
#                                    |____default value to display if you put in a invalid key


# WHILE loop
# structure in python which allows us to loop and execute a block of code multiple times
# we can set to loop repeatedly until a certain condition is met


i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# building a guessing game

secret_word = "neva"
guess = ""

while guess != secret_word:
    guess = input("Enter your guess: ")


print("You guessed the word correctly")

# improved version
# limiting the number of time the user can guess


secret_word = "neva"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose")
else:
    print("You guessed the word correctly")


# FOR loop
# allows us to loop over different collection's of items

for letter in "Nevanjith":
    print(letter)

#
friends = ["Jim", "Karen", "Kevin"]
for friends in friends:
    print(f)