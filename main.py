import requests
from token import my_token



token = 'OAuth ' + my_token

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': token}


def create_folder(folder_name):
    params = {'path': folder_name}
    reply = requests.put(url=URL, params=params, headers=headers)
    return reply.status_code


def folder_info(folder_name):
    params = {'path': folder_name}
    reply = requests.get(url=URL, params=params, headers=headers)
    return reply.status_code


if __name__ == '__main__':
    create_folder('SomeFolder')
    folder_info('SomeFolder')
