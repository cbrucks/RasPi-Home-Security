import urllib
import urllib2
import re

class SMS:

    def __init__(self):
        pass

    def _get_code(self):
        url = 'http://www.onlinetextmessage.com'
        req = urllib2.Request(url, '')
        response = urllib2.urlopen(req)
        html = response.read()
        code = re.search('(?<=\<input type="HIDDEN" name="code" value=")[0-9]+(?=">)', html)
        if code == '':
            raise Exception("Failed to find the code for sms")
            exit
        return code

    def _get_provider(self, phone_number):
        url = 'http://www.txt2day.com/lookup.php'
        data = {'action' : 'lookup',
                'pre' : number[0:3],
                'ex' : number[3:6],
                'myButton' : 'Find Provider'}

        data = urllib.urlencode(data)  ##provider checker
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        html = response.read()

        if 'Telus' in html:
            prov = '192'
        if 'Bell' in html:
            prov = '48'
        if 'Rogers' in html:
            prov = '162'
        if 'Sprint' in html:
            prov = '175'
        if 'T-Mobile' in html:
            prov = '182'
        if 'Verizon' in html:
            prov = '203'
        if 'Virgin Mobile' in html:
            prov = '205'
        if 'Att' in html:
            prov = '41'

        if prov == '':
            raise Exception("Failed To Identify Provider")
            exit
        
        return prov

        
    def send_sms(self, phone_number, from_addr, subject, message
        url = 'http://www.onlinetextmessage.com/send.php'
        data = {'code' : self._get_code(),
                'number' : phone_number,
                'from' : from_addr,
                'remember' : 'n',
                'subject' : subject,
                'carrier' : self._get_provider(phone_number),
                'quicktext' : '',
                'message' : message,
                's' : 'Send Message'}
        data = urllib.urlencode(data)  ##text sender
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read() 
