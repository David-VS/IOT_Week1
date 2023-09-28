def find_name(list_to_search, name):
    index = list_to_search.index(name)
    return index


names_list = ["Jan", "Piet", "Joris", "Korneel", "franske"]
found_index = names_list.index("Jan")
print(found_index)
found_index = find_name(names_list, "Jan")
print(found_index)


numbers = [1, 2, 3]
numbers[1] = 23
numbers[2] = 1.5

print(numbers)
