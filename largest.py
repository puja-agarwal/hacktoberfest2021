# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


res = maximum(2, 3, 1)

print("The largest number is", res)
