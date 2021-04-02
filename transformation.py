# our encoded string here is below. we're supposed to decode it, and the long
# one liner that's at the beginning is the function that we have to reverse engineer
# it creates the weird chinese text by iterating over the string and
# converting every even character to its unicode number equivalent * 256 (bit shift 8)
# and converting every odd character to its unicode number
# it then adds these two numbers together, and turns that back into a unicode character
# 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽

# example flag
flag = "picoCTF{test123}"
print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
nflag = [None] * len(enc)*2

# solution
for i in range(0, len(nflag)):
    if (i % 2) == 0:
        nflag[i] = chr(ord(enc[i//2]) // 256)
    else:
        nflag[i] = chr(ord(enc[i//2]) % 256)
print(''.join(nflag))