import json
import unittest
from framework.helpers.segment_request_builder_helper import *
from framework.helpers.segment_sql_query_builder_helper import *
from framework.helpers.mysql_helper import *


class SampleTests(unittest.TestCase):

    cnx = None

    # def test_sample(self):
    #
    #     json_payload = {'segment': {'same': ['lowesCompetitor']},
    #                     'not':{'segment':['lowes']},
    #                     'or':{'age':['21','35']}}
    #
    #     json_payload1 = {'segment': {'same': ['lowesCompetitor']},
    #                     'not':{'segment':['lowes'],}}
    #
    #     json_payload2 = {'OR': {'brand': ['1','2']},
    #                     'not':{'brand':['lowes']},
    #                     'segment': {'same': ['lowesCompetitor']},
    #                     'or':{'age':['21','35']}
    #                      }
    #
    #     json_payload_nest = {
    #
    #        'behaviour': {'same': ['homeowners']},
    #         "brand":{"same":['1']}
    #
    #     }
    #
    #
    #
    #
    #     json_payload3 = {'OR': {'brand': ['1','2']}}
    #
    #     json_payload4 = {'segment': {'same': ['lowesCompetitor']},'brand':{'same':['12']},
    #                      'or':{'age':['21','35']},
    #                      'OR': {'brand': ['1','2']}}
    #
    #     request_string = json.dumps(json_payload4)
    #
    #     # Converting the json string to json
    #     req = json.loads(request_string)
    #
    #     payload = build_request_payload_segment_size("AND",req)
    #     print "****"
    #     print payload
    #
    #
    #
    #
    #     # Converting the json string to json
    #     request_string = json.dumps(json_payload_nest)
    #     req = json.loads(request_string)
    #     dict1 = {
    #         "type":"NOT",
    #         "value": build_request_payload_segment_size("OR",req)
    #     }
    #
    #     # request_string = json.dumps(payload)
    #     req = json.loads(payload)
    #     req['value'].append(dict1)
    #     print req
    #
    #
    #     # print "Final"
    #     # print req


    # def test_sql_query(self):
    #
    #     json_payload = {
    #
    #        # 'behaviour': {'same': ['homeowners']},
    #        'NOT':{'co':['us','gb','cn']}
    #
    #     }
    #
    #     pay1 = {
    #
    #
    #        'co':{'direct':['us','gb']}
    #
    #     }
    #
    #     pay3 = {
    #
    #
    #        'OR':{'co':['us','gb','cn']}
    #
    #     }
    #
    #     pay2 = {
    #
    #         "OR":{"co":["us","gb"]},
    #         "AND":{"b":["1","9"]},
    #         "is":{"direct":["0"]}}
    #
    #
    #     request_string = json.dumps(pay2)
    #
    #     # Converting the json string to json
    #     req = json.loads(request_string)
    #
    #     print segment_sql_query_builder("AND",req)



    def test_sql_connection(self):

        cnx = mysql_connect("xadcms")
        pay2 = {

            "OR":{"co":["us","gb"]},
            "AND":{"b":["1","9"]},
            "is":{"direct":["0"]}}


        request_string = json.dumps(pay2)

        # Converting the json string to json
        req = json.loads(request_string)
        query = segment_sql_query_builder("AND",req)
        print query

        # Get the result
        print get_result(cnx,query)
        mysql_close_connection(cnx)
    #
    # def test_token_converter(self):
    #
    #      pay2 = {
    #
    #                 "OR":{"segment":["us","gb"]},
    #                 "AND":{"brand":["1","9"]}
    #             }
    #
    #
    #      print token_converter_for_query_builder(pay2)


    def test_single_value(self):

        payload ={
            "country":{"single":{"us"}}
        }

        print







if __name__ == '__main__':
    unittest.main()

