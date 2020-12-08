# >>> file = open("example.txt",'r')
# >>> type(file)
# <class '_io.TextIOWrapper'>
# >>> content=file
# >>> print(content)
# <_io.TextIOWrapper name='example.txt' mode='r' encoding='UTF-8'>
# >>> content=file.read()
# >>> print(content)
# Line 1
# Line 2
# Line 3
# >>> type(content)
# <class 'str'>
# >>> content=file.readlines()
# >>> print(content)
# []
# >>> file.seek(0)
# 0
# >>> print(content)
# []
# >>> file.seek(0)
# 0
# >>> content=file.readlines()
# >>> print(content)
# ['Line 1\n', 'Line 2\n', 'Line 3']
# >>> content=[i.rstrp("\n") for i in content]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'str' object has no attribute 'rstrp'
# >>> content=[i.rstrip("\n") for i in content]
# >>> print(content)
# ['Line 1', 'Line 2', 'Line 3']
# >>> file.close()
# >>> content
# ['Line 1', 'Line 2', 'Line 3']
# >>>
# KeyboardInterrupt
# >>>
import os

file = open("057.txt",'r')
content = file.readlines()
file.close()
# Strip list and print without brackets
content=[i.rstrip("\n") for i in content]
print("\n".join(content))
print("================")
#figure out the length of each element in the list
for element in content:
    print (len(element.strip()))