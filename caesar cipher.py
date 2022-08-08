t = str(input("1 - Decode | 2 - Encode : "))
cipher = list((str(input("enter the cipher: ")).lower()))
cc = cipher.copy()
alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
print("\n")

if t == "1":
    for key in range(26):
        for i in range(len(cc)):
            if cc[i] == " ":
                cipher[i] = " "
            else:
                s = alf.index(cc[i]) - key
                if s >= len(alf):
                    s -= len(alf)
                    cipher[i] = alf[s]
                else:
                    cipher[i] = alf[s]
        print("".join(cipher),"| key = ",key,"\n")

elif t == "2":
    key = int(input("enter the key: "))
    for i in range(len(cc)):
        if cc[i] == " ":
            cipher[i] = " "
        else:
            s = alf.index(cc[i]) + key
            if s >= len(alf):
                s -= len(alf)
                cipher[i] = alf[s]
            else:
                cipher[i] = alf[s]
    print("".join(cipher))
