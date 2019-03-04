from django.test import TestCase, Client
from django.urls import reverse
from blog.models  import Post


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.Model1 = Post.objects.create(
            title='Test1',
            author='TestAuthor',
            content="Test content1",
        )

    def test_home_GET(self):

        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_detail_GET(self):

        slug = Post.objects.first().slug
        response = self.client.get(reverse('post-detail', args=[slug]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')