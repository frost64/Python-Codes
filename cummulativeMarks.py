## IMPORTS GO HERE
import os
## END OF IMPORTS


### YOUR CODE FOR cumulative_marks() FUNCTION GOES HERE ###
def cumulative_marks(x=None):
    if x==None:
        return None
    result=[]
    for j in x:
        tup=()
        num=[]
        for i in j:
            if i != 'A' and i != None:
                num.append(i)
        data=tuple(num)
        roll=data[0][1:3]+data[0][0].upper()+'-'+data[0][3:]
        name=data[1]
        marks=data[2:]
        x=0
        for i in marks:
            x+=i # x+=float(i) if you want to get marks in float
        tup+=(roll,name,x)
        result.append(tup)
    return result
cumulative_marks()
#### End OF MARKER

if __name__ == '__main__':
    results = [
        ('p101111', 'Muhammad Amin', 64, 78.5, 89, 25, 99),
        ('p101112', 'Tehseen Khan', 14, 28.5, 83, 76),
        ('p101113', 'Tauqeer Ali', 87, None, 1.6)
    ]

#    print cumulative_marks(results)
    # output: [('10P-1111', 'Muhammad Amin', 355.5), ('10P-1112', 'Tehseen Khan', 201.5), ('10P-1113', 'Tauqeer Ali', 88.6)]

