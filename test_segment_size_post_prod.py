import unittest
from framework.helpers.segment_size_helper import *
import logging
import requests
import json
from framework.helpers.segment_save_helper import *

logger = logging.getLogger("cab.tests.SegmentSizeProductTestCases")

class SegmentSizeProductTestCases(unittest.TestCase):

 cnx = None

# #  # # Find users who live in US and visited KFC
# #  # def test_users_in_usa_and_visited_kfc(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited KFC ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["1"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited mcdonalds
# #  # def test_users_in_usa_and_visited_mcdonalds(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Mcdonalds ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["25"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited taco bell
# #  # def test_users_in_usa_and_visited_taco_bell(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Taco bell ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["48"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited Walmart Supercenter
# #  # def test_users_in_usa_and_visited_walmart_supercenter(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Walmart Supercenter ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["282"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and belong to soccer moms
# #  # def test_users_in_usa_and_soccer_moms(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to soccer moms ###")
# #  #
# #  #    request = {
# #  #              "behavior":{"direct":["soccermoms"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and belong to soccer moms and of gender male
# #  # def test_users_in_usa_and_soccer_moms_and_gender_male(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to soccer moms and gender male###")
# #  #
# #  #    request = {
# #  #              "behavior":{"direct":["soccermoms"]},
# #  #              "country":{"direct":["us"]},
# #  #              "gender":{"direct":["m"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # #Find users who live in US and belong to soccer moms and of gender female
# #  # def test_users_in_usa_and_soccer_moms_and_gender_male(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to soccer moms and gender female###")
# #  #
# #  #    request = {
# #  #              "behavior":{"direct":["soccermoms"]},
# #  #              "country":{"direct":["us"]},
# #  #              "gender":{"direct":["f"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #
# #  # #Find users who live in US and belong to soccer moms and dad
# #  # def test_users_in_usa_and_soccer_moms_and_dad(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to soccer moms and dad###")
# #  #
# #  #    request = {
# #  #              "AND":{"behavior":["soccermoms","dad"]},
# #  #              "country":{"direct":["us"]},
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #
# #  # # Find users who live in US and visited Home Depot
# #  # def test_users_in_usa_and_visited_home_depot(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Home Depot ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["8"]},
# #  #              "country":{"direct":["us"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited Home Depot and of gender male
# #  # def test_users_in_usa_and_visited_home_depot_and_gender_male(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Home Depot and gender male ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["8"]},
# #  #              "country":{"direct":["us"]},
# #  #              "gender":{"direct":["m"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited Home Depot and of gender female
# #  # def test_users_in_usa_and_visited_home_depot_and_gender_female(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Home Depot and gender female ###")
# #  #
# #  #    request = {
# #  #              "brand":{"direct":["8"]},
# #  #              "country":{"direct":["us"]},
# #  #              "gender":{"direct":["f"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #
# #
# #
# #
# #
# #  # # Find users who live in US and belong to Soccer Moms and who visited Target
# #  # def test_users_in_usa_and_soccer_moms_and_visted_target(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to soccer moms and visted target ###")
# #  #
# #  #    request = {
# #  #              "behavior":{"direct":["soccermoms"]},
# #  #              "country":{"direct":["us"]},
# #  #              "brand":{"direct":["10"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #
# #  # # Find users who live in US and belong to frequent Travelers AND visited KFC
# #  # def test_users_in_usa_and_frequent_travellers_and_visited_kfc(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to frequent travellers and visited kfc ###")
# #  #
# #  #    request = {
# #  #              "behavior":{"direct":["frequenttravelers"]},
# #  #              "country":{"direct":["us"]},
# #  #              "brand":{"direct":["1"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited KFC or visited Taco Bell
# #  # def test_users_in_usa_and_visited_kfc_or_taco(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited kfc or taco bell ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "OR":{"brand":["1","48"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited KFC and visited Taco Bell
# #  # def test_users_in_usa_and_visited_kfc_and_taco(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited kfc and taco bell ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "AND":{"brand":[1,48]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited KFC and visited Taco Bell and visited mcdonalds
# #  # def test_users_in_usa_and_visited_kfc_and_taco_and_mcdonalds(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited kfc and taco bell and mcdonalds ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "AND":{"brand":["1","48","25"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited target
# #  # def test_users_in_usa_and_visited_target(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited target ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "brand":{"direct":["10"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited target and visited departmental stores
# #  # def test_users_in_usa_and_visited_target_and_visted_departmental_stores(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited target and visited departmental stores ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "brand":{"direct":["10"]},
# #  #              "category":{"direct":["l:531102"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited Costco
# #  # def test_users_in_usa_and_visited_costco(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Costco ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "brand":{"direct":["32"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # # Find users who live in US and visited Costco and visited target
# #  # def test_users_in_usa_and_visited_costco_and_target(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and visited Costco and Target ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "AND":{"brand":["32","10"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #
# #  # # Find users who live in US and belong to Soccer Moms but NOT visited Target
# #  # def test_users_in_usa_and_soccer_moms_and_not_visited_target(self):
# #  #
# #  #    logger.info("### Usecase: Find users who live in US and belong to Soccer Moms but NOT visited Target ###")
# #  #
# #  #    request = {
# #  #              "country":{"direct":["us"]},
# #  #              "behavior":{"direct":["soccermoms"]},
# #  #              "NOT":{"brand":["10"]}
# #  #               }
# #  #    segment_size_post("AND",request,db_validation=False)
# #  #
# #  # Find users who live in US and belong to Frequent Traveler but NOT visited KFC
# #  def test_users_in_usa_and_frequent_travellers_and_not_visited_kfc(self):
# #
# #     logger.info("### Usecase: Find users who live in US and belong to frequent travellers but NOT visited kfc ###")
# #
# #     request = {
# #               "country":{"direct":["us"]},
# #               "behavior":{"direct":["frequenttravelers"]},
# #               "NOT":{"brand":["1"]}
# #                }
# #     segment_size_post("AND",request,db_validation=False)
# #
#  # # Find users who live in US and belong to business Traveler but NOT visited KFC
#  # def test_users_in_usa_and_business_travellers_and_not_visited_kfc(self):
#  #
#  #    logger.info("### Usecase: Find users who live in US and belong to business travellers but NOT visited kfc ###")
#  #
#  #    request = {
#  #              "country":{"direct":["us"]},
#  #              "behavior":{"direct":["bt"]},
#  #              "NOT":{"brand":["1"]}
#  #               }
#  #    segment_size_post("AND",request,db_validation=False)
#  #
#  #  # Find users who live in US and belong to business Traveler but NOT visited KFC
#  # def test_users_in_usa_and_business_travellers_and_visited_kfc(self):
#  #
#  #    logger.info("### Usecase: Find users who live in US and belong to business travellers but NOT visited kfc ###")
#  #
#  #    request = {
#  #              "country":{"direct":["us"]},
#  #              "behavior":{"direct":["bt"]},
#  #              "brand":{"direct":["1"]}
#  #               }
#  #    segment_size_post("AND",request,db_validation=False)
#  #
# #
#  Find users who live in US and belong to Soccer Moms OR who visited target
#  def test_users_in_usa_and_soccermoms_or_visited_target(self):
#
#     logger.info("### Usecase: Find users who live in US and belong to soccer moms or visited target ###")
#
#     request = {
#                 "type": "OR",
#                 "value": [
#
#                     {
#                         "type": "country",
#                         "value": "us"
#                     },
#                     {
#                         "type": "country",
#                         "value": "de"
#                     },
#                     {
#                         "type": "country",
#                         "value": "in"
#                     },
#                     {
#                         "type": "country",
#                         "value": "fr"
#                     },
#                     {
#                         "type": "country",
#                         "value": "cn"
#                     },
#                     {
#                         "type": "country",
#                         "value": "gb"
#                     },
#                     {
#                         "type": "country",
#                         "value": "jp"
#                     },
#                     {
#                         "type": "country",
#                         "value": "es"
#                     },
#                     {
#                         "type": "country",
#                         "value": "ca"
#                     },
#                     {
#                         "type": "country",
#                         "value": "it"
#                     },
#                     {
#                         "type": "country",
#                         "value": "au"
#                     }
#
#                 ]
#             }
#
#
#     path = API_URL + "/segment_size?query="+str(json.dumps(request))
#     logger.debug("Request Path: "+path)
#     logger.debug("Request Body: " +json.dumps(request))
#     response = requests.get(path)
#
#     logger.debug("Response Body: " + str(response.content))
#     logger.debug("Response Code: " + str(response.status_code))
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #  # # 961522638
# #  #
# #  # # 14428979
#  def test_users_who_dont_have_countries(self):
#
#     # # request = {
#     # #           "OR":{"country":["us","de","in","fr","cn","gb","jp","es","ca","it","au","mx","nl","at","be","ch","dk","fi","lu","no","se","nz"]}
#     # #            }
#     # #
#     # request = {"type": "OR", "value": [{"type": "country", "value": "us"}, {"type": "country", "value": "de"}, {"type": "country", "value": "in"}, {"type": "country", "value": "fr"}, {"type": "country", "value": "cn"}, {"type": "country", "value": "gb"}, {"type": "country", "value": "jp"}, {"type": "country", "value": "es"}, {"type": "country", "value": "ca"}, {"type": "country", "value": "it"}, {"type": "country", "value": "au"}, {"type": "country", "value": "mx"}, {"type": "country", "value": "nl"}, {"type": "country", "value": "at"}, {"type": "country", "value": "be"}, {"type": "country", "value": "ch"}, {"type": "country", "value": "dk"}, {"type": "country", "value": "fi"}, {"type": "country", "value": "lu"}, {"type": "country", "value": "no"}, {"type": "country", "value": "se"}, {"type": "country", "value": "nz"}]}
#     #
#     # path = API_URL + "/segment_save?query="+json.dumps(request)+"&segment_md5=1003"
#     # logger.debug("Request Path: "+path)
#     # logger.debug("Request Body: " +json.dumps(request))
#     # response = requests.get(path)
#     #
#     # logger.debug("Response Body: " + str(response.content))
#     # logger.debug("Response Code: " + str(response.status_code))
#
#     num1= 1222122387
#     num2= 1103900291
#
#     print num1-num2


