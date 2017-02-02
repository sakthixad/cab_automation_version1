import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_save_helper import *
import logging

logger = logging.getLogger("cab.tests.segmentSizePostTests")

class SegmentSizePostTests(unittest.TestCase):

     cnx = None

    #  ###################### Countries ################################
    #
    #  # Find users who live in country US
    #  def test_users_in_country_us(self):
    #
    #      logger.info("### Usecase: Find users who lives in USA ###")
    #      segment_size_post_single_object("country","us",db_validation=True)
    #
    #  # Find users who live in country Canada
    #  def test_users_in_country_cn(self):
    #
    #      logger.info("### Usecase: Find users who lives in Canada ###")
    #      segment_size_post_single_object("country","cn",db_validation=True)
    #
    #  # Find users who live in Great Britain
    #  def test_users_in_country_gb(self):
    #
    #      logger.info("### Usecase: Find users who lives in Great Britain ###")
    #      segment_size_post_single_object("country","gb",db_validation=True)
    #
    #
    #  ##################### States ######################################
    #
    #  # Find users who live in California
    #  def test_users_in_state_ca(self):
    #
    #      logger.info("### Usecase: Find users who lives in California ###")
    #      segment_size_post_single_object("state","ca",db_validation=True)
    #
    #  # Find users who live in Arizona
    #  def test_users_in_state_az(self):
    #
    #      logger.info("### Usecase: Find users who lives in Arizona ###")
    #      segment_size_post_single_object("state","az",db_validation=True)
    #
    #  # Find users who live in Arizona or in California
    #  def test_users_in_state_az_or_in_ca(self):
    #
    #      logger.info("### Usecase: Find users who lives in Arizona or in California ###")
    #      request = {
    #           "OR":{"state":["ca","az"]}
    #      }
    #
    #      segment_size_post("OR",request,db_validation=True)
    #
    #
    #  ##################### Dma ##########################################
    #
    #  # Find users who live in DMA "los angeles"
    #  def test_users_in_dma_los_angeles(self):
    #
    #      logger.info("### Usecase: Find users who lives in DMA - Los Angeles ###")
    #      segment_size_post_single_object("dma","803",db_validation=True)
    #
    #  # Find users who live in DMA "New york"
    #  def test_users_in_dma_new_york(self):
    #
    #      logger.info("### Usecase: Find users who lives in DMA - New York ###")
    #      segment_size_post_single_object("dma","501",db_validation=True)
    #
    #  # Find users who live in DMA "New york" or in DMA "los angeles"
    #  def test_users_in_dma_new_york_orlos_angeles(self):
    #
    #      logger.info("### Usecase: Find users who lives in DMA - New York or in Los Angeles ###")
    #      request = {
    #           "OR":{"dma":["501","803"]}
    #      }
    #
    #      segment_size_post("OR",request,db_validation=True)
    #
    #  ##################### Country and State ###########################
    #
    #  # Find users who lives in usa and in california
    #  def test_users_in_country_us_and_in_ca(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in California ###")
    #      request = {
    #           "state":{"direct":["ca"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who lives in usa and in california or in arizona
    #  def test_users_in_country_us_and_in_ca_or_in_az(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in California or in Arizona ###")
    #      request = {
    #           "OR":{"state":["ca","az"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #
    #  ##################### Country and Dma #############################
    #
    #  # Find users who lives in usa and in dma los angeles
    #  def test_users_in_country_us_and_in_dma_los_angeles(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in dma los angeles ###")
    #      request = {
    #           "dma":{"direct":["803"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who lives in usa and in dma los angeles or in dma new york
    #  def test_users_in_country_us_and_in_dma_los_angeles_or_in_dma_new_york(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in dma los angeles or in dma New York ###")
    #      request = {
    #           "OR":{"dma":["803","501"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #
    #  ##################### Country and State but not DMA ###########################
    #
    #  # Find users who lives in usa and in state ca but not in dma los angeles
    #  def test_users_in_country_us_and_in_state_ca_but_not_in_dma_los_angeles(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in state california but not in dma los angeles ###")
    #      request = {
    #           "NOT":{"dma":["803"]},
    #           "country":{"direct":["us"]},
    #           "state":{"direct":["ca"]}
    #      }
    #
    #      segment_save_post("AND",request)
    #
    #  # Find users who lives in usa and in state ca or in state arizona but not in dma los angeles
    #  def test_users_in_country_us_and_in_state_ca_and_in_az_but_not_in_dma_los_angeles(self):
    #
    #      logger.info("### Usecase: Find users who lives in usa and in state california and in state texas but not in dma los angeles ###")
    #      request = {
    #           "NOT":{"dma":["803"]},
    #           "country":{"direct":["us"]},
    #           "OR":{"state":["ca","az"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #
    #  ##################### Brands and Country #######################
    #
    #  #Usecase: Find users who visited kfc and lives in country us
    #  def test_brands_country_comb(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc and lives in country US ###")
    #      request = {
    #           "brand":{"direct":[1]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who visited kfc or mcdonalds and lives in country us
    #  def test_brands_or_combination(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc or mcdonalds and lives in country US ###")
    #      request = {
    #           "OR":{"brand":[1,25]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who visited kfc and mcdonalds and lives in country us
    #  def test_brands_and_combination(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc and mcdonalds and lives in country US ###")
    #      request = {
    #           "AND":{"brand":[1,25]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    # #Usecase: Find users who visited kfc and mcdonalds but not tacobell and lives in country us
    #  def test_brands_and_not_combination(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc and mcdonalds but not tacobell and lives in country US ###")
    #      request = {
    #           "AND":{"brand":[1,25]},
    #           "country":{"direct":["us"]},
    #           "NOT":{"brand":[48]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who visited kfc or mcdonalds but not taco bell and lives in country us
    #  def test_brands_or_not_combination(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc or mcdonalds but not taco bell and lives in country US ###")
    #      request = {
    #           "OR":{"brand":[1,25]},
    #           "country":{"direct":["us"]},
    #           "NOT":{"brand":[48]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who visited kfc but not mcdonalds and lives in country us
    #  def test_brands_not_combination(self):
    #
    #      logger.info("### Usecase: Find users who visited kfc but not mcdonalds and lives in country US ###")
    #      request = {
    #           "brand":{"direct":[1]},
    #           "NOT":{"brand":[25]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #
    #  ##################### Categories and Country #######################
    #
    #  #Usecase: Find users who belong to category departmental stores lives in country us
    #  def test_categories_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to category departmental stores lives in country US ###")
    #      request = {
    #           "AND":{"category":["l:531102"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to category departmental stores and restaurants and lives in country us
    #  def test_categories_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to category departmental stores and restaurants and lives in country US ###")
    #      request = {
    #           "AND":{"category":["l:531102","l:581208"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to category restaurants or department stores and lives in country us
    #  def test_category_or_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to category restaurants or department stores and lives in country US ###")
    #      request = {
    #           "OR":{"category":["l:531102","l:581208"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to category restaurants but not department stores and lives in country us
    #  def test_categories_not_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to category restaurants but not department stores and lives in country US ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "NOT":{"category":["l:531102"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to category restaurants and department stores but not movie theaters and lives in country us
    #  def test_categories_and_not_combination(self):
    #
    #      logger.info("### Usecase:  Find users who belong to category restaurants and department stores but not movie theaters and lives in country us ###")
    #      request = {
    #           "AND":{"category":["l:531102","l:581208"]},
    #           "NOT":{"category":["l:783201"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to category restaurants or department stores but not movie theaters and lives in country us
    #  def test_categories_or_not_combination(self):
    #
    #      logger.info("### Usecase:  Find users who belong to category restaurants or department stores but not movie theaters and lives in country us ###")
    #      request = {
    #           "AND":{"category":["l:531102","l:581208"]},
    #           "NOT":{"category":["l:783201"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  ##################### Brands and Categories and Country #######################
    #
    #  # Find users who live in us and visited kfc and belong to category restaurants
    #  def test_brand_kfc_country_us_and_categ_department_stores(self):
    #      logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and lives in country us ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "brand":{"direct":[1]},
    #           "country":{"direct":["1"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who live in us and visited kfc and mcdonalds and belong to category restaurants
    #  def test_brand_kfc_and_mcdonald_country_us_and_categ_department_stores(self):
    #      logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and mcdonalds and lives in country us ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "AND":{"brand":[1,25]},
    #           "country":{"direct":["1"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who live in us and visited kfc and mcdonalds but not visit taco bell and belong to category restaurants
    #  def test_brand_kfc_and_mcdonald_not_taco_country_us_and_categ_department_stores(self):
    #      logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc and mcdonalds but not taco bell and lives in country us ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "AND":{"brand":[1,25]},
    #           "country":{"direct":["1"]},
    #           "NOT":{"brand":[48]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who live in us and visited kfc or mcdonalds and belong to category restaurants
    #  def test_brand_kfc_or_mcdonald_country_us_and_categ_department_stores(self):
    #      logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc or mcdonalds and lives in country us ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "OR":{"brand":[1,25]},
    #           "country":{"direct":["1"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  # Find users who live in us and visited kfc or mcdonalds and belong to category restaurants but not visit taco bell
    #  def test_brand_kfc_or_mcdonald_not_taco_country_us_and_categ_department_stores(self):
    #      logger.info("### Usecase:  Find users who belong to category restaurants and visited brands kfc or mcdonalds but not taco and lives in country us ###")
    #      request = {
    #           "category":{"direct":["l:581208"]},
    #           "OR":{"brand":[1,25]},
    #           "country":{"direct":["1"]},
    #           "NOT":{"brand":[48]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  ##################### Behavioural Audiences and Country #######################
    #
    #  #Usecase: Find users who belong to behavioural audiences soccer moms and lives in country us
    #  def test_behavioural_audiences_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and lives in country us ###")
    #      request = {
    #           "behavior":{"direct":["soccermoms"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to behavioural audiences soccer moms and dad and lives in country us
    #  def test_behavioural_audiences_soccer_moms_and_dad_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and dad and lives in country us ###")
    #      request = {
    #           "AND":{"behavior":["soccermoms","dad"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to behavioural audiences soccer moms or dad and lives in country us
    #  def test_behavioural_audiences_soccer_moms_or_dad_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms or dad and lives in country us ###")
    #      request = {
    #           "OR":{"behavior":["soccermoms","dad"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who belong to behavioural audiences soccer moms and not dads and lives in country us
    #  def test_behavioural_audiences_and_country_combination(self):
    #
    #      logger.info("### Usecase: Find users who belong to behavioural audiences soccer moms and not dads and lives in country us ###")
    #      request = {
    #           "behavior":{"direct":["soccermoms"]},
    #           "country":{"direct":["us"]},
    #           "NOT":{"behavior":["dad"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #
    #  ##################### Gender and Country #######################
    #
    #  #Usecase: Find users of gender male and lives in country us
    #  def test_gender_male_and_country(self):
    #
    #      logger.info("### Usecase:  Find users of gender male and lives in country us ###")
    #      request = {
    #           "gender":{"direct":["m"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=False)
    #
    #      logger.debug("SQl Query Result: "+str(user_count_by_gender("m")))
    #
    #  #Usecase: Find users of gender female and lives in country us
    #  def test_gender_female_and_country(self):
    #
    #      logger.info("### Usecase:  Find users of gender female and lives in country us ###")
    #      request = {
    #           "gender":{"direct":["f"]},
    #           "country":{"direct":["us"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=False)
    #      logger.debug("SQl Query Result: "+str(user_count_by_gender("f")))
    #
    #
    #
    #  ##################### Custom Audiences and Country #######################
    #
    #  #Usecase: Find users who live in country US and belong to custom audience seg1='94167'
    #  def test_country_and_segments(self):
    #
    #      logger.info("### Usecase:  Find users who live in country US and belong to custom audience seg1='94167' ###")
    #      request = {
    #           "country":{"direct":["us"]},
    #           "segment":{"direct":["94167"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who live in country US and belong to custom audience seg1='94167' or seg='93767'
    #  def test_country_and_segments_with_or(self):
    #
    #      logger.info("### Usecase:Find users who live in country US and belong to custom audience seg1='94167' or seg='93767 ###")
    #      request = {
    #           "country":{"direct":["us"]},
    #           "OR":{"segment":["94167","93767"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)
    #
    #  #Usecase: Find users who live in country US and belong to custom audience seg1='94167' and not seg='93767'
    #  def test_country_and_segments_with_and_not(self):
    #
    #      logger.info("### Usecase:Find users who live in country US and belong to custom audience seg1='94167' and not seg='93767' ###")
    #      request = {
    #           "country":{"direct":["us"]},
    #           "segment":{"direct":["94167"]},
    #           "NOT":{"segment":["93767"]}
    #      }
    #
    #      segment_size_post("AND",request,db_validation=True)



     ################################### Age ######################################

     def test_age_less_than_25(self):

        logger.info("### Usecase: Find users who lives in USA ###")
        # segment_size_post_single_object("age",1,db_validation=False)
        segment_size_post_single_object("age",1,db_validation=False)
        print user_count_age(2007,1)

     # def test_minus(self):
     #
     #     a = 187728368
     #     b = 173299389
     #
     #     print a-b


     # def test_age_less_than_18(self):
     #
     # def test_age_less_than_25(self):
     #
     # def test_age_less_than_35(self):






if __name__ == '__main__':
    unittest.main()
