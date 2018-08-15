import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    if type(txt)!=str:
        raise TypeError, "Only strings can be capitalized"
    else:
        return(txt.upper())


## reverse all characters in string
def reverse(txt):
    if type(txt)!=str:
        raise TypeError, "Only strings can be reversed"
    else:
        txtrev=[]
        for i in txt:
            txtrev.insert(0,i)
        return("".join(txtrev))

## reverse word order in string
def reversewords(txt):
    if type(txt)!=str:
        raise TypeError, "Only strings can be reversed"
    else:
        wordrev=[]
        for i in txt.split():
            wordrev.insert(0,i)
        return (" ".join(wordrev))

## reverses letters in each word
def reversewordletters(txt):
    if type(txt)!=str:
        raise TypeError, "Only strings can be reversed"
    else:
        return(reverse(reversewords(txt)))

## change text to piglatin.. google it! 
def piglatin(txt):
    if type(txt)!=str:
        raise TypeError, "Only strings can speak Pig Latin"
    else:
        vowel=["a","e","i","o","u"]
        piglfull=[]
        for frag in txt.split():
            pigl=[]
            count=0
            for i in frag:
                if not i in vowel:
                    pigl.extend(i)
                    count+=1
                else:
                    pigl.insert(0,frag[count:])
                    pigl.append("ay")
                    "".join(pigl)
                    break
            piglfull.append("".join(pigl))
        return(" ".join(piglfull))

## note: not to do the work twice:
## except TypeError as err:
## print err


## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

for i in string_list:
    try:
        print(reverse(i))
    except TypeError:
        print "Type Error: the input should be a string"
