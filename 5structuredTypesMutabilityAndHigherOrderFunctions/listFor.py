
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT','Caltech'],['Harvard','Yale','Brown']]

for e in Univs:
    print('Univs contains',e)
    print('  which contains')
    for u in e:
        print('    ',u)

