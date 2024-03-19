''' we have to give '[ ]' squre brackets to declare a List '''


env = ["dev","uat","qa","stg","sit","preprod",]
env.insert(1,"testing") # insert object in middle/before the list
env.append("prod") # insert object in end of the list

print(env)


''' printing index value of list iteams'''
print(env[0])

'''adding for loop with list'''
for i in env:
    print(i)








''' get the details of list all functions'''
print(dir(env))
print(env.copy.__doc__)

