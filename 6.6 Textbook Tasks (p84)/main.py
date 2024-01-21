# -----------------------
# Title: Textbook Tasks p84
# Date: 
# -----------------------


# Version 1

import statistics

lotto = [21,15,44,60,24,35,36,42,9,46,10,3,46,26,25,26,50,13,1,9,3,31,25,5,28,39,11,4,38]

num = []
numFreq = []

# sort lotto list
lotto.sort()

# create a new list of items num[] from original list, only one instance of each item.
for item in lotto:
  if item not in num:
    num.append(item)
    
# search to see how many times each element of num[] appears in original list lotto[].
for i in num:
  total = lotto.count(i)    # count how many times each number appears in lotto[]
  numFreq.append(total)    # append this number of appearences to numFreq[]

# Print the sorted items and their frequencies 
print("Sorted list:", num)
print("Frequency: ", numFreq)



