# url : https://www.hackerrank.com/challenges/
# find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    myList = sorted(set(arr), reverse=True)
    print(myList[1])
