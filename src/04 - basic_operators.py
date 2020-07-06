"""
Basic Operators
"""

# 1. Addition, Subtraction, Multiplication, Division with Numbers
number = 1 + 2 * 3 / 4.0
print(number)

# 2. Modulo returns integer remainder of division
remainder = 5 % 10
print(remainder)

# 3. Exponentiation
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# 4. Addition operator to concatenate strings
helloworld = "hello" + " " + "world"
print(helloworld)

# 5. Multiplication to form a string with repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

# 6. Join lists with addition operator
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# 7. Form a new list with a repeated sequence with the multiplication operator
print([1, 2, 3] * 3)


"""
YOU DO
3 minute timer
"""
# assign 1 to `x`
# assign 2 to `y`

# Create two lists called `x_list` and `y_list`
# make `x_list` contain 10 instances of `x`
# make `y_list` contain 10 instances of `y`

# create a list called `combined` that
# contains 10 `x`s and 10 `y`s by concatenating
# `x_list` and `y_list`

x = 1
y = 2

x_list = []
y_list = []

i = 0
while i < 10:
    x_list.append(x)
    y_list.append(y)
    i = i + 1

combined = x_list + y_list

print(combined)
