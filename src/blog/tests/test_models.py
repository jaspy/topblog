from django.test import TestCase
from blog.models import Post, Comment



class TestModels(TestCase):

    def setUp(self):
        self.Model1 = Post.objects.create(
            title='Test1',
            author='TestAuthor',
            content="<h1>Hi it is Markdown!!!</h1>",
            )
                        
    def test_absolute_url(self):
        
        slug = Post.objects.first().slug
        taken_url = Post.objects.first().get_absolute_url()
        expected_url = f'/post/{slug}/'

        self.assertEquals(expected_url, taken_url)
 

