from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.habbits.models import Habbit


def create_user():
    User = get_user_model()
    return User.objects.create_user(username="test", password="test")


def get_auth_header(user, client):
    return {
        "Authorization": client.post(
            "/users/login/",
            {"username": user.username, "password": user.password},
        ).json()
    }


class HabbitsViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.client.login(username=self.user.username, password="test")
        self.test_data = {
            "name": "test name",
            "place": "test place",
            "action": "test action",
            "action_start_time": "12:00:00",
            "action_time_seconds": 120,
            "period_days": 1,
            "is_beneficial": True,
            "reward": "test reward",
            "is_public": False,
        }

    def test_habbits_public_get(self):
        response = self.client.get("/habbits/public/").json()
        self.assertEqual(response, {"count": 0, "next": None, "previous": None, "results": []})

    def test_habbits_get(self):
        response = self.client.get("/habbits/private/").json()
        self.assertEqual(response, {"count": 0, "next": None, "previous": None, "results": []})

    def test_habbits_post(self):
        response = self.client.post("/habbits/private/", data := self.test_data).json()
        response.pop("id")
        response.pop("user")
        data["reward_habbit"] = None
        self.assertEqual(response, data)

    def test_habbits_id_get(self):
        habbit = Habbit.objects.create(user=self.user, **self.test_data)
        response = self.client.get(f"/habbits/private/{habbit.id}/", data := self.test_data).json()
        response.pop("id")
        response.pop("user")
        data["reward_habbit"] = None
        self.assertEqual(response, data)

    def test_habbits_id_put(self):
        habbit = Habbit.objects.create(user=self.user, **self.test_data)
        data = self.test_data
        self.test_data["name"] = data["name"] = "test name 2"
        response = self.client.put(f"/habbits/private/{habbit.id}/", self.test_data).json()
        response.pop("id")
        response.pop("user")
        data["reward_habbit"] = None
        self.assertEqual(response, data)

    def test_habbits_id_patch(self):
        habbit = Habbit.objects.create(user=self.user, **self.test_data)
        data = self.test_data
        self.test_data["name"] = data["name"] = "test name 2"
        response = self.client.put(f"/habbits/private/{habbit.id}/", self.test_data).json()
        response.pop("id")
        response.pop("user")
        data["reward_habbit"] = None
        self.assertEqual(response, data)

    def test_habbits_id_delete(self):
        habbit = Habbit.objects.create(user=self.user, **self.test_data)
        response = self.client.delete(f"/habbits/private/{habbit.id}/")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
