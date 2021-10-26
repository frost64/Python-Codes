name=raw_input("Enter Your Name!")
for i in range(0,len(name)):
    if i%2==0:
        c=name[i].upper()
        print c
    else:
        s=name[i].lower()
        print s