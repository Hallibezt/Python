
# rt - open file in text mode, rb- open file in binary mode 
f = open('configuration.txt', 'rt')
content = f.read(5)
print(content)
#Python starts with the next 3 char - somehow remembers the previous
#This is the 'cursor' thing
content = f.read(3)
print(content)
#print where the cursor is currently in the file f
print(f.tell())
#move cursor to the beginning
f.seek(0)
content = f.read(5)
print(content)
print(f.closed)
f.close()
print(f.closed)


