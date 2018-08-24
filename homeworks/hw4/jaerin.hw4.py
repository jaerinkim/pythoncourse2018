def shortersort(listinput):
    temp=listinput[:]
    output=[]
    for i in range(len(temp)):
        output.append(min(temp))
        temp.remove(min(temp))
    return(output)

def longersort(listinput):
    if len(listinput)>2:
        temp=[listinput[0]]+longersort(listinput[1:])
    else:
        temp=listinput
    for i,value in enumerate(temp[1:]):
        if listinput[0]>value:
            temp.insert(i+2,temp[i])
            del temp[i]
    return(temp)
