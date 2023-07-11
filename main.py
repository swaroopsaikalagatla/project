from fastapi import FastAPI, File, UploadFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

connection_string=os.environ['CONNECTION_STRING']

container_name="swaroopc"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

@app.post("/uploadfile/")
def create_upload_file(uploadedFile: UploadFile):
    # Upload the created file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploadedFile.filename)
    blob_client.upload_blob(uploadedFile.file.read())
    return {"filename": uploadedFile.filename}