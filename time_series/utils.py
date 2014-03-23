import json

def read_file(loc):
    if loc[-4:] == ".csv":
        with open (loc, 'r') as read_file:
            for line in read_file:
                yield line
    elif loc[-5:] == ".json":
        with open (loc, 'r') as json_data:
            objs = json.load(json_data)
            for obj in objs:
                yield obj
    else:
        raise Exception("Could not parse file type")