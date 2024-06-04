details_of_servers = {
    "env": "dev",
    "server": "amzon linux2",
    "ram": 8096,
    "cpu": 4,
    "active": True
}

print(details_of_servers["env"]) # iterate single value of dictionary

details_of_servers.get("server")

print(details_of_servers.get("server")) # iterage the single value of dictionary using get function

if details_of_servers["active"]:
    print(details_of_servers["env"])


## Example 2

details_of_devservers = {
    "env": "dev",
    "server": "amzon linux2",
    "ram": 8096,
    "cpu": 4,
    "active": False
}

details_of_prodservers = {
    "env": "prod",
    "server": "amzon linux2",
    "ram": 16384,
    "cpu": 8,
    "active": True
}

servers_detils = [details_of_devservers,details_of_prodservers] # creating list of above dictionarys to print both dic values together

for server in servers_detils:
    print(server)  # here will get the key-value but in list data format but we want it in dictronary format

    for key,value in server.items(): # iterating the values of server in more details. here server is a dictionay and dictionary allways holds a Items value thats why we have used the items at the end.
        print(key,":",value)   # here will get all values in key-value pair


        if key == "active" and value == True: # printing the 
            print(server)
            print(server.values())


