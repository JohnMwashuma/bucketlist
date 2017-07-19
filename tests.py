""" This is the testing file for all bucket routes and methods/functions """
import unittest
from bucketlist import app
import crud
import bucketlist

class RoutesTestCases(unittest.TestCase):
    """ Basic Routes test Cases """       
    
    # Ensure that Login template loads correctly    
    def test_login(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/login', content_type='html/text')
        self.assertEqual(responce.status_code, 200)

     # Ensure that Sign Up template loads correctly    
    def test_signup(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/signup', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that all_bucket_activities template loads correctly    
    def test_index(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/index', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that bucket_activity_form template loads correctly    
    def test_create_bucket_activity(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/create', content_type='html/text')
        self.assertEqual(responce.status_code, 200)   

    # Ensure that my_bucket_activities template loads correctly    
    def test_my_bucket_activities(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_bucket_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that my_public_bucket_activities template loads correctly    
    def test_my_public_bucket_activities(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_public_bucket_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that my_private_bucket_activitys template loads correctly    
    def test_my_private_bucket_activitys(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_private_bucket_activities', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that Upadate Profile template loads correctly    
    def test_update_profile(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/profile', content_type='html/text')
        self.assertEqual(responce.status_code, 200)



class BucketlistTests(unittest.TestCase):
    """ These tests are for all crud operations methods """

    # Ensure the store bucket_activities method is working correctly
    def test_add_bucket_activities(self):
        """ Test to see if add bucket activity functionality is working """
        bucket_list = crud.BucketListClass()
        bucket_list.add_bucket_activities('title', 'description', True, False)  

        confirm_added_bucket_activity = bucket_list.get_check_bucket_activities('title')
        
        store_bucket_activity_works = False
        if confirm_added_bucket_activity == True:
            store_bucket_activity_works = True

        self.assertEqual(store_bucket_activity_works, True)          

    
    # Ensure the remove bucket_activities method is working correctly
    def test_remove_bucket_activities(self):
        """ Test to see if add bucket activity functionality is working """
        bucket_list = crud.BucketListClass()
        bucket_list.add_bucket_activities('title', 'description', True, False)  
        
        bucket_list.remove_bucket_activities('title')

        confirm_removed_bucket_activity = bucket_list.get_check_bucket_activities('title')
        
        remove_bucket_activity_works = False
        if confirm_removed_bucket_activity == False:
            remove_bucket_activity_works = True

        self.assertEqual(remove_bucket_activity_works, True) 

    # Ensure the edit bucket_activities method is working correctly
    def test_edit_bucket_activities(self):
        """ Test to see if add bucket activity functionality is working """
        bucket_list = crud.BucketListClass()
        bucket_list.add_bucket_activities('title', 'description', True, False)  
        
        bucket_list.edit_bucket_activities('Andela')

        confirm_update = bucket_list.get_check_bucket_activities('Andela')
        
        update_bucket_activity_works = False
        if confirm_update == True:
            update_bucket_activity_works = True

        self.assertEqual(update_bucket_activity_works, True) 

if __name__ == '__main__':
    unittest.main()
