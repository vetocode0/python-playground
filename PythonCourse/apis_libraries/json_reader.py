import os
import json

# dirs = os.listdir("../../samples/appsync-chat-app-cdk/cdk.out/")
# for file in dirs:
#    print(file)

folder = "../samples/appsync-chat-app-cdk/cdk.out/"
entries = os.scandir(folder)
for entry in entries:
  if os.path.isfile(entry):
      print('File:', entry.name)
  elif os.path.isdir(entry):
      print('Directory:', entry.name)

print('\n------------------------\n')

# closes the file at the end of execution even if exception is raised
# with open('../../samples/appsync-chat-app-cdk/cdk.out/outputs.json') as file:
    # Do file operations here

# file = open('../../samples/appsync-chat-app-cdk/cdk.out/outputs.json')
# try:
    # do some stuff
#     pass
# finally:
#     file.close()

file = open("../samples/appsync-chat-app-cdk/cdk.out/outputs.json")
jsonData = json.load(file)
print("GraphQL API ID: ", jsonData['AppSyncAPIStack']['GraphQLAPIID'])

# Returns the next line in file as a string
# result = file.readline()
# result = file.readline()

# returns all lines as a list. Iterate using for loop

# result = file.readlines()
# for line in result:
#     print(line)

# OR

# for line in file:
#     print(line)

# folder = "../samples/appsync-chat-app-cdk/cdk.out/"

# location_original = os.path.join(folder, 'outputs.json')
# location_destination = os.path.join('./', 'outputs.json')

# allows us to move a file to a new path
# os.rename(location_original, location_destination)

# os.mkdir()

