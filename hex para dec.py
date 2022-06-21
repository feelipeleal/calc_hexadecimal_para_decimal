numero_hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
 
hex = input(" ").strip().upper()
dec = 0

length = len(hex) -1
 
for digit in hex:
    dec += numero_hexa[digit]*16**length
    length -= 1
 
print(" ",dec)