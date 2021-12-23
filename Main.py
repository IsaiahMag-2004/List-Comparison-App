 #Unit 2 Challange 2 List Comparison App

print("\n\t\tSummary Table\n")

#Create Lists
list_strings = ["red", "lit", "who", "joy"]
list_ints = [1, 3, 5, 6, 7]
list_floats = [10.3, 2.09, 5.2, 7.1]
list_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#String list summary
print(f"The variable list_strings is a {type(list_strings)}")
print(f"It contains the elements: {list_strings}")
print(f"The element {list_strings[0]} is a {type(list_strings[0])}")
print()

#Int List Summary
print(f"The variable list_strings is a {type(list_ints)}")
print(f"It contains the elements: {list_ints}")
print(f"The element {list_ints[0]} is a {type(list_ints[0])}")
print()

#Float List Summary
print(f"The variable list_strings is a {type(list_floats)}")
print(f"It contains the elements: {list_floats}")
print(f"The element {list_floats[0]} is a {type(list_floats[0])}")
print()

#List List summary
print(f"The variable list_strings is a {type(list_lists)}")
print(f"It contains the elements: {list_lists}")
print(f"The element {list_lists[0]} is a {type(list_lists[0])}")
print()

#Sort all
list_strings.sort()
list_ints.sort()

#Output Comparison
print("Now sorting list_strings and list_ints...")
print(f"  Sorted list_strings: {list_strings}")
print(f"  Sorted list_ints: {list_ints}\n")

print("Strings are sorted alphabetically, while integers are sorted numerically!!")
