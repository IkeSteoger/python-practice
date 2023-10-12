tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    columnWidths = [0] * len(tableData)

    i = 0

    while i < len(tableData):
        columnWidths[i] = len(max(tableData[i], key=len))
        i += 1

    for x in range(len(tableData[0])):
        for y in range(len(columnWidths)):
            print(tableData[y][x].rjust(columnWidths[y]), end=' ')
        print(end='\n')

printTable(tableData)