i = 0
with open("trans.txt", "r", encoding="utf8") as in_file:
    bytes = in_file.read(5000) # read 5000 bytes
    while bytes:
        with open(str(i), 'w', encoding="utf8") as output:
            output.write(bytes)
        bytes = in_file.read(5000) # read another 5000 bytes
        i += 1

.rstrip()

content_list = content.splitlines()