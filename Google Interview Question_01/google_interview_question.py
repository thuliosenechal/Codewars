'''
INTRODUCTION:

If I give you a name of a city as a string, I want you to return a 
string that shows how many times each letter shows up in the string 
by using an asterisk *

SEE TEST CASE!

As you can see for Chicago, in the return string, I only show the 
letter "c" once even though there are 2 "c" in Chicago (regardless 
of upper or lowercase).

I show 2 asteriks since there are 2 "c" in Chicago.

In the return string there are no spaces between the letters, asteriks,
 and commas.

"Chicago"  =>  "c:**,h:*,i:*,a:*,g:*,o:*"
Note that the return string contains the characters in order of first 
appearence in the original string.

'''

def get_strings(city):
    string = city.lower()
    new_string = ""
    
    for letter in string:
        if letter in new_string or not letter.isalpha():
            continue
        else:
            new_string += letter + ':' + ('*' * string.count(letter)) + ','

    return new_string.rstrip(',')


if __name__ == '__main__':
    print(get_strings('Las Vegas'))
