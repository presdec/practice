# https://www.hackerrank.com/challenges/list-comprehensions/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    listijk = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if sum([i,j,k]) != n:
                    listijk.append([i,j,k])
    print(str(listijk))
