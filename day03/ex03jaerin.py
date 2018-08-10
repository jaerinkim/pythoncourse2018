## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    count=0
    try:
        print ("Your input: "+word)
    except TypeError:
        print ("This is not a string!")
    except ValueError:
        print ("Put in only one string")
    else:
        for i in range(len(word)):
            count+=word[i] in ["a","e","i","o","u"]
        return count
