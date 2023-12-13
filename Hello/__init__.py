# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

# Updated Hello/__init__.py

import logging

def main(data: str) -> str:
    # Access JSON data in the activity function
    name = data
    # print("---name---"*100, name)
    return f"Hello {name}"