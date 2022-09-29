from rest_framework.test import APIClient
class TestCreateCategory:
    def test_if_user_is_anonymous_return_401(self):
        #Arrange

        #Act
        client = APIClient()
        client.post()

