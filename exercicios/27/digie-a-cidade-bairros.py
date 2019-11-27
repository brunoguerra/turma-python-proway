

csv = open('aula\\exercicios\\27\\bairros-sc.csv', 'r', encoding='utf8')

states = {}

for line in csv:
    line_in_list = line.strip().split(',')

    if len(line_in_list) < 3:
        continue
    uf = line_in_list[0]
    if uf not in states:
        states[uf] = {}
    
    city = line_in_list[2].lower()
    if city not in states[uf]:
        states[uf][city] = []
    
    if len(line_in_list) == 4:
        neighborhood = line_in_list[3]
        states[uf][city].append(neighborhood)

user_city = input('Type one city: ')

print(len(states['SC'][user_city.lower()]))
print(states['SC'][user_city.lower()])