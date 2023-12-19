# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

from azure.storage.blob import BlobServiceClient



def orchestrator_function(context: df.DurableOrchestrationContext):
    # data = {"key" : "Successful try"}
    # path = open("C:/Users/hammad.mukhtar/Desktop/wifi_analytics/final_json_v1s.json")

    # Azure Storage account connection string
    connection_string = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Name of the container where the JSON file is stored
    container_name = "files"

    # Name of the JSON file you want to read
    blob_name = "final_json_v1s.json"

    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # Get a reference to the blob (file) in the container
    blob_client = container_client.get_blob_client(blob_name)

    # Download the content of the blob (file)
    blob_data = blob_client.download_blob()

    # Read the content of the blob (file)
    data = blob_data.readall().decode('utf-8')
    # data = json.load(path)
    result1 = yield context.call_activity('Hello', data)
    result2 = yield context.call_activity('Hello', "Seattle")
    result3 = yield context.call_activity('Hello', "London")
    return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)