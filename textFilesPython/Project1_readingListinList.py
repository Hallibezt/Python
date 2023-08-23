

with open('devices.txt') as file:
    content = file.read().splitlines()
    # print(content)
    #Now I got the file in a list, now split the list into a new inner list with ',' as the separater
    devices = list()
    # Remove the header
    for line in content[1:]:   
        devices.append(line.split(':'))
    print(devices)
    #Get just the ipaddresses of the devices, iterate just the ip add:
    for device in devices:
        print(f'pinging {device[1]}')
    
    