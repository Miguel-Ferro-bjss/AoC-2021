def run():
    #code to run
    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    count_0, count_1 = bit_count(f)

    epsilon = ''.join(['1' if x>y else '0' for (x,y) in zip(count_1,count_0)])
    gamma = ''.join(['0' if x=='1' else '1' for x in epsilon])

    print(int(epsilon, 2) * int(gamma, 2))

    oxygen = f.copy()
    co2 = f.copy()
    for i in range(len(f[0])):
        c_oxy = bit_count_at_pos(oxygen, i)
        c_co2 = bit_count_at_pos(co2, i)

        if len(oxygen) > 1:
            oxygen = list(filter(lambda o: o[i] == '0' if c_oxy[0] > c_oxy[1] else o[i] == '1', oxygen))
            
        if len(co2) > 1:
            co2 = list(filter(lambda c: c[i] == '1' if c_co2[0] > c_co2[1] else c[i] == '0', co2))
    
    # print(oxygen, co2)
    print(int(oxygen[0], 2) * int(co2[0], 2))

def bit_count(bit_arr):

    count_0 = [0*i for i in range(len(bit_arr[0]))]
    count_1 = [0*i for i in range(len(bit_arr[0]))]

    for i in range(len(bit_arr)):
        digit = bit_arr[i]
        for j in range(len(digit)):
            bit = digit[j]
            if bit == '0':
                count_0[j] += 1
            elif bit == '1':
                count_1[j] += 1

    return count_0, count_1

def bit_count_at_pos(bit_arr, pos):
    
    count = bit_count(bit_arr)

    return count[0][pos], count[1][pos]


if __name__ == '__main__':
    run()