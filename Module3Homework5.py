def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(123)
result3 = get_multiplied_digits(354)

print(result1)
print(result2)
print(result3)