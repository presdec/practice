file=open("new.txt",'w')
l = [1, 2, 3]
for item in l:
    file.write(str(item)+"\n")
file.close()