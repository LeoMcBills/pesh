numbers = [0, 1, 2, 3]

print(numbers[1])

def add(x, y):
    return x + y

print(add(2, 2))
print(add(2, 3))
print(add(4, 5))


# 12 + 12.4
# print(type(z))

'''
12'/0'+'/0'12.4

['12', '+', '12.4']

'''

class Summer:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adder(self):
        return self.x + self.y
    

add1 = Summer(12, 12.4)

print(add1.adder())





