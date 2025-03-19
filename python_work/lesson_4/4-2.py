# 12/21/24
# Loop study
animals = ['turtle', 'frog', 'lizard'] # make list; common characteristic: green
for animal in animals:
    print(f'A {animal} would make a great pet.')
print('These animals are green.\n')
#//----------->
cubes = [] # make empty list
for value in range(1, 11): # use loop to populate list
    cubes.append(value**3) # powers of 3
for cube in cubes: # print each value in cubes
    print(cube)
#//----------->
numb_lst = [i**3 for i in range(1,11)] # make a list w/ one line of code!
for numb in numb_lst: # print each value in numb_lst
    print(numb)
# millions = list(range(1, 1_000_001))
# print(min(millions))
# print(max(millions))
# print(sum(millions))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())