import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password 
    except:
        return

def main():
    zfile=zipfile.ZipFile("Any zip file")
    passFile = open("pswdlist.txt","r")
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print("password found: "+password)
            break

main()