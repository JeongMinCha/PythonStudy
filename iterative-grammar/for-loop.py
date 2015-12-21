# How to use 'for-loop'
#
# for value in collection:
#   # code using "value"

# "continue" keyword
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
print(total)

# "break" keyword
sequence = [1,2,0,4,6,5,2,1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value
print(total_until_5)

# If the collection has elements which is a tuple or list,
# you can use it like below sentence.
#
# for a, b, c in iterator:
#   # execution ...