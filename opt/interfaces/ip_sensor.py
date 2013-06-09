import urllib
import re
import socket


def getExternalIP():
    ip_website = urllib.urlopen("http://www.canyouseeme.org/")
    html = ip_website.read()
    ip_website.close()
    matches = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html)
    return matches.group(0)

def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip


if __name__=="__main__":
    print "External IP: %s" % getExternalIP()
    print "Local IP: %s" % getLocalIP()
