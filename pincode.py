
def pincode(code):
    
    if code.isdigit()==True:
        if len(code)==4 or len(code)==6:
            return True
    return False

print(pincode('1234'))

print(pincode('12345'))
print(pincode('123456'))

print(pincode('123a'))
