dat = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

def printTable(dat):
    innerLength = len(dat[0])    
    
    for j in range(innerLength):
        rowString = []
        for ls in dat:
            colWidths = len(max(ls, key=len))
            print(ls[j].rjust(colWidths, ' '), end=' ')
        print('\n')

printTable(dat)