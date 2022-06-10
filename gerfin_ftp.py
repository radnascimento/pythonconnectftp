import ftplib
import uuid


print('start')

# Open the FTP connection

ftp = ftplib.FTP('ip address here')


ftp.login(user='username here', passwd = 'password here')


ftp.cwd('your files path')


filenames = ftp.nlst()


for filename in filenames:
	
	print(filename)
	
	#create a local file

	l = open('C:\\Temp\\Gerfin\\Backup\\' + str(uuid.uuid4()) + '.db','wb')

	#write the binary in the file created before
	ftp.retrbinary('RETR ' + filename, l.write,1024)

	l.close()

ftp.quit()

print('finish')
