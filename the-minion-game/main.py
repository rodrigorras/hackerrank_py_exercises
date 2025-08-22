def minion_game(ar):
    # your code goes here
    Stuart = 0
    Kevin = 0
    L = len(ar)
    for i in range(len(ar)):
        # print()
        if ar[i] not in 'AEIOU':
            Stuart = Stuart + L - i
        else:

            Kevin = Kevin + L - i

    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)