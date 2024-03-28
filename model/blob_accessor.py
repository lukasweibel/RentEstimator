import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from joblib import dump, load

load_dotenv()

azure_connection_string = os.getenv("AZURE_CONNECTION_STRING")

def save_model(regressor):
    try:
        print("Azure Blob Storage Python quickstart sample")

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

        # Find the highest existing container suffix
        suffix = 0
        containers = blob_service_client.list_containers()
        for container in containers:
            if container.name.startswith("rentestimator-model-"):
                try:
                    current_suffix = int(container.name.split("-")[-1])
                    suffix = max(suffix, current_suffix)
                except ValueError:
                    pass  # Ignore if the suffix cannot be converted to int

        # Increment the suffix for the new container
        suffix += 1
        container_name = f"rentestimator-model-{suffix}"
        print("New container name:", container_name)

        # Create the container if it doesn't exist
        container_client = blob_service_client.create_container(container_name)

        local_file_name = "model.joblib"
        upload_file_path = os.path.join(".", local_file_name)

        # Assuming you have a model object to save; replace this with your actual model
        model = regressor
        dump(model, upload_file_path)

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

        print("Upload completed successfully.")

        return container_name

    except Exception as ex:
        print('Exception:')
        print(ex)

    
def load_model(model):
    container_name_prefix = "rentestimator-model-"

    model_blob_name='model.joblib'
    
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)

    containers = blob_service_client.list_containers()

    #model_numbers = []
    #for container in containers:
    #    model_numbers.append(int(container.name.split('-')[-1]))
    #
    #latest_container = container_name_prefix + str(max(model_numbers))

    container = model

    blob_client = blob_service_client.get_blob_client(container=container, blob=model_blob_name)

    download_file_path = os.path.join(".", model_blob_name)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    print(f"Downloaded model '{model_blob_name}' from container '{container}'.")

    model = load(download_file_path)
    print(download_file_path)

    return model

if __name__ == "__main__":
    load_model()
