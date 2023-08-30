# Password generate using python programming

import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "{}[]#()*_%;"

ans = lower_case + upper_case + num + symbol

length = 16
password = "".join(random.sample(ans,length))
print("Your New Generated Password is ", password)