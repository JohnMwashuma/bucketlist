class BucketListClass(object):
    """ Bucket List CRUD methods implementation. """
    
    def __init__(self, bucket_activities = {}):
        """ A constructor method that initializes bucket list activities """       
        self.bucket_activities = bucket_activities
    
    def add_bucket_activities(self, title='', description='', bucket_activity_status=False, bucket_activity_progress=False):
        """ A Create function for creating new items in the bucket list """     
        self.bucket_activities.update({'title': title, 'description': description, 'bucket_activity_status':bucket_activity_status, 'bucket_activity_progress':bucket_activity_progress})

    def edit_bucket_activities(self, title=''):
        """ An update function for updating bucket list activities """     
        self.bucket_activities.update({title: title})
    
    def remove_bucket_activities(self, title=''):
        """ A function for deleting bucket activities """
        
        # Checks if the bucket list activity to be deleted is in the bucket list
        if title in self.bucket_activities:
            del self.bucket_activities[title] # Deletes the particular item from the bucket list

    def get_check_bucket_activities(self, title=''):
        """ Checks if the passed bucket list activity is in the bucket list """
        if title in self.bucket_activities:
            return True
        return False

     

    

        
            