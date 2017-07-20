""" This is the testing file for all bucket routes and methods/functions """
import unittest
from bucketlist import app
from models import User,BucketList
import bucketlist

class RoutesTestCases(unittest.TestCase):
    """ Basic Routes test Cases """       
    
       
    def test_login(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/login', content_type='html/text')
        self.assertEqual(responce.status_code, 200)

       
    def test_signup(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/signup', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
       
    def test_index(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/index', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
       
    def test_create_bucket_list(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/create', content_type='html/text')
        self.assertEqual(responce.status_code, 200)   

      
    def test_my_bucket_list_activities(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_bucket_list_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
        
    def test_my_public_bucket_list_activities(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_public_bucket_list_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
      
    def test_my_private_bucket_list_activities(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_private_bucket_list_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
      
    def test_update_profile(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/profile', content_type='html/text')
        self.assertEqual(responce.status_code, 200)



class BucketlistTests(unittest.TestCase):
    """ These tests are for all crud operations methods """

    def setUp(self):
        """ A test fixture that configures the application to be ready for testing """
        self.user = User()
        self.bucket = BucketList()

    def test_lookup_user(self):
        """ Test to see if a user was added after registration """
        self.user.register_new_user("John", "Password")
        self.assertEqual(True, self.user.lookup_user("John")) 

    def test_login(self) :
        """ Checks if login function works """
        self.user.register_new_user("John", "Password")        
        self.assertEqual(True, self.user.login_user("John","Password","Password"))

    
    def test_add_bucket_activities(self):
        """ Test to see if add bucket list activity functionality is working """
        self.bucket.add_bucket_list_activities(1,"Andela","Join")  
        self.assertEqual(True,self.bucket.check_bucket_list_activities(1))

    def test_edit_bucket_activities(self):
        """ Test to see if edit bucket list activity functionality is working """
        self.bucket.add_bucket_list_activities(2,"Andela","Join")  
        self.bucket.edit_bucket_list_activities(2,"Google","Join") 
        self.assertEqual(True,self.bucket.check_bucket_list_activities(2))

    def test_delete_bucket_list_activities(self):
        """ Test to see if add bucket list activity functionality is working """ 
        self.bucket.add_bucket_list_activities(2,"Andela","Join")     
        self.bucket.delete_bucket_list_activities(2)  
        self.assertEqual(False,self.bucket.check_bucket_list_activities(2))   
   

if __name__ == '__main__':
    unittest.main()
