from django.test import TestCase
from .models import Category, Photo, Location
# Create your tests here.


class CategoryTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.category = Category(title='animals')
        self.category.save_category()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    