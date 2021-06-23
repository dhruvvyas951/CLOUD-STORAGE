import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '4ga3L0t7YTgAAAAAAAAAASqXDYTgnRhL-ndRZiLB7zd3uRK-DoPytnRzuWWLPfA0'
    transfer_data = TransferData(access_token)
    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the file path to upload to dropbox: ')
    transfer_data.upload_file(file_from, file_to)
    print('File has been moved!')

main()