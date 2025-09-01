from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users_app.models import StudentProfil


# Create your tests here.






class StudentProfilTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Admin1',
            email='admin15@gmail.com',
            password='root1')

        self.staff_user = User.objects.create_user(
            username='Admin2',
            email='admin25@gmail.com',
            password='root2',
            is_staff=True)


        self.student1 = StudentProfil.objects.create(
            user=self.user,
            birth_data="2003-07-03",
            parent_name='doi',
            parent_phone='9326548')

    def test_studentprofil_list(self):
        url =reverse('studentprofil-list')
        response =self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['user'],self.user.id)

    def test_studentprofil_update(self):
        url =reverse('studentprofil-detail',args=[self.student1.pk])
        data = { 'user':self.user.id,
            'birth_data':"2003-07-03",
            'parent_name':'don',
            'parent_phone':'9326548'}
        response =self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['parent_name'], 'don')

