import zipfile
def read_zip_file(zipfilepath):
    z = zipfile.ZipFile(zipfilepath, 'r')
    for filename in z.namelist():
        print 'File: ', filename,
        bytes = z.read(filename)
        print 'has ', len(bytes), 'bytes'

if __name__ == '__main__':
    read_zip_file('/home/yunfeng/git.zip')
