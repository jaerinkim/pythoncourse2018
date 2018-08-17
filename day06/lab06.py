import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

obamalines=''.join(obama)
## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]
findthe=re.compile(r"\Wthe\W") 
findThe=re.compile(r"\WThe\W")
for line in obama:
    if not findthe.search(line) or findThe.search(line):
        print line



# TODO: print lines that contain a word of any length starting with s and ending with e
stoe=re.compile(r"\W(s\w*)e\W")
for line in obama:
    if stoe.search(line):
        print line

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = raw_input("Please enter a date in the format MM.DD.YY: ")
altdate=re.split(r'\.',date)
print "Month: ",altdate[0],"\nDate: ",altdate[1],"\nYear: ",altdate[2]


