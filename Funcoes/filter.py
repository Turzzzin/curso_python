values = [10, 12, 34, 44, 57]

def remove_under_20(x):
    return x > 20

formatedValues = filter(remove_under_20, values)

print(list(formatedValues))