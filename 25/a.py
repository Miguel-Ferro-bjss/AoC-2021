def run():
    #code to run
    # f = open('input.txt', 'r').read().strip().split('\n')
    f = open('test.txt', 'r').read().strip().split('\n')

    grid = []

    for line in f:
        row = [x for x in line]
        grid.append(row)

    print(grid)
    print()
    new_grid = move_east(grid).copy()
    moves = 0

    print(grid)
    print()
    print(new_grid)


    # while(new_grid != grid):
    #     new_grid = move_east(grid.copy())
    #     if new_grid == grid:
    #         break
    #     moves += 1
    #     grid = new_grid.copy()
    #     new_grid = move_south(grid.copy())
    #     if new_grid == grid:
    #         break
    #     moves += 1

    print(moves)

def move_east(grid):
    ng = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '>':
                nj = j+1 if j+1 < len(grid[0]) else 0
                if ng[i][nj] == '.':
                    ng[i][j] = '.'
                    ng[i][nj] = '>'
       
    return ng

def move_south(grid):
    ng = [x for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'v':
                ni = i+1 if i+1 < len(grid) else 0
                if ng[ni][j] == '.':
                    ng[i][j] = '.'
                    ng[ni][j] = 'v'

    return ng

if __name__ == '__main__':
    run()