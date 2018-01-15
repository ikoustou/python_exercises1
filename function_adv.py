#---  Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list
def word_lengths(phrase):
    l_str = phrase.split()
    l_int = map(lambda word: len(word), l_str)
    return l_int

str1 = 'this is the first phrase'
str2 = 'Pou soun magka to xeimona?'

print word_lengths(str1)
print word_lengths(str2)
print
#--------   Use reduce to take a list of digits and return the number that they correspond t-------------------------
def digits_to_num(digits):
    return reduce(lambda a, b: a*10+b, digits)

digits = [3,4,5,0,1]
print digits_to_num(digits)
print
#--------Use filter to return the words from a list of words which start with a target letter.
str3 = 'hello my little hon! how are you today?'
str_l = str3.split()
def filter_words(word_list, letter):
    return filter(lambda str: str[0]==letter , word_list)

print filter_words(str_l, 'h')
print
#-----  Use zip and list comprehension to return a list of the same length
# where each value is the two strings from L1 and L2 concatenated together with connector between them
L1 = ['Artemis', 'Giorgos']
L2 = ['9', '5']
def concatenate(L1, L2, character):
    return [a+character+b for (a,b) in zip(L1,L2)]

print concatenate(L1, L2, '-')
print
#Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value.
# You may assume that a value will only appear once in the given list.
def list_to_dict(L1):
    """
    dict1={}
    for index,item in enumerate(L1):
        dict1.update({item:index})
    return dict1
    """
    return {item:index for index,item in enumerate(L1)}

print list_to_dict(L1)
print
#--Use enumerate and other skills from above to return the count of the number of items in the list
# whose value equals its index.
def count_match_index(L):
    c=0
    for i, value in enumerate(L):
        if i==value:
            c+=1
    return c
print count_match_index([0,2,2,1,5,5,6,10])
print