# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = input().split()
    array = input()
    A = set(input().split())
    B = set(input().split())

    # n, m = 5, 5
    #
    # array = [999999991, 999999992, 999999993, 999999994,  999999999]
    # A = {999999991, 999999993, 999999995, 999999999, 999999997}
    # B = {999999990, 999999992, 999999996, 999999998, 999999994}

    # Initialize happiness
    happiness = 0

    # Calculate happiness
    for number in array:
        if number in A:
            happiness += 1
        if number in B:
            happiness -= 1

    # Print the result
    print(happiness)


