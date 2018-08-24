import imp

# Change path as needed
meetup=imp.load_source('mu','/home/jaerin/code/meetup.py')
api=meetup.client

# Any group cotaining 'music' for its description.
# It is weird, because it contains something like
# "Metro East Friends". But let's assume that they are
# devoted to music anyway.

musicgroups=api.GetFindGroups({"text":"music"})

def mostPopular(groups):
# Find list of how many members are for each group
    memlist=[i.members for i in groups]
# Find where the most popular group is in the list,
# and return the group as a MeetupObject.
    return(groups[memlist.index(max(memlist))])
# 1.'Sip, Socialize, and Get Creative in STL!' is the most
# popular group with 5323 members, as of now

mmp=mostPopular(musicgroups)
print mmp.name,'\n' ,mmp.members

# 2. First, GetIDs fundtion returns IDs of group members,
# given a group meetup object as an input

def getIDs(group):
    users=api.GetMembers({"group_urlname":group.urlname})
    output=[]
    return [i["id"] for i in users.__dict__["results"]]

# getUserGroups takes a list of ID as an input,
# and returns a dictionary of lists containing each member's groups
# If this function takes too long, consider something like
# IDlist[0:10] as input

def getUserGroups(IDlist):
    import time
    output={}
    itr=0
    itj=0
    for i in IDlist:
        ugroups=api.GetGroups({"member_id":i})
        ugroupurl=[]
        for j in ugroups.__dict__["results"]:
            ugroupurl.append(j["urlname"])
            time.sleep(10)
        output[i]=ugroupurl
        time.sleep(10)
    return(output)

# getActiveUser calculates the number of groups each user participates in
# and returns a member's ID with highest number of groups

def getActiveUser(IDlist):
    usergroups=getUserGroups(IDlist)
    ngroups={}
    for i in usergroups:
        ngroups[i]=len(usergroups[i])
    return(max(ngroups, key=ngroups.get))

# The functions above, when connected, completes the problem #2

mostActiveUser=getActiveUser(getIDs(mostPopular(musicgroups)))

# 3. We already defined the functions above. We can just run them
# to answer the question #3.

mostPopular(api.GetFindGroups({'member_id':mostActiveUser})).name
