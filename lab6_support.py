# Chat Encryption Helper - ch9_crypto_chat.py
import os, base64, json
#from Crypto.Cipher import PKCS1_OAEP, AES
#from Crypto.PublicKey import RSA, ECC
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
 
# encryption method used by all calls
def encrypt(message, usePKI, useDH, dhSecret):
    em =cipherEncrypt(message, dhSecret, 1)
    return em
 
# decryption method used by all calls
def decrypt(message, usePKI, useDH, dhSecret):
    dm=cipherEncrypt(message, dhSecret, -1)
    return dm
 
# decrypt using RSA (for future reference)
#def decrypt_rsa(ciphertext):
#    return ciphertext
 
# encrypt using RSA (for future reference)
#def encrypt_rsa(message):
#    return message
 
# check client commands (for future reference)
def check_client_command(data):
    return 1
 
# check server commands (for future reference)
def check_server_command(data):
    return 1
    
def reversed_string(a_string):
    return a_string[::-1]

def cipherEncrypt(inputText, n, d):
# custom encryption from Lab 3
        #this is where we will implement encryption
    print("Encrypting...")
    # 1: reverse input text
    encryptedText = inputText[::-1] # reverse text using splicing. 
    shiftedText = ""
    start = 34
    end = 126
    if (d == 1): # right shift 
        for char in encryptedText:
                shiftedchar =  chr(((ord(char) - start) + n) % (end - start + 1) + start)
                shiftedText += shiftedchar
    if (d == -1):# shift left 
         for char in encryptedText:
            shiftedchar = chr(((ord(char) - start) - n) % (end - start + 1) + start)
            shiftedText += shiftedchar
    return shiftedText
   