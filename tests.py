""" This is the testing file for all bucketlist routes and methods/functions """
import unittest
from bucketlist import app
import bucketlist

class RoutesTestCases(unittest.TestCase):
    """ Basic Routes test Cases """

    # Testing if our app has been loaded correctly
    def test_config_loading(self):
        """ Return okay if debug is set to true """
        assert app.config['DEBUG'] is True
        
    
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
    
    # Ensure that all_bucket_list_activitys template loads correctly    
    def test_index(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/index', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that bucket_list_form template loads correctly    
    def test_create_bucket_activity(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/create', content_type='html/text')
        self.assertEqual(responce.status_code, 200)   

    # Ensure that my_bucket_list_activitys template loads correctly    
    def test_my_bucket_list_activitys(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_bucket_list_activitys', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that my_public_bucket_activitys template loads correctly    
    def test_my_public_bucket_activitys(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_public_bucket_activitys', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that my_private_bucket_activitys template loads correctly    
    def test_my_private_bucket_activitys(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/my_private_bucket_activitys', content_type='html/text')
        self.assertEqual(responce.status_code, 200)
    
    # Ensure that Upadate Profile template loads correctly    
    def test_update_profile(self):
        """ Return a 200 http status code if the page loads correctly """
        tester = app.test_client(self)
        responce = tester.get('/profile', content_type='html/text')
        self.assertEqual(responce.status_code, 200)



class BucketlistTests(unittest.TestCase):
    """ These tests are for all crud operations methods """

     # Ensure that bucket_list_form template can redirect after a post request
    def test_create(self):
        """ Return a 200 http status code if the page redirects after a post request """
        tester = app.test_client(self)
        response = tester.post('/create', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Ensure the store bucket activity method is working correctly
    def test_store_bucket_list_activity(self):
        """ Test to see if add bucket activity functionality is working """
        
        bucketlist.store_bucket_list_activity('title', 'description', True, False)
        bucket_list_activities = bucketlist.get_bucket_list_activities(1)

        store_bucket_list_activity_works = False
        if bucket_list_activities:
            store_bucket_list_activity_works = True

        self.assertEqual(store_bucket_list_activity_works, True)          



if __name__ == '__main__':
    unittest.main()
