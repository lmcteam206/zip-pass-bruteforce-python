import time,datetime,random,_random,string,itertools
def generate_passwords(output_file='passwords.txt', max_length=5):
    with open(output_file, 'w') as outfile:
        for length in range(1, max_length + 1):
            for password_tuple in itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=length):
                password = ''.join(password_tuple)
                outfile.write(password + '\n')


generate_passwords(max_length=6)