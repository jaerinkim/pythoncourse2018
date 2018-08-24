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

import matplotlib.pyplot as plt
import time
import random

# Defining a function drawing observations from a uniform distribution
def ranun(trials):
    return([random.uniform(-1,1) for i in range(trials)])
# Defining a function calculating time taken to run sort functions
def elapsed(trials):
    shtime=[]
    lntime=[]
    srtime=[]
    for i in range(trials):
# For each loop, ranun is called to create a list of size i
        tester=ranun(i)
# Time is recorded just before running the function
        ctime=time.time()
        shortersort(tester)
# The difference between time after running function and
# the recorded one is appended in the respective lists,
        shtime.append(time.time()-ctime)
        ctime=time.time()
# for longersort function,
        longersort(tester)
        lntime.append(time.time()-ctime)
        ctime=time.time()
# and the built-in sorted function.
        sorted(tester)
        srtime.append(time.time()-ctime)
    return([shtime,lntime,srtime])
# How much time do functions take for 600 trials?
timetaken=elapsed(600)
# Quite a while. Now we can plot the result.


# Plotting how efficient the built-in sort function is
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
# 'timetaken' is a list of lists, each representing time taken
# to perform shortersort, longersort, and sorted, respectively.
plt.plot(range(1,601),timetaken[0])
plt.plot(range(1,601),timetaken[1])
plt.plot(range(1,601),timetaken[2])
plt.legend(['shortersort', 'longersort','sorted'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time Elapsed (Seconds)")
plt.xlabel("Number of Elements in the List")
plt.title("How Inefficient It Is to Write Your Own Sort Function")
txt = """
Let's use 'sorted' function.
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot.pdf')
