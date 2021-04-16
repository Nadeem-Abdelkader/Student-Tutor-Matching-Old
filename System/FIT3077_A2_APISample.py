#!/usr/bin/env python

# Access the student tutoring system web service and query data in Python

# To make HTTP requests with Python's Request Library,
# You will need to install request with command "pip install requests" and import requests in the script, as below.

import requests

# NOTE: In order to access the web service, you will need to include your API key in the Authorization header of all requests you make.
# Your personal API key can be obtained here: https://fit3077.com
my_api_key = '<INSERT YOUR API KEY HERE>'

# Provide the root URL for the web service. All web service request URLs start with this root URL.
root_url = 'https://fit3077.com/api/v1'


# To get a specific resource from the web service, extend the root URL by appending the resource type you are looking for.
# For example: [root_url]/user will return a JSON array object containing all users.

users_url = root_url + "/user"


'''
Part 1 - Unauthenticated requests
'''

# This request is unauthenticated (API key not attached), and will return an error.
response = requests.get(url=users_url)
json_data = response.json()

print('Part 1\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason)) # Status code of 4xx or 5xx indicates an error with the request or with the server, respectively.
print('Error message is: {}'.format(json_data['message'])) # Might not always be defined, so be careful
print('Full JSON response is: {}'.format(json_data))
print('----\n\n')


'''
Part 2 - Performing GET requests that return an array of objects.
'''

# This request is authenticated (API key attached in the Authorization header), and will return the JSON array object containing all users.
response = requests.get(url=users_url, headers={ 'Authorization': my_api_key })
json_data = response.json()

print('Part 2\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('Full JSON response is: {}'.format(json_data))

print()

# Error checking for this sample code. You can check the status code of your request, as part of performing error handling in your assignment.
if response.status_code != 200:
  raise Exception('Please specify your API key in line 12 to continue using this sample code.')

# The GET /user endpoint returns a JSON array, so we can loop through the response as we could with a normal array/list.
for user in json_data:
  print(user)

print('----\n\n')

# Get the first user object in the array and keep for future use in later parts of this sample code.
user_object_for_part_3 = json_data[0]


'''
Part 3a - Performing an invalid GET request to fetch a particular resource by ID.
'''

# To get a particular User resource, you will need to specify the user ID you are interested in. Simply extend the users_url by appending the user's id.

users_id_url = users_url + "/this-is-my-make-believe-id"

# This request will fail as the user's ID is invalid/does not exist.
response = requests.get(url=users_id_url, headers={ 'Authorization': my_api_key })
json_data = response.json()

print('Part 3a\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason)) # Error 400 indicates a problem with our request.
print('Full JSON response is: {}'.format(json_data))
print('----\n\n')


'''
Part 3b - Performing a valid GET request to fetch a particular resource by ID.
'''

# This request will succeed (assuming there was at least one user object returned in the array from Part 2).
users_id_url = users_url + "/{}".format(user_object_for_part_3['id'])

response = requests.get(url=users_id_url, headers={ 'Authorization': my_api_key })
json_data = response.json()

print('Part 3b\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('Full JSON response is: {}'.format(json_data))
print('----\n')


'''
Part 3c - Performing a valid GET request to fetch a particular resource by ID, with query parameters.
'''

# To get more data for users (e.g. their competencies and qualifications), you can add query params to the request.
# There are two ways to do this:
# 1. Directly append the query string to the end of the request URL - e.g. users_id_url = users_id_url + '?fields=competencies'
# 2. Attach a params keyword argument to the request, containing the additional fields that you wish to obtain.
users_id_url = users_url + "/{}".format(user_object_for_part_3['id'])

# Select competencies as the additional field that we want. (n.b. see approach #2 mentioned above)
response = requests.get(url=users_id_url, headers={ 'Authorization': my_api_key }, params={ 'fields': 'competencies' })

# To select multiple fields, provide an array instead.
# response = requests.get(url=users_id_url, headers={ 'Authorization': my_api_key }, params={ 'fields': ['competencies', 'qualifications'] })

json_data = response.json()

print('Part 3c\n----')
print(response.url) # Resulting URL that gets called (n.b. see approach #1 mentioned above)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('Full JSON response is: {}'.format(json_data)) # Note that the object now has the competencies property returned.
print('----\n')


'''
Part 4 - Authenticating a user's credentials using the POST /user/login endpoint
'''
users_login_url = users_url + "/login"

# Note the post() method being used here.
# A request body needs to be supplied to this endpoint, otherwise a 400 Bad Request error will be returned.
response = requests.post(
  url=users_login_url,
  headers={ 'Authorization': my_api_key },
  params={ 'jwt': 'true' }, # Return a JWT so we can use it in Part 5 later.
  data={
    'userName': user_object_for_part_3['userName'],
    'password': user_object_for_part_3['userName'] # The password for each of the sample user objects that have been created for you are the same as their respective usernames.
  }
)

json_data = response.json()
jwt = json_data['jwt']

print('Part 4\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('Full JSON response is: {}'.format(json_data)) # The JWT token that has just been issued will be returned since we set ?jwt=true.
print('----\n')


'''
Part 5a - Verifying a JWT using the POST /user/verify-token endpoint
'''
users_verify_token_url = users_url + "/verify-token"

# Note the post() method being used here.
# A request body needs to be supplied to this endpoint, otherwise a 400 Bad Request error will be returned.
# Be careful: This endpoint does not return a JSON response if verification succeeds, so calling the line of code 'json_data = response.json()' will cause your program to crash.
response = requests.post(
  url=users_verify_token_url,
  headers={ 'Authorization': my_api_key },
  data={
    'jwt': jwt
  }
)

print('Part 5a\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('----\n')


'''
Part 5b - Verifying a forged/tampered JWT using the POST /user/verify-token endpoint
'''
users_verify_token_url = users_url + "/verify-token"

# Note the post() method being used here.
# A request body needs to be supplied to this endpoint, otherwise a 400 Bad Request error will be returned.
# A JSON response will only be returned by the POST /user/verify-token endpoint if there were problems verifying the JWT.
response = requests.post(
  url=users_verify_token_url,
  headers={ 'Authorization': my_api_key },
  data={
    'jwt': jwt + 'tampered' # Tamper with the JWT.
  }
)

json_data = response.json()

print('Part 5b\n----')
print(response.url)
print('Status code is: {} {}'.format(response.status_code, response.reason))
print('Error message is: {}'.format(json_data['message'])) # Again, be careful here. Note that all 4xx and 5xx errors are guaranteed to return a JSON response.
print('----\n')
