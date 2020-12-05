line = 'FBFBBFFRLR'

temp = int(''.join('1' if c in 'BR' else '0' for c in line),2)

print(temp)
