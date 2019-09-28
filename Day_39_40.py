

def power(k, n):
    if n == 1:
        return k
    else:
        return k*power(k, n-1)


print(power(5, 3))
print("-------------------------")

num_list = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
x = list(filter(lambda y: y > 0, num_list))
print(x)





