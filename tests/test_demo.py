import requests
import logging
from request.postRequest import createPostRequest

class TestPytestDemo:
    def test_get_demo(self):
        base_url = 'https://jsonplaceholder.typicode.com'
        response = requests.get(f"{base_url}/todos/1")

        assert response.status_code == 200
        assert response.json()['userId'] == 1
    def test_post_demo(self):
        base_url = 'https://reqres.in'
        response = requests.post(f"{base_url}/api/users",json=createPostRequest(),headers={"x-api-key": "reqres-free-v1"})
        logging.info(response.json())
        assert response.status_code == 201
