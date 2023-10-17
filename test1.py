# this is a comment

last_name = "Roman"
first_name = 'Samantha'
age = 99
price = 13.46
found = False


print(first_name)
print(last_name)

# operations with variables and concatination
print(first_name + " " + last_name)

# math 
print(age / 2)


#  You cant combine a string and a number
# print(first_name + age)  -- commented out to stop error -- 
# to make it work
print(first_name + str(age))




# decision flows if and else
# parenthasis is optional. its better without and makes it easier to read.
if age < 100:
    print("don't worry you are young")
    print("inside the if")
elif age == 100:
    print("Congradulations, you got to live 1 centery") # you can add as many elif as you like.. ex elif age == 200, elif age == 300
    
else:
    print("Sorry, you are getting old")


print("outside the if") # this line breaks the indentation and stops the if statement logic



# functions 
# to declare a function is called define or the definition of a function
def say_hello():
    print("Hello from a fn")

# a function with a paramater
def greet(name):
    print("Hello " + name)

# call a fns
say_hello()
say_hello()
say_hello()

greet("John")
greet("Juan")

