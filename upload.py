import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

         
        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BGTPJGKMnQ311wlpJ12cIIUTCbH2_GaMa6n23pHnkILf8K-f_Rm5k7F_yfXip9E2FAqN_H36toTEj324l4vtdCTo1f-oLextLRWv6s2u1JgDYmNppNCYfLnEoWb94-FepDT3ZVg'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the file path to transfer  - "))
    file_to = input("enter the full path to upload to dropbox - ")  

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()

print("made by om")
