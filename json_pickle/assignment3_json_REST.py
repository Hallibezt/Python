import json
import requests
import csv



request = requests.get('https://jsonplaceholder.typicode.com/users')
obj = json.loads(request.text)

result = []
for person in obj:
    name = person['name']
    city = person['address']['city']
    gps_coordinates = (person['address']['geo']['lat'], person['address']['geo']['lng'])
    company_name = person['company']['name']
    result.append((name, city, gps_coordinates, company_name))


with open('people.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    head = ('name', 'city','GPS','Company')
    writer.writerow(head)
    for person in result:
        writer.writerow(person)


