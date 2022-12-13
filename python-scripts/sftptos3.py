import pysftp
import boto3

host = 's-c8cd657eb16040d48.server.transfer.ap-northeast-1.amazonaws.com'
port = 22
username = 'afroz'
privateKeyFilePath = 'id_rsa'

try:
  conn = pysftp.Connection(host=host,port=port,username=username, private_key=privateKeyFilePath)
  print("connection established successfully")
except:
  print('failed to establish connection to targeted server')
conn.get("/a.f.r.o.z/afroz/new_file.txt", preserve_mtime=True)
print("file downloaded to local machine successfully")

s3_client = boto3.client('s3')
file_name = 'new_file.txt'
bucket_name = 'from-sftp-data'
object_name= file_name

try:
    s3_client.upload_file(file_name,bucket_name,object_name)
    print('file:',file_name,' uploaded on bucket:',bucket_name,' successfully')
except Exception as e:
    print("failed to upload specified file")
    print(e)