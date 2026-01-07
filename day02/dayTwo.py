#comma code
''' 
def print_completely(list) :
    sizeOflist = len(list)
    sentence = ''

    if sizeOflist == 0 :
        return
    elif sizeOflist == 1 :
        return str(list[0])
    elif sizeOflist == 2 :
        return str(list[0]) + ' and ' + str(list[1]) 
    end = sizeOflist - 1
    for items in range(end):
        sentence += (str(list[items]) + ', ')
    sentence += 'and ' + str(list[end])
    return sentence



childNames = ['xeno', 'Dylan', 'xylan' , 'bob']

childNamesComlp = print_completely(childNames)
print(childNamesComlp)

'''
#Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

row = len(grid)
col = len(grid[0])

for i in range(col):
    for j in range(row):
        print(grid[j][i], end='')
    print('')

'''
  this problem solution is small and easy but took a while to conceptualize
  through the use of examples i found online especially for the row and col seting
  was very beneficial to the solution
'''