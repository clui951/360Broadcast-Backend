### Sanitize Inputs ###
import cgi


def sanitize_num(num):
	if not isValidNumber(num):
		return None
	else:
		num = translateNumber(num)
		num.replace("-","")
		num = "+1" + num
		return num



def sanitize_msg(msg):
	return msg




def isValidNumber(phone_number):
    for i,c in enumerate(phone_number):
        if i in [3,7]:
            if c != '-':
            	return False
        elif not c.isalnum():
        	return False
    return True

def translateNumber(phone_number):
	s=""
	for char in phone_number:
		if char is '1':
			x1='1'
			s= s + x1
		elif char is '-':
			x2='-'
			s= s + x2
		elif char in 'ABCabc':
			x3='2'
			s= s + x3
	return s
