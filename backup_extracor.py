from iosbackup import iOSbackup 
b = iOSbackup(udid="00008101-001C712C34E8001Es", cleartextpassword="")
files = b.getBackupFilesList()
for f in files:
    if f['relativePath'].lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov')):
        file = b.getFileDecryptedData(fileNameHash=f['fileID'],manifestData=f['file'])
        if file[0]['created'].day == 29 and file[0]['created'].month == 9 and file[0]['created'].year == 2022:
            b.getFileDecryptedCopy(relativePath=f['relativePath'], targetFolder='C:\\Users\\ricca\\Desktop\\new', targetName='')