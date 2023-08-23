import json
import pickle

def serialize(object, file, protocol):
    if protocol.lower() == 'json':
        with open(file, 'w') as f:
            json.dump(object, f)
    elif protocol.lower() == 'pickle':
         with open(file, 'wb') as f:
            pickle.dump(object, f)            
    else:
        print('Invalid serialization. Use pickle or json!')

            
     
def deserialize(file, protocol):
    if protocol.lower() == 'json':
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    elif protocol.lower() == 'pickle':
         with open(file, 'rb') as f:
            obj = pickle.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')

if __name__ == "__main__":
 
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}
 
    # Serializing using pickle
    serialize(d1, 'a.dat', 'pickle')
 
    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')
 
    print('#' * 20)
 
    # serializing using pickle
    serialize(d1, 'a.json', 'json')
 
    # deserializing
    x = deserialize('a.json', 'json')
    # Notice how the tuple value was not preserved!
    print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}