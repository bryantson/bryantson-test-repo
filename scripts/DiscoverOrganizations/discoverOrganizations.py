# 
# discoverOrganization.py
#   A simple utility script to call GHES REST API endpoint to get list of organization names
# 
# @author Bryant Son
# @since 08/09/21
#

import requests
import os

#
# GRAB environment variables necessary to connect to GHES:
#
# Personal Access Token (PAT) with orgs permission created from GHES: 
GHES_TOKEN=os.environ.get('GHES_TOKEN')
# GHES host name without prefix HTTPS. e.g. ghes-demo.com
GHES_HOST=os.environ.get('GHES_HOST')
# Name of output file containing list of organization names:
OUTPUT_FILE="organizations.txt"

# SET header with a PAT and API:
customHeaders={'Authorization': 'token ' + GHES_TOKEN, 'Accept': 'application/vnd.github.v3+json'}
# CALL a HTTP request to list organizations: https://docs.github.com/en/enterprise-server@2.22/rest/reference/orgs#list-organizations:
response = requests.get('https://' + GHES_HOST + '/api/v3/organizations', headers=customHeaders)

# SAVE the response as JSON:
listOrgs = response.json()

# CREATE a new file whether or not it exist:
f = open(OUTPUT_FILE,"w")

# Iterate through the organizations and only write the organization name:
for org in listOrgs:
  f.write(org['login'])
  f.write("\n")

# Close the file:
f.close()
