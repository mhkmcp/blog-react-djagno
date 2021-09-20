from django.test import TestCase
from .models import Post, Category
from django.contrib.auth.models import User
import pytest


class Test_Create_Categroy(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Django')
        test_user_1 = User.objects.create(username='testuser1', password='testuser@1')
        test_post = Post.objects.create(category_id=1,
                                        title='Post Title',
                                        excerpt='Post Excerpt',
                                        content='Post Detail Content',
                                        status='published')

    def test_blog_content(self):
        cat = Category.objects.get(id=1)
        post = Post.postobjects.get(id=1)
        author = post.author

        self.assertEqual(author, 'testuser1')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'Django')
        self.assertEqual(post.content, 'Post Detail Content')
        self.assertEqual(post.status, 'published')
