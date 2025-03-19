# 12/20/24
# python crash course
# 3-8
favs = ['japan', 'italy', 'thailand', 'uk', 'korea'] # initialize
print('Raw List:')
print(favs) # raw list
print('\nSorted; Alpha; Non-destro:')
print(sorted(favs)) # sorted alpha non destructive
print('\nOriginal Raw List:')
print(favs) # original raw list
print('\nSorted; Reverse-alpha; Destro:')
favs.reverse() # sorted rev-alpha destro
print(favs) # reversed list
favs.reverse() # set back to original order
print('\nReturn to Original Order:')
print(favs) # orginal order
favs.sort() # this is destructive!
print('\nSorted; Alpha; Destro')
print(favs)
favs.sort(reverse=True)
print('\nSorted; Rev-alpha; Destro')
print(favs)