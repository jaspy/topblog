from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_detail_url(self):
        url = reverse('post-detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
