from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Snack,Post
# Create your tests here.
class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_snack = Snack.objects.create(
            name="rake",
            purchaser=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_snack.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_purchaser = str(snack.purchaser)
        actual_name = str(snack.name)
        actual_description = str(snack.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["name"], "rake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("snack_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_purchaser_can_delete_snack(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("snack_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_post = Post.objects.create(
            random_comment="very tasty snack", 
        )
        test_post.save()
    
    def test_post_model(self):
        post = Post.objects.get(id=1)
        actual_random_comment = str(post.random_comment)
        self.assertEqual(actual_random_comment, "very tasty snack")

    def test_get_post_list_without_login(self):
        url = reverse("post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post = response.data
        self.assertEqual(len(post), 1)
        self.assertEqual(post[0]["random_comment"], "very tasty snack")