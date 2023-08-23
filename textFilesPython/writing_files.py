
with open('myfile.txt', 'w') as file:
    file.write('A line \n')
    file.write(('New line \n'))

# a mode - append
with open('myfile.txt', 'a') as file:
    file.write('A line \n')
    file.write(('New line'))

#read and write open - r+  a file must exist before
with open('myfile.txt', 'r+') as file:
    file.write('A line with r+ \n')
    print(file.read())
 
