ora = input ('Hány Óra Van most?')
ora = int(ora)

if 8 <= ora <16:
    print('A Bolt nyitva van.')
    print('Ennyi órád van még odaérni', 16 - ora)
    
else:
    print('A bolt zárva van')
