import json
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from django.utils.six import StringIO
from rest_framework import status
from rest_framework.test import APITestCase

from hobbies.models import Hobbie

from .models import User


class RandomUserTest(TestCase):
    def test_command_output(self):
        """Creation new hobbies for test"""
        hobbies = [
            'Natacion', 'Voleibol', 'Futbol', 'Correr', 'Estudiar', 'Comer',
            'Caminar', 'Musica', 'Programar'
        ]
        for hobbie in hobbies:
            hob = Hobbie(name=hobbie)
            hob.save()
        out = StringIO()
        call_command('random_user', 4, stdout=out)
        self.assertIn('Successfully created users', out.getvalue())


class AccountTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new User.
        """
        url = reverse('users-list')
        data = {
            "age": 30,
            "genre": "Male",
            "hobbies": [
                {
                    "name": "Prueba"
                },
                {
                    "name": "test"
                }
            ],
            "last_name": "Rosales",
            "name": "Alejandro"
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content.decode("utf-8"))
        # Add Id
        data['id'] = 1
        # Comparation result
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response, data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().age, 30)
        self.assertEqual(User.objects.get().genre.name, 'Male')
        self.assertEqual(User.objects.get().id, 1)
        self.assertEqual(User.objects.get().last_name, 'Rosales')
        self.assertEqual(User.objects.get().name, 'Alejandro')
