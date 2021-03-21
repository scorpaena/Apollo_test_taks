from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Event, EventType
import json

time = timezone.now()

class EventTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        self.client = APIClient()
        self.client1 = APIClient() # unauthorized client
        self.user = User.objects.create(username='user1', password='passw')
        self.event_type = EventType.objects.create(name='type1')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        # print(self.user.password, self.event_type, self.token.key)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # setting up the data for test_event_creation
        self.event = Event.objects.create(
            user=self.user,
            event_type=self.event_type,
            info=json.dumps({'this': 1, 'that': 2}),
            timestamp=time,
            created_at=time
        )

    def test_event_post_positive(self):
        payload = {
            'user': self.user.id,
            'event_type': self.event_type.id,
            'info': {'this': 1, 'that': 2},
            'timestamp': time,
            'created_at': time
        }
        request = self.client.post('/event/', 
            data=payload,
            format = 'json',
            # headers = {'Authorization': 'Token '+ self.token.key} # not needed, since client is authorized above
        )
        # print(request.json())
        self.assertEqual(request.status_code, 201)

    def test_event_post_negative(self):
        payload = {
            'user': self.user.id,
            'event_type': self.event_type.id,
            'info': {'this': 1, 'that': 2},
            'timestamp': time,
            'created_at': time
        }
        request = self.client1.post('/event/', 
            data=payload,
            format = 'json',
        )
        # print(request.json())
        self.assertEqual(request.status_code, 401)

    def test_event_model(self):
        event_fetched = Event.objects.get(event_type=self.event_type)
        self.assertEqual(event_fetched.info, json.dumps({'this': 1, 'that': 2}))
        self.assertEqual(event_fetched.timestamp, time)
        self.assertTrue(isinstance(self.event, Event))

