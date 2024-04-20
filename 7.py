values = {'M': 1, 'Y': 2, 'E': 5, 'N': 6, 'D': 7, 'R': 8, 'S': 9, 'O': 0}

SEND = values['S']*1000 + values['E']*100 + values['N']*10 + values['D']
MORE = values['M']*1000 + values['O']*100 + values['R']*10 + values['E']
MONEY = values['M']*10000 + values['O']*1000 + values['N']*100 + values['E']*10 + values['Y']

print('SEND:', SEND)
print('MORE:', MORE)
print('MONEY:', MONEY)