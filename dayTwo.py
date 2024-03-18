import re

file = 'values.txt'
game_data = []
total = 0
total_pt2 = 0

with open(file, 'r') as file:
    for line in file:
        match = re.match(r'Game (\d+): (.+)', line)
        if match:
            game_id, scores = match.groups()
            game_total = {'gameID': int(game_id), 'Red': 0, 'Green': 0, 'Blue': 0}

            scores = re.findall(r'(\d+) (green|blue|red)', scores)
            for count, colour in scores:
                count = int(count)
                if count > game_total[colour.capitalize()]:
                    game_total[colour.capitalize()] = count

            game_data.append(game_total)

for dict in game_data:
    if dict.get('Red') <= 12 and dict.get('Green') <= 13 and dict.get('Blue') <= 14:
        total += dict.get('gameID')
for dict in game_data:
    final = dict.get('Red') * dict.get('Green') * dict.get('Blue')
    total_pt2 += final

print('Part one total:', total)
print('Part two total:', total_pt2)
