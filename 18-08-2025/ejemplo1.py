# -*- coding: utf-8 -*-
platos_peruanos = ['ceviche', 'lomo saltado', 'aji de gallina', 'pachamanca', 'juanes', 'ceviche', 'lomo saltado']
print(platos_peruanos.count('ceviche'))  # Salida: 2
print(platos_peruanos.count('anticuchos'))  # Salida: 0
print(platos_peruanos.index('lomo saltado'))  # Salida: 1
print(platos_peruanos.index('lomo saltado', 2))  # Encuentra la siguiente aparición de lomo saltado desde la posición 2, Salida: 6
platos_peruanos.reverse()
print(platos_peruanos)  # Salida: ['lomo saltado', 'ceviche', 'juanes', 'pachamanca', 'aji de gallina', 'lomo saltado', 'ceviche']
platos_peruanos.append('anticuchos')
print(platos_peruanos)  # Salida: ['lomo saltado', 'ceviche', 'juanes', 'pachamanca', 'aji de gallina', 'lomo saltado', 'ceviche', 'anticuchos']
platos_peruanos.sort()
print(platos_peruanos)  # Salida: ['aji de gallina', 'anticuchos', 'ceviche', 'ceviche', 'juanes', 'lomo saltado', 'lomo saltado', 'pachamanca']
print(platos_peruanos.pop())  # Salida: 'pachamanca'
