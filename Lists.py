import math

squares = []
for x in range(10):
    squares.append((x**2))

# print(squares)

squares3 = [x**2 for x in range(11)]
# print(squares3)

list_comp = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]
# print(list_comp)

list_vec = [x*2 for x in [-4, -2, 0, 2, 4]]
# print(list_vec)

list_sqrt = [math.sqrt(x) for x in [4, 9, 25, 36]]
print(list_sqrt)


