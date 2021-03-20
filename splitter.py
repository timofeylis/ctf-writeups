#prints the solution to picoCTF vault-door-3 plus some debugging stuff
#doing it manually would have been painstaking

import string
foo = "j U 5 t _ a _ s n a _ 3 l p m 1 8 g b 4 1 _ u _ 4 _ m f r 3 4 0"
bar = foo.split()
flag = [''] * 32
print(flag)

for i in range(0, 8):
    flag.insert(i, bar[i])

for i in range(8, 16):
    flag.insert(i, bar[23-i])

for i in range(16, 32, 2):
    flag.insert(i, bar[46-i])

for i in range(31, 15, -2):
    flag.insert(i, bar[i])
print(flag)
print(''.join(flag))
print(len(''.join(flag)))
print(len("jU5t_a_sna_3lpm18gb41_u_4_mfr340"))