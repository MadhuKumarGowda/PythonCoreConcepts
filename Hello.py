tot = 0
for i in [5,4,3,2,1]:
    tot = tot + 1
print(tot)
smallest_so_far = None
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num is None:
    if the_num < smallest_so_far:
      smallest_so_far = the_num
print(smallest_so_far)