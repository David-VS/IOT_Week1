def find_name(list, name):
    index = list.index(name)
    return index

index = find_name(["Jan","Piet","Joris"], "Joris")
print(index)



numbers = [1,2,3]
numbers[1] = 23
numbers[2] = 1.5

print(numbers)