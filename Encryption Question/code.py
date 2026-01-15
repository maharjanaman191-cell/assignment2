#Encryption function
def encrypt_char(shift1, shift2):
    l1 = "abcdefghijklm"
    l2 = "nopqrstuvwxyz"
    u1 = "ABCDEFGHIJKLM"
    u2 = "NOPQRSTUVWXYZ"
    Evalue = ""

    with open("raw_text.txt", "r") as file:
        txt = file.read()

    for c in txt:
        if c.islower():
            if c in l1:
                idx = l1.index(c)
                new_idx = (idx + (shift1 * shift2)) % 13
                Evalue += l1[new_idx]
            elif c in l2:
                idx = l2.index(c)
                new_idx = (idx - (shift1 + shift2)) % 13
                Evalue += l2[new_idx]
        elif c.isupper():
            if c in u1:
                idx = u1.index(c)
                new_idx = (idx - shift1) % 13
                Evalue += u1[new_idx]
            elif c in u2:
                idx = u2.index(c)
                new_idx = (idx + (shift2 ** 2)) % 13
                Evalue += u2[new_idx]
        else:
            Evalue += c

    with open("encrypted.txt", "w") as file:
        file.write(Evalue)

