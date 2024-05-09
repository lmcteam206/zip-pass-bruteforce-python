import os
from art import *
import subprocess
import time
import itertools
import random
import string
from colorama import Fore


print(Fore.RED)
tprint('Zip-Carcker-Tool')
print(Fore.BLUE)
print('''[+]- by Lmcteam206
[+]- this tool is for eductional propuses only
[+]- this tool is still demo''')
print(Fore.LIGHTRED_EX)
print('These are all the files in this folder now >>>')
print(Fore.GREEN )
print(os.system('dir'))
print(Fore.RESET)
#################################################################################################################################- zip extract section-
def extract_zip_with_password(zip_file, output_dir, password):
    # Modify this with the correct path to 7z.exe
    seven_zip_path = "C:\\Program Files\\7-Zip\\7z.exe"
    
    # Check if 7z.exe exists at the specified path
    if not os.path.exists(seven_zip_path):
        print("7z.exe not found at the specified path. Please provide the correct path.")
        return False
    
    # Command to execute 7z.exe with the appropriate parameters
    command = [seven_zip_path, 'x', '-p{}'.format(password), zip_file, '-o{}'.format(output_dir), '-y']
    
    # Execute the command
    try:
        result = subprocess.run(command, check=False)
        if result.returncode == 0:
            print("Extraction successful. Password is correct.")
            return True
        else:
            print("Extraction failed. Incorrect password.")
            return False
    except FileNotFoundError:
        print("7z.exe not found. Please make sure 7z.exe is installed and accessible.")
        return False


zip_file_var = input('Enter the zip file directory: ')
#################################################################################################################################



################################################################################################################################# - brute section-

def force(word, zip_file):
    if extract_zip_with_password(zip_file, 'C:/Users/lmcteam206/Desktop/brute_force_test/outs', word):
        return 'success'
    else:
        return 'failed'

def attempt(at_num, word):
    result = force(word, zip_file_var)
    print(Fore.GREEN + f'Attempt number [{at_num}]: --- {word} --- : [{result}]' + Fore.RESET)
    if result == 'success':
        print(Fore.RED + '-----------------------------------------------------------------------------------------------------')
        print(f'Password found: {word}')
        print('-----------------------------------------------------------------------------------------------------' + Fore.RESET)
        input('Enter ....')
        exit()

# Generate passwords dynamically
def generate_passwords(length=6, characters=string.ascii_letters + string.digits):
    for password in itertools.product(characters, repeat=length):
        yield ''.join(password)

# Adjust the password length as needed
password_length = 6

x = 0
for password in generate_passwords(password_length):
    x += 1
    attempt(x, password)

print("Password not found.")
