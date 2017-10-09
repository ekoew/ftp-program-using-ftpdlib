from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('files')

def uploadFile():
 filename = raw_input('Enter filename to upload: ')
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

uploadFile()