import random
import string
from django.test import TestCase
from blog.models import Category, Comment

class CategoryTestCase(TestCase):
    KEY_LEN = 20

    def test_create_categories(self):
        # Test: Check on creating categories with random names.
        arr_letters_name = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        name_test = "". join(arr_letters_name)
        
        print(f"---> Test with: {name_test}")

        category = Category.objects.create(name=name_test)

        self.assertIsNotNone(category.id) # Check if the id was successfully created in the database
        self.assertEqual(category.name, name_test) # Check if the user was created correctly
