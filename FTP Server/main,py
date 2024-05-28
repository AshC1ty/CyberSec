import ftplib
def anonLogin(hostname):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login("anonymous")
        print('\n [+] ' + str(hostname) + ' FTP login anonymously done')
        ftp.quit
        return True
    except Exception:
        print('\n' + str(hostname) + ' FTP login anonymously failed')
        return False
    
anonLogin('IP address of a public ftp server that accepts anonymous login')