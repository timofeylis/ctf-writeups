# our encoded string here is below. we're supposed to decode it, and the long
# one liner that's at the beginning is the function that we have to reverse engineer
# it creates the weird chinese text by 
# 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽

flag = "picoCTF{test123}"
print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
nflag = [None] * len(enc)*2

for i in range(0, len(nflag)):
    if (i % 2) == 0:
        nflag[i] = chr(ord(enc[i//2]) // 256)
    else:
        nflag[i] = chr(ord(enc[i//2]) % 256)
print(''.join(nflag))

# for i in range(0,len(enc)):
#    nflag[i]

# chr(ord(enc[i]) >> 8)
