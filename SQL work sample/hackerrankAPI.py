'''
Most Active Authors

API URL: https://jsonmock.hackerrank.com/api/article_users?page=1
THRESHOLD: integer that represents the threshold value for the number of submission count

The function should return an array of strings that represent the usernames of users 
whose submission count is greater than the given threshold

The usernames in the array must be order in the order they appear in the API response

'''

import requests
import json

def getUsernames(threshold):
    # set variables
    usernames = []
    page = 1
    totalPages = 1 # initial value

    while page <= totalPages:

        # make request for each page
        apiRequest = requests.get(f'https://jsonmock.hackerrank.com/api/article_users?page={page}')
        articles = apiRequest.json()['data']

        # set totalPages value
        if page == 1: 
            totalPages = apiRequest.json()['total_pages']

        # get data for each user
        for value in articles:
            submissionCount = value['submission_count']

            # check if submissionCount is greater than threshold
            if submissionCount > threshold:
                usernames.append(value['username'])
        page += 1

    return usernames



# names = getUsernames(10)

def zigzag_arr(n, arr):
    # LHLH... order
    flag = 1
    cnt_lh = 0
    for i in range(n-1):
        if flag * arr[i] < flag * arr[i+1]:
            continue
        else:
            cnt_lh += 1
        flag *= -1
    # HLHL... order
    flag = 1
    cnt_hl = 0
    for i in range(n-1):
        if flag * arr[i] > flag * arr[i+1]:
            continue
        else:
            cnt_hl += 1
        flag *= -1
    return max(cnt_lh, cnt_hl)