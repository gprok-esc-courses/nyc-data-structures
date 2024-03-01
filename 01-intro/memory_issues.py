
a = 5
b = 7
c = 5


# passing by value
def change_value(v):
    v = v * 2

# passing by reference
def change_list(data):
    data[0] *= 2


print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

change_value(a)
print(a)

d = [4, 5, 6, 7]
change_list(d)
print(d)