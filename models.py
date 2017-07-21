""" All CRUD implementation classes """

from datetime import datetime

class BucketList(object):
    """ Bucket list CRUD methods """
    
    def __init__(self, bucket_list = []):
        """ A constructor method that initializes the bucket list """  

        self.bucket_list = bucket_list



    def create_bucket_list(self,user,bucket_list_id,bucket_list_name):
        """ Create bucket List method """  

        self.bucket_list.append(dict(
            bucket_list_id= bucket_list_id,
            bucket_list_name=bucket_list_name,
            user= user,            
            date=datetime.utcnow
            ))  



    def edit_bucket_list(self,bucket_list_id,bucket_list_name):
        """ Bucket list edit method """  

        # Find the bucket list id index and deleting it.
        bucket_activity_index = next(index for (index, d) in enumerate(self.bucket_list)if d["bucket_list_id"] == bucket_list_id)       
        bucket_list_activity = self.bucket_list[bucket_activity_index]["bucket_list_name"]=bucket_list_name        
        return bucket_list_activity



    def delete_bucket_list(self,bucket_list_id):        
        """ A function for deleting a bucket list """ 

        # Find the bucket list id index and delete it
        bucket_list_index = next(index for (index, d) in enumerate(self.bucket_list) if d["bucket_list_id"] == bucket_list_id)
        del self.bucket_list[bucket_list_index]  



    def check_bucket_lists(self, bucket_list_id):
        """ Checks if the passed bucket list activity is in the bucket list """
        for t in self.bucket_list:
            if t['bucket_list_id'] == bucket_list_id:
                return True
            else:
                return False   



class BucketlistActivities(object):
    """ Bucket list Activities CRUD methods """

    def __init__(self, bucket_list_activities = []):
        """ A constructor method that initializes bucket list activities """  

        self.bucket_list_activities = bucket_list_activities 



    def create_bucket_list_activities(self,user,bucket_list_activity_id,title, description,bucket_list_name=''):
        """ Appends a bucket_activity property to the bucket_list_activities variable """  
        self.bucket_list_activities.append(dict(
            bucket_list_activity_id= bucket_list_activity_id,
            bucket_list_name=bucket_list_name,
            title=title,
            user= user,
            description=description,            
            date=datetime.utcnow()
            ))



    def get_bucket_list_activities(self,num):
        """ Returns sorted bucket activities by date created in terms of the latest bucket list activities """

        return sorted(self.bucket_list_activities, key=lambda bm: bm['date'], reverse=True)[:num]



    def get_bucket_list_activity(self,bucket_list_activity_id):
        """ Returns the bucket list activities by based on the bucket_list_activity_id given """

        bucket_list_activity_index = next(index for (index, d) in enumerate(self.bucket_list_activities) if d["bucket_list_activity_id"] == bucket_list_activity_id)
        bucket_list_activity = self.bucket_list_activities[bucket_list_activity_index]
        return bucket_list_activity


    
    def edit_bucket_list_activities(self,bucket_list_activity_id, title='', bucket_list_name='', description=''):
        """ An update function for updating bucket list activities """ 

        bucket_list_activity_index = next(index for (index, d) in enumerate(self.bucket_list_activities)if d["bucket_list_activity_id"] == bucket_list_activity_id)       
        
        for bucket_list_activity in self.bucket_list_activities:
            if bucket_list_activity['bucket_list_activity_id'] == bucket_list_activity_id:
                self.bucket_list_activities[bucket_list_activity_index]["title"]=title 
                self.bucket_list_activities[bucket_list_activity_index]["description"]=description
                self.bucket_list_activities[bucket_list_activity_index]["bucket_list_name"]=bucket_list_name


        
    def delete_bucket_list_activities(self, bucket_list_activity_id):
        """ A function for deleting bucket list activities """ 
               
        # Find the bucket_list_activity_id index and delete it
        bucket_list_activity_index = next(index for (index, d) in enumerate(self.bucket_list_activities) if d["bucket_list_activity_id"] == bucket_list_activity_id)
        del self.bucket_list_activities[bucket_list_activity_index]
                
            

    def check_bucket_list_activities(self, bucket_list_activity_id):
        """ Checks if the bucket list activity passed is in the bucket list """

        for t in self.bucket_list_activities:
            if t['bucket_list_activity_id'] == bucket_list_activity_id:
                return True
            else:
                return False



class User(object):
    """ Users CRUD methods implementation """

    def __init__(self, users={}):
        """ A constructor method that initializes all users """

        self.users = users


           
    def register_new_user(self, username='', password='', confirm_password=''):
        """ A Create function for creating a new user """ 
         
        if username in self.users:
            return 'The username already exsist, Please choose another.'
        elif len(password) < 4:
            return 'Password needs to be more than four characters'
        elif password != confirm_password:
            return 'The Passwords Entered do not match'
        else:
            self.users[username]=password
                    
            

    def login_user(self,username='', password=''):
        """ A login function for authenticating users """     
        
        if username in self.users and  self.users[username] == password:
            return True
        elif username not in self.users:
            return False        
        else:
            return False



    def lookup_user(self, username):
        """ Looks up for a particular user in the dictionary """

        if username in self.users:
            return True
        return False

            
    
   


     

    

        
            