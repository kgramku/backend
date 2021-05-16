from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Post
# Create your tests here.
User = get_user_model()

class PostTestCase(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username='abc', password='somepass')
        self.userb= User.objects.create_user(username='alu', password='somepassword')
        post_obj= Post.objects.create(content='first my post', user= self.user)
        post_obj= Post.objects.create(content='secondmy post', user= self.user)
        post_obj= Post.objects.create(content='secondmy post', user= self.userb)
        post_obj= Post.objects.create(content='secondmy post', user= self.userb)
        self.currentCount = Post.objects.all().count()
        
    def test_post_created(self):
        post_obj= Post.objects.create(content='my post', user= self.user)
        self.assertEqual(post_obj.id, 5)
        self.assertEqual(post_obj.user, self.user)
    
    def get_client(self):
        client = APIClient()
        client.login(username= self.user.username, password='somepass')
        return client
    
    def test_post_list(self):
        client = self.get_client()
        response = client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/posts/action/",{"id" : 1, "action":"like"})
        self.assertEqual(response.status_code, 200)
        likes_count = response.json().get("likes")
        self.assertEqual(likes_count,1)
        #print(response.json())
        #self.assertEqual(len(response.status_code), 4)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/posts/action/",{"id" : 2, "action":"like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/posts/action/",{"id" : 2, "action":"unlike"})
        self.assertEqual(response.status_code, 200)
        likes_count = response.json().get("likes")
        self.assertEqual(likes_count,0)

    def test_action_repost(self):
        client = self.get_client()
        response = client.post("/api/posts/action/",{"id" : 2, "action":"repost"})
        self.assertEqual(response.status_code, 201)
        data = response.json()        
        new_post_id = data.get("id")
        self.assertNotEqual(new_post_id,2)
        self.assertEqual(self.currentCount + 1, new_post_id)
    
    def test_post_create_api_view(self):
        request_data = {"content" : "this is my test."}
        client = self.get_client()
        response = client.post("/api/posts/create/",request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()        
        new_post_id = response_data.get("id")
        self.assertNotEqual(new_post_id,2)
        self.assertEqual(self.currentCount + 1, new_post_id)

    def test_post_detail_api_view(self):   
        client = self.get_client()
        response = client.get("/api/posts/2/")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id,2)

    def test_post_detail_api_view(self):  
        client = self.get_client()
        response = client.delete("/api/posts/2/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/posts/2/delete/")
        self.assertEqual(response.status_code, 404)
        
        response_incorrect_owner = client.delete("/api/posts/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)


    



    
        

