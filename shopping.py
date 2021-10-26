x=raw_input("Do you want to add item?\nEnter y for yes or Press Enter Key to continue")
price_dic={"شساشعيساش":30,"Prince":20,"Coke":10}
if x.upper()=='Y':
    i=raw_input("Enter Item's Name:")
    p=input("Enter Item's Price:")
    price_dic[i]=p
print "Type \"done\" and press Enter when you're done!"
qw=[]
while "done" not in qw:
    i=raw_input("Enter Item's Name:")
    qw.append(i)
q=qw[:len(qw)-1]

from datetime import datetime
def time(x):
    hours=int(x[:2])
    if hours<12:
        print x,"AM"
    elif hours==12:
        print x,"PM"
    elif hours>12:
        print str(int(hours)-12)+x[2:],"PM"



def object_price(x):
    result=[]
    for obj in x:
        if obj in price_dic:
            data=(obj,float(price_dic[obj]))
            result.append(data)
        else:
            print obj,'is not in the price list!'
    return result



def total_price(ls):
    total=0.0
    result=[]
    for name,price in ls:
        total+=price
    data=('Total',total)
    result.append(data)
    return result


def balance(ls,total):
    result=[]
    blnc=total-ls[0][1]
    data=("Balance",blnc)
    result.append(data)
    return result

amount_paid=input("Enter Paid Amount!\t")
priceout=object_price(q)
totalout=total_price(priceout)
balanceout=balance(totalout,amount_paid)

def final(price,total,balance):
    name=raw_input("Operator's Name:\t")
    print '\n'
    print 'Khayat Dana Al-Fareej'.center(114)
    for k,v in price:
        print k,'\t\t\t','Rs',v,'/-'
    print "\nAmount Paid\t\t","Rs",amount_paid,"/-"
    for k,v in total:
        print k,'\t\t\t','Rs',v,'/-'
    for k,v in balance:
        print k,'\t\t','Rs',v,'/-'
    print '\nOperator\t\t',name
    clock=datetime.now()
    tim=str(clock)
    date=tim[0:10]
    print 'Time\t\t\t',
    time(tim[11:19])
    print 'Date\t\t\t',date
final(priceout,totalout,balanceout)
print "Thanks for Shopping here! Have a nice day!".center(114)
feedback=raw_input("Give your Feedback here!")