from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Condition, Habit, Reward
from users.models import User


class ConditionTestCase(APITestCase):
    """Тесты для модели Condition."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@coo.coo")
        self.condition = Condition.objects.create(
            place="Тесты", start_time="12:00:00", frequency=2, seconds_to_complete=100
        )
        self.client.force_authenticate(user=self.user)

    def test_condition_create(self):
        """Тестирование создания нового условия с корректными данными."""
        url = reverse("habit:conditions-list")
        data = {
            "place": "Новое условие",
            "start_time": "13:00:00",
            "frequency": "2",
            "seconds_to_complete": "15",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Condition.objects.count(), 2)

    def test_condition_retrieve(self):
        """Тестирование просмотра одного условия."""
        url = reverse("habit:conditions-detail", args=(self.condition.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.condition.place)

    def test_condition_update(self):
        """Тестирование обновления условия."""
        url = reverse("habit:conditions-detail", args=(self.condition.pk,))
        data = {"place": "Измененное место"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Измененное место")

    def test_condition_delete(self):
        """Тестирование удаления условия."""
        url = reverse("habit:conditions-detail", args=(self.condition.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Condition.objects.count(), 0)

    def test_condition_list(self):
        """Тестирование просмотра списка условий."""
        url = reverse("habit:conditions-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.condition.pk,
                    "place": self.condition.place,
                    "start_time": self.condition.start_time,
                    "frequency": self.condition.frequency,
                    "seconds_to_complete": self.condition.seconds_to_complete,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
        self.assertEqual(data["count"], 1)


class RewardTestCase(APITestCase):
    """Тесты для модели Reward."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@coo.coo")
        self.reward = Reward.objects.create(
            name="Тестовое вознаграждение", owner=self.user, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_reward_create(self):
        """Тестирование создания нового вознаграждения с корректными данными."""
        url = reverse("habit:rewards-list")
        data = {
            "name": "Новое вознаграждение",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reward.objects.count(), 2)

    def test_reward_retrieve(self):
        """Тестирование просмотра одного вознаграждения."""
        url = reverse("habit:rewards-detail", args=(self.reward.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(data.get("is_public"))

    def test_reward_update(self):
        """Тестирование обновления вознаграждения."""
        url = reverse("habit:rewards-detail", args=(self.reward.pk,))
        data = {"is_public": False}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(data.get("is_public"))

    def test_reward_delete(self):
        """Тестирование удаления вознаграждения."""
        url = reverse("habit:rewards-detail", args=(self.reward.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reward.objects.count(), 0)

    def test_reward_list(self):
        """Тестирование просмотра списка вознаграждений."""
        url = reverse("habit:rewards-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.reward.pk,
                    "name": self.reward.name,
                    "owner": self.user.pk,
                    "is_public": True,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
        self.assertEqual(data["count"], 1)


class HabitTestCase(APITestCase):
    """Тесты для модели Habit."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@coo.coo")
        self.condition = Condition.objects.create(
            place="Тесты", start_time="12:00:00", frequency=2, seconds_to_complete=100
        )
        self.reward = Reward.objects.create(
            name="Тестовое вознаграждение", owner=self.user, is_public=True
        )
        self.pleasant_habit = Habit.objects.create(
            name="Тестовая приятная привычка",
            owner=self.user,
            condition=self.condition,
            is_pleasant=True,
            is_public=False,
        )
        self.habit = Habit.objects.create(
            name="Тестовая привычка",
            owner=self.user,
            condition=self.condition,
            is_public=True,
            is_pleasant=False,
            associated_habit=self.pleasant_habit,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тестирование создания новой привычки с корректными данными."""
        url = reverse("habit:habits-list")
        data = {
            "name": "Новая привычка",
            "condition": self.condition.pk,
            "is_public": True,
            "is_pleasant": True,
            "associated_habit": "",
            "reward": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 3)

    def test_habit_retrieve(self):
        """Тестирование просмотра одной привычки."""
        url = reverse("habit:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(data.get("is_public"))

    def test_habit_update(self):
        """Тестирование обновления привычки."""
        url = reverse("habit:habits-detail", args=(self.habit.pk,))
        data = {
            "is_public": False,
            "is_pleasant": False,
            "associated_habit": "",
            "reward": self.reward.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(data.get("is_public"))

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("habit:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_list(self):
        """Тестирование просмотра списка привычек."""
        url = reverse("habit:habits-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 2)


class RewardReadOnlyViewSetTestCase(APITestCase):
    """Тесты для RewardReadOnlyViewSet."""

    def setUp(self):
        """Окружение для тестов."""
        self.user = User.objects.create(email="test@coo.coo")
        self.public_reward = Reward.objects.create(
            name="Тестовое публичное вознаграждение", owner=self.user, is_public=True
        )
        self.not_public_reward = Reward.objects.create(
            name="Тестовое непубличное вознаграждение", owner=self.user, is_public=False
        )
        self.client.force_authenticate(user=self.user)

    def test_public_reward_list(self):
        """Тестирование просмотра списка публичных вознаграждений."""
        url = reverse("habit:public_rewards-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.public_reward.pk,
                    "name": self.public_reward.name,
                    "owner": self.user.pk,
                    "is_public": True,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
        self.assertEqual(data["count"], 1)

    def test_public_reward_retrieve(self):
        """Тестирование просмотра одного публичного вознаграждения."""
        public_reward_url = reverse(
            "habit:public_rewards-detail", args=(self.public_reward.pk,)
        )
        public_response = self.client.get(public_reward_url)
        data = public_response.json()
        self.assertEqual(public_response.status_code, status.HTTP_200_OK)
        self.assertTrue(data.get("is_public"))
        not_public_reward_url = reverse(
            "habit:public_rewards-detail", args=(self.not_public_reward.pk,)
        )
        not_public_response = self.client.get(not_public_reward_url)
        data = not_public_response.json()
        self.assertEqual(not_public_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(data.get("is_public"))
