from string import ascii_uppercase, ascii_lowercase, digits

def checker(charset, s):
    matched = [char for char in s if char in charset]
    if len(matched) > 0:
        return 1 # At least one exists
    else:
        return 0 # One doesn't exist

def has_upper(s):
    return checker(ascii_uppercase, s)

def has_lower(s):
    return checker(ascii_lowercase, s)

def has_num(s):
    return checker(digits, s)

def has_misc(s):
    return checker(r"""!@$%^&*()_-+={}[]|\,.></?~`"':;""", s)

def check_len(s):
    if len(s) > 10:
        return 1
    else:
        return 0

def eval_security(num):
    intified = int(num, 2)
    if intified >= 10:
        return 10
    else:
        return intified

def addr(s):
    if s == "0":
        return ""
    else:
        return s

def check_security(s):
    bin_num = ""
    bin_num += addr(str(has_upper(s)))
    bin_num += addr(str(has_lower(s)))
    bin_num += addr(str(has_num(s)))
    bin_num += addr(str(has_misc(s)))
    bin_num += addr(str(check_len(s)))
    print s + ": " + bin_num
    print "Security level: " + str(eval_security(bin_num)) 

if __name__ == '__main__':
    check_security("Hi")
    check_security("hi")
    check_security("Hi!")
    check_security("hi!")
    check_security("Hi123!")
    check_security("Hi123456789!")
    check_security("hiiiiiiiiiiiiiiiiiiiii")