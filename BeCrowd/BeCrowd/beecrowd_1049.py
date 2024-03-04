x = input()
y = input()
z = input()
if x == 'vertebrado':
    if y == 'ave':
        if z == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif y == 'mamifero':
        if z == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if y == 'inseto':
        if z == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    elif y == 'anelideo':
        if z == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')


