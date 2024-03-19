cloud_env = ["aws","gcp","azure"]

try:
    print(cloud_env[4])
except:
    print("exception handled")

finally:
    print("i will execute anyways")

print("this code should run")


# raise Exception ("this is new exception manually created") # Creating own Exception

try:
    a = 10
    b = 0
    c = a/b

except ZeroDivisionError as e:
    print(e)
