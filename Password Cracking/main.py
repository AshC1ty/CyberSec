import hashlib

def crackHash(inputPass):
    try:
        passFile=open("wordlist.txt","r") #wordlist is the file which contains common passwords
    except:
        print("No file found")
    
    for password in passFile:
        encPass = password.encode("utf-8")
        digest=hashlib.md5(encPass.strip()).hexdigest()

        if digest == inputPass:
            print("Password found: "+password)


crackHash("A hash that you wanna try finding the password for")