# Sorter 1
def shortersort(listinput):
#Copy listinput to temp. [:] put to disconnect their linkage
#while conducting .remove function, for preserving the original input
    temp=listinput[:]
    output=[]
    for i in range(len(temp)):
        output.append(min(temp))
#For each loop, the smallest element is filled to output,
        temp.remove(min(temp))
#and it is removed from temp, making the second smallest element
#on this loop to be the smallest one on the next loop
    return(output)

# Sorter 2
def longersort(listinput):
#Set condition to make the function recursive, until there are
#only two elements left for the current execution.
    if len(listinput)>2:
#Until then, temp[0] equals listinput[0], which is not sorted,
#while listinput[1:] is sorted by recursive 'longersort' function
        temp=[listinput[0]]+longersort(listinput[1:])
#Yet, if the length of listinput hits 2,
    else:
#we just need to figure out which of the two numbers is bigger,
#leaving no need for calling longersort function anymore.
        temp=listinput
#Then, the only element not sorted for each call is temp[0],
#and the for loop below determines where this element should go.
    for i,value in enumerate(temp[1:]):
#For each element smaller than temp[0], it will move to the right
#in the list.
        if listinput[0]>value:
#temp[0] is inserted to i+2, not i+1, because the loop is one
#element shorter than it should be at the end(note temp[1:]).
            temp.insert(i+2,temp[i])
            del temp[i]
    return(temp)

print shortersort(['a',5,1,3,'b'])
print longersort(['b',3,1,5,'a'])
test=['this',12,'is',3,'a',6,'test']
shortersort(test)==longersort(test)
