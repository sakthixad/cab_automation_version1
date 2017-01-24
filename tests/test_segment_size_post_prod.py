import unittest
from framework.helpers.segment_size_helper import *
import logging
import requests
import json

logger = logging.getLogger("cab.tests.segmentSizePostProdTests")

class SegmentSizePostProdTests(unittest.TestCase):

 cnx = None

 # # Find users who live in US and visited KFC
 # def test_users_in_usa_and_visited_kfc(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited KFC ###")
 #
 #    request = {
 #              "brand":{"direct":["1"]},
 #              "country":{"direct":["us"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited Walmart Supercenter
 # def test_users_in_usa_and_visited_walmart_supercenter(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited Walmart Supercenter ###")
 #
 #    request = {
 #              "brand":{"direct":["282"]},
 #              "country":{"direct":["us"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # Find users who live in US and belong to soccer moms
 def test_users_in_usa_and_soccer_moms(self):

    logger.info("### Usecase: Find users who live in US and belong to soccer moms ###")

    request = {
              "behavior":{"direct":["soccermoms"]},
              "country":{"direct":["us"]}
               }
    segment_size_post("AND",request)

 # # Find users who live in US and belong to Soccer Moms and who visited Target
 # def test_users_in_usa_and_soccer_moms_and_visted_target(self):
 #
 #    logger.info("### Usecase: Find users who live in US and belong to soccer moms and visted target ###")
 #
 #    request = {
 #              "behavior":{"direct":["soccermoms"]},
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["10"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and belong to frequent Travelers AND visited KFC
 # def test_users_in_usa_and_frequent_travellers_and_visted_kfc(self):
 #
 #    logger.info("### Usecase: Find users who live in US and belong to frequent travellers and visted kfc ###")
 #
 #    request = {
 #              "behavior":{"direct":["frequenttravelers"]},
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["1"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited KFC or visited Taco Bell
 # def test_users_in_usa_and_visited_kfc_or_taco(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited kfc or taco bell ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "OR":{"brand":["1","48"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited KFC and visited Taco Bell
 # def test_users_in_usa_and_visited_kfc_and_taco(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited kfc and taco bell ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "AND":{"brand":["1","48"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited KFC and visited Taco Bell and visited mcdonalds
 # def test_users_in_usa_and_visited_kfc_and_taco_and_mcdonalds(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited kfc and taco bell and mcdonalds ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "AND":{"brand":["1","48","25"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited target
 # def test_users_in_usa_and_visited_target(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited target ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["10"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited target and visited departmental stores
 # def test_users_in_usa_and_visited_target_and_visted_departmental_stores(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited target and visited departmental stores ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["10"]},
 #              "category":{"direct":["531102"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited Costco
 # def test_users_in_usa_and_visited_costco(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited Costco ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["32"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and visited Costco and visited target
 # def test_users_in_usa_and_visited_costco_and_target(self):
 #
 #    logger.info("### Usecase: Find users who live in US and visited Costco and Target ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "brand":{"direct":["32","10"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and belong to Soccer Moms but NOT visited Target
 # def test_users_in_usa_and_soccer_moms_and_not_visited_target(self):
 #
 #    logger.info("### Usecase: Find users who live in US and belong to Soccer Moms but NOT visited Target ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "behavior":{"direct":["soccermoms"]},
 #              "NOT":{"brands":["10"]}
 #               }
 #    segment_size_post("AND",request)
 #
 # # Find users who live in US and belong to Business Traveler but NOT visited KFC
 # def test_users_in_usa_and_frequent_travellers_and_not_visited_kfc(self):
 #
 #    logger.info("### Usecase: Find users who live in US and belong to frequent travellers but NOT visited kfc ###")
 #
 #    request = {
 #              "country":{"direct":["us"]},
 #              "behavior":{"direct":["frequenttravelers"]},
 #              "NOT":{"brands":["1"]}
 #               }
 #    segment_size_post("AND",request)
 #
 #
 # # Find users who live in US and belong to Soccer Moms OR who visited target
 # def test_users_in_usa_and_soccermoms_or_visited_target(self):
 #
 #    logger.info("### Usecase: Find users who live in US and belong to soccer moms or visited target ###")
 #
 #    request = {
 #                "type": "AND",
 #                "value": [
 #
 #                    {
 #                        "type": "country",
 #                        "value": "us"
 #                    },
 #
 #                    {
 #                        "type": "OR",
 #                        "value": [{
 #                            "type": "behavior",
 #                            "value": "soccermoms"
 #                        }, {
 #                            "type": "brand",
 #                            "value": {
 #                                "id": "10"
 #                            }
 #                        }]
 #
 #                    }
 #                ]
 #            }
 #
 #
 #    path = API_URL + "/segment_size?query="+str(json.dumps(request))
 #    logger.debug("Request Path: "+path)
 #    logger.debug("Request Body: " +json.dumps(request))
 #    response = requests.get(path)
 #
 #    logger.debug("Response Body: " + str(response.content))
 #    logger.debug("Response Code: " + str(response.status_code))























if __name__ == '__main__':
    unittest.main()