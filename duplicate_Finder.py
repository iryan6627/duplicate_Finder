import hashlib, os, shutil, sys;
storage_Dictionary = {};
dupe_Finder = {};
parent = 'C:/Users/ryan6/Documents/python_related/';
files_To_Hash = filter(os.path.isfile, os.listdir());
#this is to test if the file has been updated.
#Creates and obtains the hashes for each video in the directory
for video in files_To_Hash:
    with open(os.path.join(parent, video), 'rb') as content_Stream:
        content = content_Stream.read(); #read files in byte stream
        hashed = hashlib.sha256(); #the hashing function
        hashed.update(content); #methods return None when assigned to variables
        storage_Dictionary[f'{video}'] = hashed.hexdigest();


# flip the values and keys, so you can see which keys have the same values
for i, v in storage_Dictionary.items(): 
    if v in dupe_Finder: #if this KEY, not items/keyvalue pair with .items()
        dupe_Finder[v].append(i);
    else:
        dupe_Finder[v] = [i]; # can't append without a list/squares
print(dupe_Finder);

#print out the keys that have multiple values (flipped)
for each_Key in dupe_Finder.values():
    if len(each_Key) > 1:
        c = ', '
        print(str(c.join(each_Key)) + ' have the same hashes!'); 
        for each_Item in each_Key:
            shutil.move(os.path.join(parent, each_Item), 'C:/Users/ryan6/Documents/detected_dupes')
        print('Moved files to detected_dupes folder!');

