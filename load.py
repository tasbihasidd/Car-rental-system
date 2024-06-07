import json

def load_json(filepath : str) -> dict:
    try:
        with open(filepath,'r') as file:
            d = file.read()
            # print(d)
            data = json.loads(d)
            # print("DATA  -> ",data)
            return data
    except Exception as e:
        print("Error while loading json file")
        

# print(load_json('cars.json'))