s = 'Hello Mr. Jenkins ! How are you today?'

def up_low(s1):
    d={"upper":0, "lower":0}
    for c in s1:
        if c.isupper():
            d["upper"] +=1
        elif c.islower():
            d["lower"] +=1
        else:
            pass
    print 'original string : ', s1
    print 'Number of Uppercase letters: ', d["upper"]
    print 'Number of lowercase letters: ', d["lower"]

up_low(s)