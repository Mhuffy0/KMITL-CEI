print("*** Clockwise Spiral Rectangle ***")
raw = input("Enter width height : ")

width, height = raw.split()
width = int(width)
height = int(height)

table = []
for i in range(height):
    table.append([0] * width)

# Clockwise directions.
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = 0  # current direction
x = 0  # current column
y = 0  # current row

for n in range(1, width * height + 1):
    table[y][x] = n

    # Look at the cell 
    next_x = x + dx[d]
    next_y = y + dy[d]

    # The bounds are checked BEFORE table[next_y][next_x]
    if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height or table[next_y][next_x] != 0:
        d = (d + 1) % 4  # % 4 wraps 3 (up) back to 0 (right)
        next_x = x + dx[d]
        next_y = y + dy[d]

    x = next_x
    y = next_y

# Every column is padded to the width of the biggest num
size = len(str(width * height))

for row in table:
    line = ""
    for value in row:
        text = str(value)
        text = " " * (size - len(text)) + text  # right align
        if line == "":
            line = text
        else:
            line += " " + text
    print(line)

print("===== End of program ======")
#create template table then check each cell in clockwise and fill.