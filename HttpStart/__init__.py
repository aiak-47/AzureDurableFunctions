# # This function an HTTP starter function for Durable Functions.
# # Before running this sample, please:
# # - create a Durable orchestration function
# # - create a Durable activity function (default name is "Hello")
# # - add azure-functions-durable to requirements.txt
# # - run pip install -r requirements.txt
 
# # Updated HttpStart/__init__.py

# import logging
# import json
# import azure.functions as func
# import azure.durable_functions as df

# async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
#     # Read JSON data from the file
#     try:
#         with open("C:/Users/hammad.mukhtar/Desktop/wifi_analytics/final_json_v1.json", "r") as json_file:
#             req_body = json.load(json_file)
#     except FileNotFoundError:
#         return func.HttpResponse("JSON file not found", status_code=400)
#     except json.JSONDecodeError:
#         return func.HttpResponse("Invalid JSON in file", status_code=400)

#     # Start orchestration with JSON data and set a custom timeout
#     client = df.DurableOrchestrationClient(starter, extended_timeout_seconds=600)  # 10 minutes
#     instance_id = await client.start_new(req.route_params['functionName'], None, req_body)
#     logging.info(f"Started orchestration with ID = '{instance_id}'.")

#     return client.create_check_status_response(req, instance_id)


# Updated HttpStart/__init__.py

import logging
import json
import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:

    client = df.DurableOrchestrationClient(starter)

    # Read JSON data from the file
    try:
        # with open("C:/Users/hammad.mukhtar/Desktop/wifi_analytics/final_json_v1s.json", "r") as json_file:
        req_body = {"first_time":1699276346000,"last_time":1699276346000,"time_diff_mints":0.0,"devkey":"4202770D00000000_2CA684C26A34","phyname":"IEEE802.11","devmac":"34:6A:C2:84:A6:2C","strongest_signal":-89,"min_lat":0.0,"max_lat":0.0,"avg_lat":0.0,"min_lon":0.0,"max_lon":0.0,"avg_lon":0.0,"bytes_data":0,"type":"Wi-Fi AP","manufacturer":"HUAWEI TECHNOLOGIES CO.,LTD","server_uid":"EDF6468A-797C-11EE-A55F-4B49534D4554","min_signal":-94.0,"last_signal":-89.0,"distance (feet)":13.445328843},{"first_time":1699276346000,"last_time":1699276346000,"time_diff_mints":0.0,"devkey":"4202770D00000000_FCAAB5EA7646","phyname":"IEEE802.11","devmac":"46:76:EA:B5:AA:FC","strongest_signal":0,"min_lat":0.0,"max_lat":0.0,"avg_lat":0.0,"min_lon":0.0,"max_lon":0.0,"avg_lon":0.0,"bytes_data":0,"type":"Wi-Fi Client","manufacturer":"Unknown","server_uid":"EDF6468A-797C-11EE-A55F-4B49534D4554","min_signal":"null","last_signal":"null","distance (feet)":0.719685673}
        # req_body = json.load(json_file)
        instance_id = await client.start_new("Hello", None, req_body)

        return client.create_check_status_response(req, instance_id)

    except Exception as e:

        logging.error(f"An Error occurred: {str(e)}")

        return func.HttpResponse("Error occurred while starting orchestration", status_code=500)

    # except FileNotFoundError:
    #     return func.HttpResponse("JSON file not found", status_code=400)
    # except json.JSONDecodeError:
    #     return func.HttpResponse("Invalid JSON in file", status_code=400)

    # Start orchestration with JSON data
    # client = df.DurableOrchestrationClient(starter)
    # instance_id = await client.start_new(req.route_params['functionName'], None, req_body)
    # logging.info(f"Started orchestration with ID = '{instance_id}'.")

    # return client.create_check_status_response(req, instance_id)
