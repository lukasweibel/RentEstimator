# cd model
# python save.py -c '***AZURE_STORAGE_CONNECTION_STRING***'

import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
from joblib import load

load_dotenv()

azure_connection_string = os.getenv("AZURE_CONNECTION_STRING")

# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli
# Erlaubnis auf eigenes Konto geben :-)

def save_model():
    try:
        print("Azure Blob Storage Python quickstart sample")

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

        # account_url = "https://mosazhaw.blob.core.windows.net"
        # default_credential = DefaultAzureCredential()
        # Create the BlobServiceClient object
        # blob_service_client = BlobServiceClient(account_url, credential=default_credential)

        exists = False
        containers = blob_service_client.list_containers(include_metadata=True)
        suffix = 0
        for container in containers:
            existingContainerName = container['name']
            print(existingContainerName, container['metadata'])
            if existingContainerName.startswith("rentestimator-model"):
                parts = existingContainerName.split("-")
                print(parts)
                if (len(parts) == 3):
                    newSuffix = int(parts[-1])
                    if (newSuffix > suffix):
                        suffix = newSuffix

        suffix += 1
        container_name = str("rentestimator-model-6" + str(suffix))
        print("new container name: ")
        print(container_name)

        for container in containers:            
            print("\t" + container['name'])
            if container_name in container['name']:
                print("EXISTIERTT BEREITS!")
                exists = True

        if not exists:
            # Create the container
            container_client = blob_service_client.create_container(container_name)

        local_file_name = "model.joblib"
        upload_file_path = os.path.join(".", local_file_name)

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(file=upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)

    except Exception as ex:
        print('Exception:')
        print(ex)
        exit(1)

def load_model(container_name='rentestimator-model-1', model_blob_name='model.joblib'):
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
    
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=model_blob_name)
    
    download_file_path = os.path.join(".", model_blob_name)
    
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print(f"Downloaded model '{model_blob_name}' from container '{container_name}'.")

    model = load(download_file_path)
    print("Model loaded successfully.")

    return model

if __name__ == "__main__":
    load_model()