# url : https://www.hackerrank.com/challenges/find-angle/problem


from math import atan, degrees


ab = int(input())
bc = int(input())
print(str(int(round(degrees(atan(ab/bc)), 0)))+'°')
