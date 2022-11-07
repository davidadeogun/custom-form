"""Procedural programming focuses on the process or the steps 
to accomplihs a task."""

# Example 1

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")


# Call main to start this program.
if __name__ == "__main__":
    main()

"""Declarative programming focuses on what we want from the task,
or in other words, we focus on the desired result. or example, SELECT AVG from TABLE,
how the computer does it is none of my business. But a declarative programming cannot be 
successful without the procedural programming that tells the computer the steps to take to
perform a task."""
#Example 2

"""SELECT AVG(numbers) FROM table;"""


"""Functional programming focuses on the functions necessary to accomplish a task"""
# Example 3

from datetime import datetime
from functools import reduce

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")


# Call main to start this program.
if __name__ == "__main__":
    main()

"""Object Oriented Programming is based on the concept of objects. An object is a piece of a program that contains
both data (also kown as atttibutes) and functions (also known as methods)."""
# Example 4

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""There are several types of commands that are commonly found in object-oriented programs.
These types of common are so common, that a programmer must be able to recognize and write them.
Theree of these types of commands are:"""

#Creating objects. An example:
obj = datetime.now()

#Accessing the attributes of an object using the dot operator(.)
year = obj.year

#Calling the methods of an object using the dot operator (.)
new_obj = obj.replace(year=2035)
day_of_week = obj.weekday()

#EXAMPLE 5
def main():
    #Create an empty list that will hold fabric names.
    fabrics = []

    #Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    #Insert an element at the beginning of the fabrics list
    fabrics.insert(0, "chiffon")

    #Get the index where velvet is stored in the fabrics list
    i = fabrics.index("velvet")
    

    #Replace velvet with tafetta
    fabrics[i] = "taffeta"

    #Remove the last element from the fabrics list.
    fabrics.pop()

    #Remove denim from the fabrics list
    fabrics.remove("denim")

#Call main to start the program.
if __name__ == "__main__":
    main()


"""
Method	          Description
d.clear()	Removes all the elements from the dictionary d.
d.copy()	Returns a copy of the dictionary d.
d.get(key)	Returns the value of the specified key. Calling the get method is almost equivalent to using square brackets ([ and ]) to find a key in a dictionary.
d.items()	Returns a list that contains the key value pairs that are in the dictionary d.
d.keys()	Returns a list that contains the keys that are in the dictionary d.
d.pop(key)	Removes the element with the specified key from the dictionary d.
d.update(other)	Updates the dictionary d with the key value pairs that are in the other dictionary.
d.values()	Returns a list that contains the values that are in the dictionary d."""


# Example 6

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students.get(id)

    if name:
        # Print the student name.
        print(name)

        # Remove the student that the user
        # specified from the dictionary.
        students.pop(id)
    else:
        print("No such student")
    print()

    # Use a for loop to print each key value pair
    # in the dictionary. Of course, the code in
    # the body of a loop can do much more with
    # each key value pair than simply print it.
    for key, value in students.items():
        print(key, value)


# Call main to start this program.
if __name__ == "__main__":
    main()