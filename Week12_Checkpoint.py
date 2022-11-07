"""There are several types of commands that are commonly found in object oriented programs.
 These types of commands are so common, that a programmer must be able to recognize and write them. 
One of these types of commands is calling the methods of an object using the dot operator (.) as shown in this template:"""

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.append("orange")
    print(fruit_list)

    where = fruit_list.index("apple")   #finds the index location of apple in the list
    fruit_list.insert(2, "cherry")   #inserts cherry at index 2
    fruit_list.remove("banana") #removes banana from the list
    last_elem= fruit_list.pop()  #removes the last element in the list
    sorted_list = sorted(fruit_list)   #sorts the list by alphabet
    fruit_list.clear()
    print(last_elem)
    print(fruit_list)
    print(sorted_list)
    print(fruit_list)

if __name__ == "__main__":
    main()

