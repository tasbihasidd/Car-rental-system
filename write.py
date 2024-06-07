import json

# def write_json(filepath,cars):
#     d = json.dumps(d)
#     with open(filepath,'w') as file:
#         data = file.write()
#         print("Data written successfully")

def write_json(data, filepath):
    try:
        d = json.dumps(data)
        with open(filepath, 'w') as file:
            file.write(d)
            print("data written succestully")
    except Exception as e:
        print('Error while writing in json',e)
        