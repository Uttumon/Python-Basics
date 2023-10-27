"""
# Using break statement in a while loop
i = 0
while i < 10:
  i += 1
  if i == 5:
    break
  print(i)
# Using continue statement in a for loop
"""
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i)

# Output: 1 3 5 7 9