# #  # 1222122387 # 1103900291
#  def test_users_who_dont_have_countries(self):
#
#     request = {
#               "country":{"direct":["us"]},
#               "NOT":{"country":["us"]}
#                }
#     segment_save_post("OR",request,db_validation=False)


# #  # def test_users_who_dont_have_countries(self):
# #  #
# #  #
# #  #    segment_size_post_single_object("country","fr",db_validation=False)
# #
# #
#  def test_users_in_usa_and_ca_or_ny_(self):
#
#         logger.info("### Usecase: Find users who live in US and visited walmart and visited restaurants and golfers ###")
#
#         request = {
#                 "type": "AND",
#                 "value": [{
#                     "type": "country",
#                     "value": "us"
#                 }, {
#                     "type": "OR",
#                     "value": [{
#                         "type": "brand",
#                         "value": {
#                             "id": 9
#                         }
#                     }, {
#                         "type": "behavior",
#                         "value": "go"
#                     },
#                         {
#                         "type": "category",
#                         "value": {
#                             "id": "581208"
#                         }
#                     }
#                         ]
#                 }
#             ]
#             }
#
#         path = API_URL + "/segment_size?query="+str(json.dumps(request))
#         logger.debug("Request Path: "+path)
#         logger.debug("Request Body: " +json.dumps(request))
#         response = requests.get(path)
#
#         logger.debug("Response Body: " + str(response.content))
#         logger.debug("Response Code: " + str(response.status_code))

 # def test_users_in_usa_and_visited_walmart_and_restaurants_golfers(self):
 #
 #        logger.info("### Usecase: Find users who live in US and visited walmart and visited restaurants and golfers ###")
 #
 #        request = {
 #                "type": "AND",
 #                "value": [{
 #                    "type": "country",
 #                    "value": "us"
 #                }, {
 #                    "type": "AND",
 #                    "value": [{
 #                        "type": "brand",
 #                        "value": {
 #                            "id": 9
 #                        }
 #                    }, {
 #                        "type": "behavior",
 #                        "value": "go"
 #                    },
 #                        {
 #                        "type": "category",
 #                        "value": {
 #                            "id": "458106"
 #                        }
 #                    }
 #                        ]
 #                },
 #                    {
 #                        "type": "state",
 #                        "value": "ca"
 #                    },
 #                    {
 #                        "type" :"NOT",
 #                        "value" :{"type":"dma","value":803}
 #                    },
 #
 #                    {
 #                        "type":"gender",
 #                        "value":"m"
 #                    },
 #                    {
 #                        "type":"segment",
 #                        "value":"336555"
 #                    },
 #
 #                    {
 #                        "type":"AND","value":[{ "type": "NOT","value" :{"type":"brand","value":{"id": 10}}},
 #                                              { "type": "NOT","value" :{"type":"behavior","value":"bt"}}]
 #
 #
 #                    },
 #                    {
 #                        "type": "OR",
 #                        "value":[{"type":"age","value":2},{"type": "age","value": 3}]
 #                    },
 #                {
 #                        "type" :"NOT",
 #                        "value" :{"type":"segment","value":336560}
 #                    }]
 #            }
 #
 #        # request = {
        #         "type": "AND",
        #         "value": [{
        #             "type": "country",
        #             "value": "us"
        #         }, {
        #             "type": "OR",
        #             "value": [{
        #                 "type": "category",
        #                 "value": {
        #                     "id": "581208"
        #                 }
        #             }, {
        #                 "type": "brand",
        #                 "value": {
        #                     "id": 9
        #                 }
        #             }, {
        #                 "type": "behavior",
        #                 "value": "go"
        #             },
        #                 ]
        #         },
        #             {
        #                 "type": "state",
        #                 "value": "ca"
        #             },
        #             {
        #                 "type" :"NOT",
        #                 "value" :{"type":"dma","value":803}
        #             },
        #                     {
        #                 "type":"AND","value":[{ "type": "NOT","value" :{"type":"brand","value":{"id": 10}}},
        #                                       { "type": "NOT","value" :{"type":"behavior","value":"bt"}}]
        #
        #
        #             }
        #             ,
        #
        #             {
        #                 "type":"gender",
        #                 "value":"m"
        #             },
        #
        #             {
        #                 "type": "OR",
        #                 "value":[{"type":"age","value":2},{"type": "age","value": 3}]
        #             }]
        #     }
        #
        # path = API_URL + "/segment_size?query="+str(json.dumps(request))
        # logger.debug("Request Path: "+path)
        # logger.debug("Request Body: " +json.dumps(request))
        # response = requests.get(path)
        #
        # logger.debug("Response Body: " + str(response.content))
        # logger.debug("Response Code: " + str(response.status_code))

