from pprint import pprint
pprint([{'bin': bin(number), 'dec': number, 'oct': oct(number), 'hex': hex(number)} for number in range(16)])
