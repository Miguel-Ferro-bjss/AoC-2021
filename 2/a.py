def run():
    #code to run
    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    aim = 0
    x = 0
    depth = 0
    for line in f:
        cmd = line.split(" ")
        if cmd[0] == "forward":
            x += int(cmd[1])
            depth += aim * int(cmd[1])
        elif cmd[0] == "up":
            aim -= int(cmd[1])
        elif cmd[0] == "down":
            aim += int(cmd[1])
        # print(x, depth, aim)
    print(aim * x)
    print(depth * x)

if __name__ == '__main__':
    run()