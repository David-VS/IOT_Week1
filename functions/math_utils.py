def fibonacci(how_much: int):
    if how_much > 2:
        values = [1, 1]
        count = 2
        while count < how_much:
            new_number = values[-1] + values[-2]
            values.append(new_number)
            count += 1
        return values
    return []


def fibonacci_bis(how_much: int):
    if how_much > 2:
        a = 1
        b = 1
        values = [a, b]
        count = 2
        while count < how_much:
            new_number = a + b
            values.append(new_number)
            a = b
            b = new_number
            count += 1
        return values
    return []
