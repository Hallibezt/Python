import pickle #pickle python to python - not considered secure, cPickle is faster (must be installed with pip)
#json python to other languages

#Create dictionary
friends1 = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 25252525]}
friends2 = {"John": [20, "Singapure", 3234342], "Sigga": [25, "Reykjavik", 25252525]}

friends = (friends1, friends2)

#Can not write dictionary, it must be in string format - or other more portable format: json or pickle
#with open('friends.txt', 'w') as f:
  #  f.write(friends)       

#Now with pickle, open .data and write+binary
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)     

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)