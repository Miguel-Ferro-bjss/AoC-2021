def run():

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')
    # print(f)
    count = 0
    depth = int(f[0])

    for line in f:
        if int(line) > depth:
            count += 1
        depth = int(line)

    print(count)

    count2 = 0
    window = [int(x) for x in f[0:3]]

    for i in range(1, len(f)-2):
        next_window = [int(x) for x in f[i:i+3]]
        if sum(next_window) > sum(window):
            count2 += 1
        window = next_window
        
    print(count2)

if __name__ == '__main__':
    run()