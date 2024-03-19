Example - 1
def fetching_server_details():
    dev_server = {
        "env": "dev",
        "type": "t2.micro",
        "cpu": 4,
        "ram": 8192,
        "image": "amazon linux2",
        "active": False
    }

    prod_server = {
        "env": "prod",
        "type": "t3.medium",
        "cpu": 8,
        "ram": 16384,
        "image": "amazon linux2",
        "active": True    
    }

    list_of_servers = [dev_server, prod_server]

    for server in list_of_servers:
        # print(server)
        for key, value in server.items(): # items= used the iterate/get the items of dictionary
            print(key, ":", value)

            if key == "active" and value == True:
                return server.get("env") # get - used to get single items of dictionary

result = fetching_server_details()  # keeping the whole function in a variable
print(result)   # printing the function