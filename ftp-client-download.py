from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('files') #replace with your directory
print ("Permissions  No. Owner	Type	Size	Date	 Time  Filename")
ftp.retrlines('LIST')

def downloadFile():
 filename = raw_input('Enter filename to download: ')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

downloadFile()