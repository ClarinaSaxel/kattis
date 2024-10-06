N=int(input())
match N%3:
    case 0:
        print(N//3)
        print(' '.join(['3']*(N//3)))
    case 1:
        print(N//3 + 1)
        print(' '.join(['3']*(N//3-1)), 2, 2)
    case 2:
        print(N//3 + 1)
        print(' '.join(['3']*(N//3)), 2)