#More efficient and common way to deal with files


with open('configuration.txt') as file:
    content = file.read()
    print(content)
#with statement opens file, but it is closed outstate the with    
print(file.closed)


#Read file into a list
# 1. split string 
with open('configuration.txt') as file:
    content = file.read().splitlines()
    print(content)

print('#' * 50)

# 2. f.readline()
with open('configuration.txt') as file:
    content = file.readlines()
    print(content)

with open('configuration.txt') as file:
    content = file.readline()
    print(content)
    print(file.readline(), end='')
    print(file.readline())

print('#' * 50)

# 3. Iterable file object = list(file)
with open('configuration.txt') as file:
    content = list(file)
    print(content)
    
print('#' * 50)


# 4. iterate over a file
with open('configuration.txt') as file:
    for line in file:
        print(line)