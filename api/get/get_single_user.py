import allure
import requests


class StepsGetSingleUser:
    @allure.step("")
    def get_single_user(self):
        body = {
                "data": {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg"
                },
                "support": {
                    "url": "https://reqres.in/#support-heading",
                    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
                }
        }
        response = requests.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        assert response.json().get('first_name') == 'Janet'

