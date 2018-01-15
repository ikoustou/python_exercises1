#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True


def end_other(a, b):
  len1=len(a)
  len2=len(b)

  new_a = a.lower()
  new_b = b.lower()
  if len1>len2:
    return new_a[len1-len2:]==new_b
  else:
    return new_b[len2-len1:]==new_a