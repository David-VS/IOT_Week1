def find_name(list, name):
    index = list.index(name)
    return index

list = ["Jan","Piet","Joris","Korneel","Joske"]
index = find_name(list, "Joris")
print(index)
index = find_name(list, "Jan")
print(index)


numbers = [1,2,3]
numbers[1] = 23
numbers[2] = 1.5

print(numbers)