#  def test_users_in_usa_and_state_california_or_texas_or_dma_austin(self):
#
#         logger.info("### Usecase: Find users in usa and state california or in state texas or in dma austin ###")
#
#         # request = {
#         #         "type": "AND",
#         #         "value": [
# 			# 	  {"type": "country","value": "us"},
# 			# 	  {"type": "OR", "value": [{"type":"dma","value":635},
# 			# 							   {"type":"OR","value":[{"type":"state","value":"ca"},{"type":"state","value":"ny"}]}] }
# 			# 	]
#         #         }
#
#         request = {
#                 "type": "AND",
#                 "value": [
# 				  {"type": "country","value": "us"},
# 				  {"type": "OR", "value": [{"type":"dma","value":635},
# 										   {"type":"OR","value":[{"type":"state","value":"ca"},{"type":"state","value":"ny"}]}] },
#                     {"type": "NOT","value":{"type":"dma","value":803}}
# 				]
#                 }
#
#         path = API_URL + "/segment_size?query="+str(json.dumps(request))
#         logger.debug("Request Path: "+path)
#         logger.debug("Request Body: " +json.dumps(request))
#         response = requests.get(path)
#
#         logger.debug("Response Body: " + str(response.content))
#         logger.debug("Response Code: " + str(response.status_code))
# # #
 # def test_state_ca_ny_hampshire_not_dmas(self):
 #        logger.info("### Usecase: Find users who live in US and visited ca,ny ###")
 #
 #        request = {
 #                        "type": "AND",
 #                        "value": [
 #                          {"type": "country","value": "us"},
 #                          {"type": "OR","value": [{"type": "state","value": "ca"},
 #                                                  {"type": "state","value": "mn"},
 #                                                  {"type": "state","value": "ny"}
 #                                                 ]
 #                          },
 #                          {
 #                           "type": "OR","value": [{"type": "NOT","value": {"type": "dma","value": 803}},
 #                                                  {"type": "NOT","value": {"type": "dma","value": 613}}]
 #
 #                          }
 #
 #                          ]
 #                    }
 #
 #        path = API_URL + "/segment_size?query="+str(json.dumps(request))
 #        logger.debug("Request Path: "+path)
 #        logger.debug("Request Body: " +json.dumps(request))
 #        response = requests.get(path)
 #
 #        logger.debug("Response Body: " + str(response.content))
 #        logger.debug("Response Code: " + str(response.status_code))



#
#
#
#
 # Usecase: Find users who live in country US and belong to custom audience seg1='94167' or seg='93767'
 def test_country_and_segments_with_and(self):

     logger.info("### Usecase:Find users who live in country US and belong to custom audience seg1='94167' or seg='93767 ###")
     request = {
          "OR":{"segment":["202551","214996"]},
          "country":{"direct":["us"]},
          "NOT":{"segment":["330465"]},
          "segment":{"direct":["336555"]}

     }

     segment_size_post("AND",request,db_validation=True)






if __name__ == '__main__':
    unittest.main()