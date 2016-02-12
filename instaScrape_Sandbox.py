__author__ = 'Abhishek Srivastava'

import json
import os
import re
import requests
import time
import urllib


'''
Get access token
'''

def isSet(next_url):
    if next_url == '':
        return False
    else:
        return True


def setAccessToken():
    global access_token
    if os.path.exists('config.txt'):
        access_token = ''
        config_file = open('config.txt', 'r')
        for line in config_file.readlines():
            if 'access_token' in line:
                access_token = line.split('=')[1]
                print('Token found...')
            else:
                print('Error in config file. No access_token found.')
                exit('Exiting, issue with getting token.')
        config_file.close()
    else:
        print('No access token found. Please create a config file with access token...\nP.S: Details are in Readme file')
        exit()

def createDir():
    if not os.path.exists('Gallery'):
        print('Creating Gallery folder...')
        os.makedirs('Gallery')


def core():
    '''
    Setting up data
    '''
    global seq
    seq = 1
    url = 'https://api.instagram.com/v1/users/self/media/recent?access_token='+str(access_token)+'&count=40'
    response = requests.get(url)
    json_data = json.loads(response.text)
    json_length = len(json_data['data'])

    for itr in range(0, json_length, 1):
            image_url = re.sub(r'\/s[0-9][0-9][0-9][a-z][0-9][0-9][0-9]','',(json_data['data'][itr]['images']['standard_resolution']['url']).replace('https', 'http'))
            print(image_url)
            createDir()
            urllib.urlretrieve(image_url, 'Gallery/Image_' + str(seq) + '.jpg')
            seq += 1
            time.sleep(2)

    if 'next_url' in json_data['pagination']:
            next_url = (json_data['pagination']['next_url'])
            max_id = (json_data['pagination']['next_max_id'])
            print(next_url)
    else:
            next_url = ''

    '''
    Loop through the pagination, if available
    '''
    while isSet(next_url):
        response = requests.get(next_url)
        json_data = json.loads(response.text)
        json_length = len(json_data['data'])
        if 'next_url' in json_data['pagination']:
            next_url = (json_data['pagination']['next_url'])
            print(next_url)
        else:
            next_url = ''


        for itr in range(0, json_length, 1):
            image_url = re.sub(r'\/s[0-9][0-9][0-9][a-z][0-9][0-9][0-9]','',(json_data['data'][itr]['images']['standard_resolution']['url']).replace('https', 'http'))
            print(image_url)
            urllib.urlretrieve(image_url, 'Gallery/Image_{}.jpg'.format(str(seq)))
            seq = seq + 1
            time.sleep(2)


if __name__ == '__main__':
    print('\t\t####################################')
    print('\t\t####################################')
    print('\t\t##### Insta Gallery Downloader #####')
    print('\t\t####################################')
    print('\t\t# Developed by Abhishek Srivastava #')
    print('\t\t####################################')
    print('\t\t####################################')

    setAccessToken()
    print('Started Download')
    core()
    print('Completed full download of {} images. Please check the files in Gallery folder.'.format(seq-1))
