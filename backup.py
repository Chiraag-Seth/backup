import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'r') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A5Et016RC1atYw_uOF9dMW8uAg_t3zZ1HyNTvCQFo0zhKe5btj8OpCc_GZHqzi_0dAz51IQ1Q28jbpbIhNsW2Af35jz9xSEeowpPGGUW_oqtOtGmOkdn8zCRvvoBunhbiMOWG4g'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/Backup-files-py/text.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()