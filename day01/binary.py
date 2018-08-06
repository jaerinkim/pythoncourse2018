def binarize(dec):
    binr=[]
    rmd=dec
    while rmd!=0:
        binr.insert(0,rmd%2)
        rmd=rmd/2
    print("".join(str(i) for i in binr))

binarize(50)

def int_to_base(num,base):
    output=[]
    rmd=num
    while rmd!=0:
        output.insert(0,rmd%base)
        rmd=rmd/base
    print("".join(str(i) for i in output))

int_to_base(50,2)
int_to_base(50,5)

def flexibase_add(str1, str2, base1, base2):
    num1=0
    num2=0
    for i in range(1,len(str(str1))+1):
        num1+=base1**(i-1)*int(str(str1)[-i])
    for i in range(1,len(str(str2))+1):
        num2+=base2**(i-1)*int(str(str2)[-i])
    print(num1+num2)

flexibase_add(10, 20, 2, 5)

def flexibase_multiply(str1, str2, base1, base2):
    num1=0
    num2=0
    for i in range(1,len(str(str1))+1):
        num1+=base1**(i-1)*int(str(str1)[-i])
    for i in range(1,len(str(str2))+1):
        num2+=base2**(i-1)*int(str(str2)[-i])
    print(num1*num2)
flexibase_multiply(10,20,2,5)

def romanify(num):
    output=[]
    roman=["I","V","X","L","C","D"]
    for i in range(1,len(str(num))+1):
        curdig=int(str(num)[-i])
            if curdig==9:
                output.insert(0,"".join([roman[i*2-1],roman[i*2+1]])
            else:
                romdig=str(curdig)*roman[i*2-1]
                    if curdig>4:
                        romdig=romdig[-i:]
                        romdig.insert(0,roman[i*2])
                    elif curdig==4:
                        romdig="".join[roman[i*2-1],roman[i*2]]
                 output.insert(0,romdig)
    print(output)

romanify(32)
