import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.prod_data_validation_helper import *
import logging

logger = logging.getLogger("cab.tests.ProductionTests")

class ProductionTests(unittest.TestCase):

 cnx = None

 # Test case : Find users who live in US
 def test_users_in_us(self):

     query = "Find users who visited kfc and lives in country US"
     logger.info("### Usecase:"+str(query)+" ###")
     count = segment_size_post_single_object("country","us",db_validation=False)
     verify_data_in_db_helper(count,"1",query)




if __name__ == '__main__':
    unittest.main()



