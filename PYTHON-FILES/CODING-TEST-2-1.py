import string

def first_half (s):
   ret_value=''

   char_num = len(s)

   if char_num %2 == 0:
       first_half_length = char_num/2
   else :
       first_half_length = ((char_num/2)+1)

   return (s[ 0 : first_half_length]) 

imp = raw_input('Enter your string here: ')
print first_half(imp)

