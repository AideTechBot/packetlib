packetlib
=========

A python package for encoding and parsing data.

How to use:
=========
```
encode_data(data,sepchar)
```

data: the data you want encoded in a list 
ex: ["foo","bar","hello,"world"]

sepchar: the char that seperates everything 
ex: "|"

output: "START|foo|bar|hello|world|END"

=========
```
parse_data(data,sepchar)
```
data: the data you want parsed in an encoded string
ex: "START|foo|bar|hello|world|END"

sepchar: the char that seperates everything 
ex: "|"

output: ["foo","bar","hello,"world"]
