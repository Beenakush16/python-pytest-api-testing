from faker import Faker

def createPostRequest():
    fake = Faker()
    body = {
        "name": fake.name(),
        "job": fake.job(),
    }
    return body