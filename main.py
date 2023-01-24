import json

print('Введите название оборудования:')
name_1 = input().replace(' ', '_')

print('Введите количество параметров у оборудования:')
n = int(input())

dist_1 = {}

for i in range(n):
    print('Введите название параметра:')
    name = input()
    print('Введите значение параметра:')
    value = input()
    dist_1[name] = value

with open(f'/home/evgeny/Загрузки/{name_1}.json', 'w') as file_1:
    json.dump(dist_1, file_1)
