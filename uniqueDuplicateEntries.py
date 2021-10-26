## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR uniqueEntries GOES HERE ####

def uniqueEntries(x):
    full=[]
    unique=[]
    duplicate=[]
    for elements in x:
        full.append(elements)
    for i in full:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.append(i)
    return unique,duplicate

#### End OF MARKER ----uniqueEntries



if __name__ == '__main__':
    uniqueEntries([12,24,35,24,88,120,155,88,120,155])
