# Reverse an array
arr = [1, 2, 3, 4, 5]
rev = arr[::-1]
print("Reversed array:", rev)

# Find max and min
maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Max:", maximum)
print("Min:", minimum)

# Frequency of elements
freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)
