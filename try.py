#check user input with try-except code
def askint():
    try:
        val = int(raw_input('Give me an integer number'))
    except:
        print 'please try again'
        askint()


askint()