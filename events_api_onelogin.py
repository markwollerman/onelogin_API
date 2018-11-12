#!/usr/bin/env python

'''
Program created by Mark Wollerman to access events reporting with Onelogin
API and output the results to a readable CSV file
This program requires requests, base64m csv and json from PIP and brew installed using Python3
To run this program simply open terminal to the location and use the following command python OLAPI.py
'''

import requests
import base64
import csv
import json

# DO NOT EDIT
url = "https://api.us.onelogin.com/auth/oauth2/token"
payload = "{\n\"grant_type\":\"client_credentials\"\n}"

# paste client_id and client_sectret from onelogin API settings

headers = {
    'authorization': "client_id:YOUR_CLIENT_ID_HERE, client_secret:YOUR_SECRET_HERE",
    'content-type': "application/json", }
response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)
blob = response.json()
#print (blob)
token = blob["data"][0]["access_token"]


# edit the events type ID found in https://developers.onelogin.com/api-docs/1/events/event-resource
url = "https://api.us.onelogin.com/api/1/events?event_type_id=1"

r = requests.get(url, headers={"Authorization": "Bearer " + token})
body = r.json()
# print (body)

with open('events_output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["id","created_at","account_id","user_id","event_type_id","notes","ipaddr","actor_user_id","assuming_acting_user_id","role_id","app_id","group_id","otp_device_id","policy_id","actor_system","custom_message","role_name","app_name","group_name","actor_user_name", "user_name","policy_name","otp_device_name","operation_name","directory_sync_run_id","directory_id","resolution","client_id","resource_type_id","error_description","proxy_ip"])
    i = 0
    while True:
        if url is None:
            break
        else:
            i = i + 1
            print ('Writing to CSV %d' % i)
        r = requests.get(url, headers={"Authorization": "Bearer " + token})
        # convert the return into a json blob
        #body = r.json.dumps(None)
        # parse the blob

        for x in body['data']:
            # print body
            try:
                id = x['id']
            except: pass
            try:
                created_at = x['created_at']
            except: pass
            try:
                account_id = x['account_id']
            except: pass
            try:
                user_id = x['user_id']
            except: pass
            try:
                event_type_id = x['event_type_id']
            except: pass
            try:
                notes = x['notes']
            except: pass
            try:
                ipaddr = x['ipaddr']
            except: pass
            try:
                actor_user_id = x['actor_user_id']
            except: pass
            try:
                assuming_acting_user_id = x['assuming_acting_user_id']
            except: pass
            try:
                role_id = x['role_id']
            except: pass
            try:
                app_id = x['app_id']
            except: pass
            try:
                group_id = x['group_id']
            except: pass
            try:
                otp_device_id = x['otp_device_id']
            except: pass
            try:
                policy_id = x['policy_id']
            except: pass
            try:
                actor_system = x['actor_system']
            except: pass
            try:
                custom_message = x['custom_message']
            except: pass
            try:
                role_name = x['role_name']
            except: pass
            try:
                app_name = x['app_name']
            except: pass
            try:
                group_name = x['group_name']
            except: pass
            try:
                actor_user_name = x['actor_user_name']
            except: pass
            try:
                user_name = x['user_name']
            except: pass
            try:
                policy_name = x['policy_name']
            except: pass
            try:
                otp_device_name = x['otp_device_name']
            except: pass
            try:
                operation_name = x['operation_name']
            except: pass
            try:
                directory_sync_run_id = x['directory_sync_run_id']
            except: pass
            try:
                directory_id = x['directory_id']
            except: pass
            try:
                resolution = x['resolution']
            except: pass
            try:
                client_id = x['client_id']
            except: pass
            try:
                resource_type_id = x['resource_type_id']
            except: pass
            try:
                error_description = x['error_description']
            except: pass
            try:
                proxy_ip = x['proxy_ip']
            except: pass


            # print CSV
            writer.writerow([str(id),str(created_at),str(account_id),str(user_id),str(event_type_id),str(notes),str(ipaddr),str(actor_user_id),str(assuming_acting_user_id),str(role_id),str(app_id),str(group_id),str(otp_device_id),str(policy_id),str(actor_system),str(custom_message),str(role_name),str(app_name),str(group_name),str(actor_user_name),str(user_name),str(policy_name),str(otp_device_name),str(operation_name),str(directory_sync_run_id),str(directory_id),str(resolution),str(client_id),str(resource_type_id),str(error_description),str(proxy_ip)])

            # test to see if reached the end of the query
            if ('pagination' in body) and ('next_link' in body['pagination']):
                url = body['pagination']['next_link'];
            else:
                break;
