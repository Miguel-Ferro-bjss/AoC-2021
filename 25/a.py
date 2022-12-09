def run():
    #code to run
    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    grid = []

    for line in f:
        row = [x for x in line]
        grid.append(row)

    moves = 0
    while(True):

        ng = move_east(grid)
        ng = move_south(ng)

        if (ng == grid):
            break
        
        grid = [x.copy() for x in ng]
        moves += 1

    print(moves+1)

def move_east(grid):

    ng = [x.copy() for x in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '>':
                nj = j+1 if j+1 < len(grid[0]) else 0
                if grid[i][nj] == '.':
                    ng[i][j] = '.'
                    ng[i][nj] = '>'
       
    return ng

def move_south(grid):

    ng = [x.copy() for x in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'v':
                ni = i+1 if i+1 < len(grid) else 0
                if grid[ni][j] == '.':
                    ng[i][j] = '.'
                    ng[ni][j] = 'v'

    return ng

if __name__ == '__main__':
    run()