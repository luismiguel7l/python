larg = float(input('LARGURA DA PAREDE: '))
alt = float(input('altura da parede: '))
area =larg * alt
print('sua parede tem a dimensao de {}x{} e sua área é de {}m2'.format(larg,alt,area))
tinta = area / 2
print ('para pintar essa parede, voce precisará de {}l de tinta'.format(tinta))