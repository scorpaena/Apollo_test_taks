from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Event, EventType
import json


class EventTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user1', password='passw1')
        self.event_type = EventType.objects.create(name = 'type1')
        self.token, _ = Token.objects.get_or_create(user = self.user)
        # print(self.user, self.event_type, self.token.key)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
       

    def test_event_post(self):
        payload = {
            'user': self.user.id,
            'event_type': self.event_type.id,
            'info': {'this': 1, 'that': 2},
            'timestamp': timezone.now(),
            'created_at': timezone.now()
        }
        request = self.client.post('/event/', 
            data=payload,
            format = 'json',
            headers = {'Authorization': 'Token '+ self.token.key}
        )
        # print(request.json())
        self.assertEqual(request.status_code, 201)
