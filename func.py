def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter+two)


sum = get_summ("Learn", "python").upper()

print(sum)
