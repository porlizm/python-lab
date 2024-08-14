import json

filename = 'file.json'

try: 
    f2 = open(filename, 'r')
    data = json.load(f2)
    if('name' in data):
        print("Hello "+data['name'])
    else:
        name = input("What is your name?")
        f1 = open(filename, 'w')
        json.dump({"name":"Porlizm"}, f1)
        f1.close()
except FileNotFoundError:
    print('file json not found')
except json.decoder.JSONDecodeError as e:
    print(e)
# import json

# filename = 'file.json'

# # Open the file in write mode ('w')
# with open(filename, 'w') as f1:
#     # Use json.dump() to write the data to the file
#     json.dump({"name": "Porlizm"}, f1)
