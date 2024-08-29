import random
import string
def gen_password():
    password=string.ascii_letters+string.digits+string.punctuation
    return ''.join(random.choice(password) for i in range(8) )
new_password=gen_password()
print(new_password)