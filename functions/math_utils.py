def fibonacci(how_much: int):
    if how_much < 1:
        return []
    elif how_much == 1:
        return [1]
    else:
        sequence = [1, 1]
        counter = 2
        while counter < how_much:
            counter += 1
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence
