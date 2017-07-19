# 
# Python FTP access
# 

import ftplib

FTP_SERVER_URL = 'speedtest.tele2.net'
DOWNLOAD_DIR_PATH = './'
DOWNLOAD_FILE_NAME = '100KB.zip'

def ftp_file_download(path, username, email):
    ftp_client = ftplib.FTP(path, username, email)
    # list the files in the download directory
    ftp_client.cwd(DOWNLOAD_DIR_PATH)
    print("File list as %s: " %path)
    files = ftp_client.dir()
    print(files)
    # download a file
    file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
    ftp_cmd = 'RETR {}'.format(DOWNLOAD_FILE_NAME)
    ftp_client.retrbinary(ftp_cmd, file_handler.write)
    file_handler.close()
    ftp_client.quit()

if __name__ == '__main__':
    ftp_file_download(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')