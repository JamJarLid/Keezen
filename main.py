#48 tiles around the board
#4 tiles for each colors' goal

from square import square


pavement = []

for row in range(1,14):
    for col in range(1,14):
        if row == 1:
            if col <= 5 and col >=9:
                s = new square (column = col, row = row)
                pavement.append(s)
        elif row >= 2 and row <= 4:
            if col == 5 or col == 9:
                s = new square(column = col, row = row)
                pavement.append(s)
        elif row == 5:
            if col <= 5 or col >= 9:
                s = new square(column=col, row=row)
                pavement.append(s)
        elif row >= 6 and row <= 8:
            if col == 1 or col == 13:
                s = new square(column=col, row=row)
                pavement.append(s)
        elif row == 9:
            if col <= 5 or col >= 9:
                s = new square(column=col, row=row)
                pavement.append(s)
        elif row >= 10 and row <= 12:
            if col == 5 or col == 9:
                s = new square(column=col, row=row)
                pavement.append(s)
        else:
            if col <= 5 and col >= 9:
                s = new square(column=col, row=row)
                pavement.append(s)
