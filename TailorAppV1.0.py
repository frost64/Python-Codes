from tkinter import *
import time
import os

window=Tk()
window.geometry("920x750")
#####################################


def data():
    time.sleep(0.5)
    message.delete(0.0,'end')
    
    name=e2.get()
    contact=e3.get()
    serial=contact[-4:]
    
    length=e4.get()
    sleeves=e5.get()
    shoulder=e6.get()
    collar=e7.get()
    chest=e8.get()
    widy=e9.get()
    pants=e10.get()
    pensa=e11.get()
    baazudet=e12.get()
    
    plate=varplate.get()
    if plate==1:
        plate="Yes"
    else:
        plate="No"
    
    chkpatti=varchk.get()
    if chkpatti==1:
        chkpatti="Yes"
    else:
        chkpatti="No"
        
    cllrtype=varcollar.get()
    if cllrtype==1:
        cllrtype="Ban"
    else:
        cllrtype="Collar"
        
    daman=vardaman.get()
    if daman==1:
        daman="Gol"
    else:
        daman="Chorus"
        
    sidepkt=varside.get()
    if sidepkt==1:
        sidepkt="Single"
    else:
        sidepkt="Double"
        
    frntpkt=varfront.get()
    if frntpkt==1:
        frntpkt="Yes"
    else:
        frntpkt="No"
        
    extradt=extra.get(0.0,'end')
    ######################
    data="Customer's Name: "+name+"\nContact Number: "+contact+"\nSerial Number: "+str(serial)+"\n"+"\nMEASUREMENTS:\n"+"\nLength: "+length+"\nSleeves: "+sleeves+"\nShoulder: "+shoulder+"\nCollar: "+collar+"\nChest: "+chest+"\nWidy: "+widy+"\nPants: "+pants+"\nPensa: "+pensa+"\nBaazu Details: "+baazudet+"\nPlate: "+plate+"\nChakpatti Button: "+chkpatti+"\nCollar Type: "+cllrtype+"\nDaman: "+daman+"\nSide Pockets: "+sidepkt+"\nFront Pocket:"+frntpkt+"\n\nExtra Information: "+extradt+"\n"
    ######################
    try:
        os.makedirs('Register')
    except:
        pass
    current=os.getcwd()
    direct=current+"/Register"
    outpath=contact+".txt"
    file_name=os.path.join(direct,outpath)
    with open(file_name,'w') as fw:
        for i in data:
            fw.write(i)
##############################
    msg=" Data Saved Successfully! "
    message.insert(0.0,msg)
###################################

#############################
save=Button(window,text="Save Data!",bg="Olive",fg="White",command=data)
save.grid(row=23,columnspan=3)
############################
# window.geometry('480x720')

window.title("Tailor's App")
#labels
l1=Label(window,text="Universal Tailor's!\n---------------")
l1.grid(row=0,column=1)

l2=Label(window,text="Customer's Information:")
l2.grid(row=1,column=1)

l3=Label(window,text="Customer's Name:")
l3.grid(row=2,column=0)

l4=Label(window,text="Contact Number:")
l4.grid(row=3,column=0)

l5=Label(window,text="Measurements:")
l5.grid(row=4,column=1)

l6=Label(window,text="Length:")
l6.grid(row=5,column=0)

l7=Label(window,text="Sleeves:")
l7.grid(row=6,column=0)

l8=Label(window,text="Shoulder:")
l8.grid(row=7,column=0)

l9=Label(window,text="Collar:")
l9.grid(row=8,column=0)

l10=Label(window,text="Chest:")
l10.grid(row=9,column=0)

l11=Label(window,text="Widy:")
l11.grid(row=10,column=0)

l12=Label(window,text="Pants:")
l12.grid(row=11,column=0)

l13=Label(window,text="Pensa:")
l13.grid(row=12,column=0)

l14=Label(window,text="Baazu Details:")
l14.grid(row=13,column=0)

l15=Label(window,text="Plate:")
l15.grid(row=14,column=0)

l16=Label(window,text="Chakpatti Button:")
l16.grid(row=15,column=0)

l17=Label(window,text="Collar Type:")
l17.grid(row=16,column=0)

l18=Label(window,text="Daman:")
l18.grid(row=17,column=0)

l19=Label(window,text="Side Pockets:")
l19.grid(row=18,column=0)

l20=Label(window,text="Front Pockets:")
l20.grid(row=19,column=0)

l21=Label(window,text="Extra Information:")
l21.grid(row=20,column=0)

l22=Label(window,text="Black Hawk Creations!")
l22.grid(row=26,column=3)

#labels' space


name_text=StringVar()
e2=Entry(window,textvariable=name_text)
e2.grid(row=2,column=2)

contact_text=StringVar()
e3=Entry(window,textvariable=contact_text)
e3.grid(row=3,column=2)


