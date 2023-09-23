from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.urls import reverse


class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        client = APIClient()
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

    def test_user_login(self):
        # Attempt to log in with valid credentials
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if an authentication token is returned
        self.assertIn('token', response.data)

        # Verify that the token is associated with the user
        token_key = response.data['token']
        token = Token.objects.get(key=token_key)
        self.assertEqual(token.user, self.user)

    def test_user_login_invalid_credentials(self):
        # Attempt to log in with invalid credentials
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TaskCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_task_creation(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'title': 'Test Task', 'description': 'Description', 'due_date': '2023-09-30', 'status': 'pending'}
        response = client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


class TaskEditingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='Description', due_date='2023-09-30', status='pending', assignee=self.user)

    def test_task_editing(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'due_date': '2023-10-15', 'status': 'in_progress'}
        response = client.put(f'/api/tasks/{self.task.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')


class TaskPatchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='Description', due_date='2023-09-30', status='pending', assignee=self.user)

    def test_task_patch(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'status': 'in_progress'}
        response = client.patch(f'/api/tasks/{self.task.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.description, 'Updated Description')
        self.assertEqual(self.task.status, 'in_progress')


class TaskDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='Description', due_date='2023-09-30', status='pending', assignee=self.user)

    def test_task_delete(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)


class UserRegistrationViewTest(TestCase):
    def test_user_registration_view(self):
        # Create a test user registration data
        user_data = {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
        }

        # Get the URL for the user registration view
        url = reverse('register')

        # Perform a POST request with the user registration data
        response = self.client.post(url, data=user_data)

        # Check if the user is redirected to the login page upon successful registration
        self.assertRedirects(response, reverse('login'))

        # Check if the user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())


class AuthViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='TestPassword123')

    def test_login_view(self):
        # Get the URL for the login view
        url = reverse('login')

        # Perform a GET request to the login view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_view(self):
        # Create a Django test client
        client = Client()

        # Log in the test user
        client.login(username='testuser', password='TestPassword123')

        # Get the URL for the authenticated view (replace with your actual URL)
        url = reverse('login')

        # Perform a GET request to the authenticated view
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)


class UserLogoutViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='TestPassword123')
        self.client.login(username='testuser', password='TestPassword123')

    def test_user_logout_view(self):
        # Get the URL for the user logout view
        url = reverse('logout')

        # Perform a GET request to the logout view
        response = self.client.get(url)

        # Check if the user is redirected to the login page upon successful logout
        self.assertRedirects(response, reverse('login'))

        # Check if the user is no longer authenticated
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)


class TaskViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='TestPassword123')

        # Create some tasks assigned to the test user
        self.task1 = Task.objects.create(title='Task 1', description='Test description', due_date=timezone.now().date(), assignee=self.user)
        self.task2 = Task.objects.create(title='Task 2', description='Test description', due_date=timezone.now().date(), assignee=self.user)

        # Create a client and log in the test user
        self.client = Client()
        self.client.login(username='testuser', password='TestPassword123')

    def test_task_list_view(self):
        # Get the URL for the task list view
        url = reverse('task_list')

        # Perform a GET request to the task list view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the tasks assigned to the test user are present in the context
        tasks = response.context['tasks']
        self.assertIn(self.task1, tasks)
        self.assertIn(self.task2, tasks)

    def test_task_detail_view(self):
        # Get the URL for the task detail view for task1
        url = reverse('task_detail', args=[self.task1.pk])

        # Perform a GET request to the task detail view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the task in the context matches task1
        task = response.context['task']
        self.assertEqual(task, self.task1)

    def test_task_create_view(self):
        # Get the URL for the task create view
        url = reverse('task_create')

        # Perform a GET request to the task create view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the form is present in the context
        self.assertIn('form', response.context)

    def test_task_update_view(self):
        # Get the URL for the task update view for task1
        url = reverse('task_edit', args=[self.task1.pk])

        # Perform a GET request to the task update view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the form is present in the context
        self.assertIn('form', response.context)

    def test_task_delete_view(self):
        # Get the URL for the task delete view for task1
        url = reverse('task_delete', args=[self.task1.pk])

        # Perform a GET request to the task delete view
        response = self.client.get(url)

        # Check if the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the task1 is deleted
        with self.assertRaises(Task.DoesNotExist):
            self.task1.refresh_from_db()
