from django.contrib.auth.models import User, Group
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class NewTopicTest(TestCase):
	def setUp(self):
		Board.objects.create(name='Django', description='Django board.')
		user = User.objects.create_user(username='test', email='test@example.com', password='123')
		group, created = Group.objects.get_or_create(name="blogger")
		user.groups.add(group)
		self.client.login(username='test', password='123')

	def test_new_topic_view_success_status_code(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_new_topic_view_not_found_status_code(self):
		url = reverse('new_topic', kwargs={'pk': 999})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_new_topic_url_resolves_new_topic_view(self):
		view = resolve('/boards/1/new/')
		self.assertEqual(view.func, new_topic)

	def test_new_topic_view_contains_link_back_to_board_topics_view(self):
		new_topic_url = reverse('new_topic', kwargs={"pk": 1})
		board_topics_url = reverse('board_topics', kwargs={"pk": 1})
		response = self.client.get(new_topic_url)
		self.assertContains(response, 'href="{0}"'.format(board_topics_url))

	def test_csrf(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertContains(response, 'csrfmiddlewaretoken')

	def test_new_topic_valid_post_data(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		data = {
			'subject': 'Test title',
			'message': 'Lorem ipsum dolor sit amet'
		}
		response = self.client.post(url, data)
		self.assertTrue(Topic.objects.exists())
		self.assertTrue(Post.objects.exists())

	def test_new_topic_invalid_post_data(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.post(url, {})
		form = response.context.get('form')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(form.errors)

	def test_new_topic_invalid_post_data_empty_fields(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		data = {
			'subject': '',
			'message': ''
		}
		response = self.client.post(url, data)
		self.assertEquals(response.status_code, 200)
		self.assertFalse(Topic.objects.exists())
		self.assertFalse(Post.objects.exists())

	def test_contains_form(self):
		url = reverse('new_topic', kwargs={'pk': 1})
		response = self.client.get(url)
		form = response.context.get('form')
		self.assertIsInstance(form, NewTopicForm)