def anagram_number(number):
    str1 = f"{number}"    
    str2 = str1[::-1] 
    if (str1 == str2):
        return True  
    else:
        return False

def roman_to_int(s):
    numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    n = 0
    last_value = 0
    for value in (numerals[c] for c in reversed(s.upper())):
        n += (value, -value)[value < last_value]
        last_value = value
    return n