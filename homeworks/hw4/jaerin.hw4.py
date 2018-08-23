def shortersort(listinput):
    output=[]
    for i in range(len(listinput)):
        output.append(min(listinput))
        listinput.remove(min(listinput))
    return(output)

def longersort(listinput):
    changes=True
    while changes==True:
        changes=False
        for i in range(len(listinput)-1):
            for j in range(len(listinput)-1):
                if listinput[i]>listinput[j+1]:
                    listinput.insert(j+1,listinput[i])
                    listinput.remove(listinput[i])
                    changes=True
                    break
    return(listinput)
