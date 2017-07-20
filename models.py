class BucketList(object):
    """ Bucket List CRUD methods implementation. """
    
    def __init__(self):
        """ A constructor method that initializes bucket list activities """       
        self.bucket_list_activities = {}


    def add_bucket_list_activities(self, buckt_list_id=0,title='', description=''):
        """ A Create function for creating new items in the bucket list """     
        self.bucket_list_activities.update({buckt_list_id:buckt_list_id, title: title, description: description})

    def edit_bucket_list_activities(self, buckt_list_id=0, title='', description=''):
        """ An update function for updating bucket list activities """ 
        if buckt_list_id in self.bucket_list_activities:
            self.bucket_list_activities.update({ title: title, description: description})
    
    def delete_bucket_list_activities(self, buckt_list_id=0):
        """ A function for deleting bucket activities """
        
        # Checks if the bucket list activity to be deleted is in the bucket list
        if buckt_list_id in self.bucket_list_activities:
            del self.bucket_list_activities[buckt_list_id] # Deletes the particular item from the bucket list

    def check_bucket_list_activities(self, buckt_list_id):
        """ Checks if the passed bucket list activity is in the bucket list """
        if buckt_list_id in self.bucket_list_activities:
            return True
        return False

class User(object):
    """ This is the users class that inherits from the BucketListClass """

    def __init__(self):
        """ A constructor method that initializes all users """   
        self.users = {}
           
    def register_new_user(self, username='', password=''):
        """ A Create function for creating a new user """  
        if username in self.users:
            return 'The username already exsist, Please choose another.'
        elif len(password) < 4:
            return 'Password needs to be more than four characters'
        else:
            self.users[username]=password
                    
            

    def login_user(self,username='', password='', confirm_password=''):
        """ A login function for authenticating a user """     
        
        if username in self.users and  self.users[username] == password:
            return True
        elif username not in self.users:
            return False
        elif password != confirm_password:
            return False
        else:
            return False

    def lookup_user(self, username):
        """ Looks up for a particular user in a database """
        if username in self.users:
            return True
        return False

            
    
   


     

    

        
            