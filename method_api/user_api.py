from api import UserApi

def create_user(user_data):
    response = UserApi.create_user(user_data)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def delete_user(user_data):
    UserApi.delete_user(user_data['accessToken'])
