from sys import stdin

stdin.readline()
cells = [int(i) for i in stdin.readline().split(" ")]

previous = cells[0]
penultimate = 0
for i in range(1, len(cells)):

    if i >= 2:
        if previous < penultimate + cells[i]:
            penultimate, previous = previous, penultimate + cells[i]
        else:
            penultimate = previous
    else:
        penultimate = previous
        previous = cells[i]

print(previous)
