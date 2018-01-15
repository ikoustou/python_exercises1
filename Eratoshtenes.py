
def Eratosthenes(n):
    current = 2
    array = [True for x in xrange(1, n + 1)]

    def delete_mult(i,lim):
        m = 2
        while i*m<=lim:
            array[i*m-1] = False
            m+=1

    def find_next_current(j):
        for i in xrange(j+1,n+1):
            if array[i-1] == True:
                number = i
                break
        else:
            number = n
        print number
        return number

    def extract_prime():
        for index, item in enumerate(array):
            if item == True:
                yield index+1


    while current<n:
        delete_mult(current,n)
        current = find_next_current(current)
        print array

    print 'the prime numbers are :'
    for x in extract_prime():
        print x

def ask_number(): #ask for an interger
    try:
        n = int(raw_input("Give me an integer lower than 1000 : ") )
    except:
        print "this is not a valid integer, try again "
        ask_number()
    return n

num = ask_number()
Eratosthenes(num)
