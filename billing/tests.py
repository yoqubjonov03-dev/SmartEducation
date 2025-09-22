from http.client import responses

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from .models import Payments
from users_app.models import Enrollments, Groups

# Create your tests here.
class PaymentsTests(APITestCase):
    fixtures = ['users_app/fixtures/smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.group = Groups.objects.get(id=1)
        self.enrollment=Enrollments.objects.get(id=1)
        self.payment = Payments.objects.get(id=18)


    def test_payment_list(self):
        url = reverse('payments-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_payment_create_signals(self):
        url = reverse('payments-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'enrollment_id': self.enrollment.id,
            'amount': 700000,
            'payment_method': 'Cash'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.enrollment.refresh_from_db()
        self.assertTrue(self.enrollment.is_paid)

    def test_payment_updete(self):
        url = reverse('payments-detail', args=[self.payment.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'enrollment_id': self.enrollment.id,
            'amount': 700000,
            'payment_method': 'Cash'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_payment_delete(self):
        url = reverse('payments-detail', args=[self.payment.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


