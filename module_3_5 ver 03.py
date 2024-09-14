def get_multipled_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if number % 10 == 0:
        number = number // 10
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        second = number - (first * 10 ** (len(str_number) - 1))
        s = get_multipled_digits(second)
        return s * first


result1 = get_multipled_digits(423)
print(result1)
result2 = get_multipled_digits(40203)
print(result2)
result3 = get_multipled_digits(400002003)
print(result3)
result4 = get_multipled_digits(402003000)
print(result4)
