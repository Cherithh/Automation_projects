import json

def get_test_data():

    with open("test_data.json",'r') as f:
        data = json.load(f)
        print(data)
    return data
