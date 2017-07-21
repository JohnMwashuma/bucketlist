""" This is the testing file for all bucket routes and methods/functions """

import unittest
from bucketlist import app
from models import User, BucketList, BucketlistActivities
import bucketlist



class RoutesTestCases(unittest.TestCase):
    """ Basic Routes test Cases """      
       
    def test_login(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


       
    def test_signup(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    

       
    def test_index(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)



class UserTests(unittest.TestCase):
    """ These tests are for user crud operations methods """

    def setUp(self):
        """ A test fixture that configures the application to be ready for testing """
        self.user = User()  



    def test_lookup_user(self):
        """ Test to see if a user was added after registration """

        self.user.register_new_user("John", "Password","Password")
        response=self.user.lookup_user("John")
        self.assertEqual(response,True) 



    def test_login(self) :
        """ Checks if login function works """

        self.user.register_new_user("John", "Password", "Password") 
        response=self.user.login_user("John","Password")       
        self.assertEqual(response,True)



class BucketlistTests(unittest.TestCase):
    """ Bucket list crud operations methods Test Cases """

    def setUp(self):
        """ A test fixture that configures the application to be ready for testing """
        self.bucket = BucketList()


    
    def test_create_bucket_list(self):
        """ Test to see if create bucket list functionality is working """

        self.bucket.create_bucket_list(user='John',bucket_list_id=1,bucket_list_name="Andela")  
        response=self.bucket.check_bucket_lists(1)
        self.assertEqual(response,True)



    def test_edit_bucket_list(self):
        """ Test to see if edit bucket list functionality is working """

        self.bucket.create_bucket_list(user='John',bucket_list_id=1,bucket_list_name="Andela")  
        self.bucket.edit_bucket_list(bucket_list_id=1,bucket_list_name="Google") 
        response=self.bucket.check_bucket_lists(1)
        self.assertEqual(response,True)



    def test_delete_bucket_list(self):
        """ Test to see if delete bucket list functionality is working """ 

        self.bucket.create_bucket_list(user='John',bucket_list_id=21,bucket_list_name="Andela")     
        self.bucket.delete_bucket_list(21) 
        response=self.bucket.check_bucket_lists(21)
        self.assertEqual(response,False)   



class BucketlistActivitiesTests(unittest.TestCase):
    """ Bucket activities crud operations methods """

    def setUp(self):
        """ A test fixture that configures the application to be ready for testing """ 

        self.bucket = BucketlistActivities()
        

    
    def test_create_bucket_list_activities(self):
        """ Test to see if add bucket list activities functionality is working """

        self.bucket.create_bucket_list_activities(user='John',bucket_list_activity_id=1,bucket_list_name="World Class Dev",title="Andela",description="Join")
        response=self.bucket.check_bucket_list_activities(1)
        self.assertEqual(response,True)



    def test_edit_bucket_list_activities(self):
        """ Test to see if edit bucket list activities functionality is working """

        self.bucket.create_bucket_list_activities(user='John',bucket_list_name="Hiking",bucket_list_activity_id=1,title="Andela",description="Join")  
        self.bucket.edit_bucket_list_activities(bucket_list_activity_id=1,title="Google",bucket_list_name="Maps",description="Travel")
        response=self.bucket.check_bucket_list_activities(1) 
        self.assertEqual(response,True)



    def test_delete_bucket_list_activities(self):
        """ Test to see if delete bucket list activities functionality is working """ 

        self.bucket.create_bucket_list_activities(user='John', bucket_list_activity_id=21,bucket_list_name='Programming',title="Andela",description="Join")     
        self.bucket.delete_bucket_list_activities(21) 
        response=self.bucket.check_bucket_list_activities(21)
        self.assertEqual(response,False)   



if __name__ == '__main__':
    unittest.main()
