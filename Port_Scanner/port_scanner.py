from socket import *
import optparse

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('Connection successful at %d'%tgtPort)
        connskt.close()
    except:
        print('Connection failed at %d'%tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve: %d"%tgtHost)
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n Scan result of %s: "%tgtName[0])
    except:
        print("\n Scan result of %s: "%tgtIP)
    
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning Port: %d"%tgtPort)
        conScan(tgtHost, int(tgtPort))

portScan('google.com',[80,443])