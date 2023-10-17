# global vars 



# functions

def sum(num1, num2):
    result = num1 + num2
    print(result)


def division(num1, num2):
    # if the second number is a zero, print an error 
    # otherwise, divide and print the result
    if num2 == 0:
        print("error, zero division not aloud")
    else:
        result = num1 / num2
        print(result)


def print_greater(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)


def print_numbers():
    nums = [12,3,53,67,12,8,45,87,31,98,30,82,24,16,82,68,34]

    for n in nums:
        if n < 50:
            print(n)




def print_list():
    names = ["Jason", "Michael"]

    # add elements
    names.append("Samantha")
    names.append("Ricky")

    # read
    print(names[0])
    print(names[2])

    # check if element exist
    if not "Serigio" in names:
        names.append("Sergio")
        
    print(names)




def print_dict():
    me = {
        "name": "Samantha",
        "last": "Roman",
        "hobbies": ["fishing", "A", "B", "C"],
    }

    print(me)

    # read
    print(me["name"])

    # add a key
    me["age"] = 37

    # modify a key
    me["age"] = 38

    # modify a key name
    me["last-name"] = me["last"]
    del me["last"]

    print(me)

    # check if key exist before reading
    if "invalid" in me:
        print(me["invalid"])




# call functions with different numbers
sum(21, 21)
sum(-2, 345)
sum(12323124, 3423423)

division(100,10)
# should print 10
division(0, 10)
# should print 0
division(10, 0)
# should show an error 

print_greater(3, 7)
print_greater(10, 5)
print_greater(9, 9)


print("----------------------") # printing a seperation 
print_numbers()
print_list()
print_dict()