length_text=StringVar()
e4=Entry(window,textvariable=length_text)
e4.grid(row=5,column=2)

sleeves_text=StringVar()
e5=Entry(window,textvariable=sleeves_text)
e5.grid(row=6,column=2)

shoulder_text=StringVar()
e6=Entry(window,textvariable=shoulder_text)
e6.grid(row=7,column=2)

collor_text=StringVar()
e7=Entry(window,textvariable=collor_text)
e7.grid(row=8,column=2)

chest_text=StringVar()
e8=Entry(window,textvariable=chest_text)
e8.grid(row=9,column=2)

widy_text=StringVar()
e9=Entry(window,textvariable=widy_text)
e9.grid(row=10,column=2)

pants_text=StringVar()
e10=Entry(window,textvariable=pants_text)
e10.grid(row=11,column=2)

pensa_text=StringVar()
e11=Entry(window,textvariable=pensa_text)
e11.grid(row=12,column=2)

baazu_text=StringVar()
e12=Entry(window,textvariable=baazu_text)
e12.grid(row=13,column=2)

varplate=IntVar()
plate=Radiobutton(window,text="Yes",variable=varplate,value=1)
plate2=Radiobutton(window,text="No",variable=varplate,value=2)
plate.grid(row=14,column=2,sticky=W)
plate2.grid(row=14,column=2,sticky=E)


varchk=IntVar()
patti=Radiobutton(window,text="Yes",variable=varchk,value=1)
patti2=Radiobutton(window,text="No",variable=varchk,value=2)
patti.grid(row=15,column=2,sticky=W)
patti2.grid(row=15,column=2,sticky=E)

varcollar=IntVar()
collar=Radiobutton(window,text="Ban",variable=varcollar,value=1)
collar2=Radiobutton(window,text="Collar",variable=varcollar,value=2)
collar.grid(row=16,column=2,sticky=W)
collar2.grid(row=16,column=2,sticky=E)

vardaman=IntVar()
daman=Radiobutton(window,text="Gol",variable=vardaman,value=1)
daman2=Radiobutton(window,text="Chorus",variable=vardaman,value=2)
daman.grid(row=17,column=2,sticky=W)
daman2.grid(row=17,column=2,sticky=E)

varside=IntVar()
side=Radiobutton(window,text="Single",variable=varside,value=1)
side2=Radiobutton(window,text="Double",variable=varside,value=2)
side.grid(row=18,column=2,sticky=W)
side2.grid(row=18,column=2,sticky=E)

varfront=IntVar()
front=Radiobutton(window,text="Yes",variable=varfront,value=1)
front2=Radiobutton(window,text="No",variable=varfront,value=2)
front.grid(row=19,column=2,sticky=W)
front2.grid(row=19,column=2,sticky=E)

extra=Text(window,width=50,height=5,wrap=WORD)
extra.grid(row=21,columnspan=5,sticky=W)

lg=Label(window,text="--------------------")
lg.grid(row=22,columnspan=3)

lg3=Label(window,text="--------------------")
lg3.grid(row=24,columnspan=3)

message=Text(window,width=50,height=1,wrap=WORD)
message.grid(row=25,columnspan=3)
###################################
# k0=Label(window,text="|")
# k0.grid(row=0,column=3)

for i in range(26):
    w="k"+str(i)
    if i!=21:
        w=Label(window,text="          .          ")
        w.grid(row=i,column=3)
    elif i==21:
        w=Label(window,text="          .          \n          .          \n          .          \n          .          \n          .          ")
        w.grid(row=i,column=3)

###################################

#############################
def data():
    message2.delete(0.0,'end')
    try:    
        contact2=g3.get()
        name=str(contact2)+".txt"
        direct="Register"
        fname=os.path.join(direct,name)
        with open(fname,'r') as f:
            message2.insert(0.0,f.read())
    except Exception:
        message2.insert(0.0,"File Not Found!")
# #############################
l5=Label(window,text="Customer's Details:\n--------------------")
l5.grid(row=0,column=5)

l7=Label(window,text="Enter Contact Number:")
l7.grid(row=1,column=4)

contact_text=StringVar()
g3=Entry(window,textvariable=contact_text)
g3.grid(row=1,column=6)

lk3=Label(window,text="-------------------------")
lk3.grid(row=2,column=5)

save=Button(window,text="Check Details!",bg="Olive",fg="White",command=data)
save.grid(row=3,column=5)

lk4=Label(window,text="-------------------------")
lk4.grid(row=4,column=5)

message2=Text(window,width=50,height=35,wrap=WORD)
message2.grid(row=5,rowspan=20,columnspan=10,sticky=E)
###########################

###################################

#submit button       
window.mainloop()
f=raw_input("Press Enter to Exit")