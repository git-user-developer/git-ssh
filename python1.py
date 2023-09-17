import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="123456789"
symbols="!@#$%^&*()"
combine=lower+upper+numbers+symbols
length=10
password="".join(random.sample(combine,length))
print("the generated password is :-",password)