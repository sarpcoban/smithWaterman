import numpy as np

word1 = input("Please enter the first word:\n")
word2 = input("Please enter the second word:\n")
match = input("Please enter the match reward:\n")
match = int(match)
mismatch = input("Please enter the mismatch penalty:\n")
mismatch = int(mismatch)
gap = input("Please enter the gap penalty:\n")
gap = int(gap)

#Matrix created
column = len(word1) + 1
row = len(word2) + 1
sw_matrix = np.zeros((row, column))



for i in range(1, row):
    for j in range(1, column):
        if word1[j-1] == word2[i-1]:
            sw_matrix[i][j] = sw_matrix[i-1][j-1] + match
        else:
            if sw_matrix[i - 1][j - 1] > sw_matrix[i - 1][j] and sw_matrix[i - 1][j - 1] > sw_matrix[i][j - 1]:
                sw_matrix[i][j] = sw_matrix[i - 1][j - 1] + mismatch
            else:
                sw_matrix[i][j] = max(sw_matrix[i - 1][j], sw_matrix[i][j - 1]) + gap
        if sw_matrix[i][j] < 0:
            sw_matrix[i][j] = 0



print("SW Matrix:\n",sw_matrix)


#Max value has been found
max_value = np.max(sw_matrix)
max_indices = np.where(sw_matrix == max_value)
max_indices_arr = []

for i in zip(max_indices[0], max_indices[1]):
    max_indices_arr.append(i)

sequence1_all = []
sequence2_all = []

for i in range(0,len(max_indices_arr)):
    row = max_indices_arr[i][0]
    column = max_indices_arr[i][1]
    sequence1 = []
    sequence2 = []
    while(sw_matrix[row][column] != 0):
        sequence1.append((word1[column-1]))
        sequence2.append(word2[row-1])
        row -= 1
        column -= 1
    sequence1.reverse()
    sequence2.reverse()
    sequence1_all.append(sequence1)
    sequence2_all.append(sequence2)


print("Sequence 1:",sequence1_all)
print("Sequence 2:",sequence2_all)
print("Score:", max_value)
