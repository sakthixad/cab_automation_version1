from config import API_URL
from framework.helpers.segment_sql_query_builder_helper import *
from framework.helpers.segment_request_builder_helper import *
import requests
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger = logging.getLogger("cab.helpers.segmentsizehelper")

def segment_size_post(main_type,generic_input_dict,db_validation):

    cnx = mysql_connect("test_cab")

    request_obj = build_request_payload_segment_size(main_type,generic_input_dict)
    path = API_URL + "/segment_size?query="+str(request_obj)

    logger.debug("Request Path: "+path)

    if request_obj is not None:
        logger.debug("Request Body: " +request_obj)

        response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))

    if response.status_code is 200:

       response_result = response.json()['num_audience']
       # response_time = response.json()['response_time']
       #
       # # Make sure that the response time is less than 500 ms
       # response_time_final = response_time.replace("us","")
       # if int(response_time_final) > 500000:
       #   raise Exception(" The response time cannot be more than 500 milliseconds")

       if db_validation is True:

            # DB Validations
            input_for_query_builder = token_converter_for_query_builder(generic_input_dict)
            main_query= segment_sql_query_builder(main_type,input_for_query_builder)
            logger.debug("SQL Query: "+main_query)
            data = get_result(cnx, main_query)
            logger.debug("SQl Query Result: "+str(data))

            # Compare the result of the rest call with the results of the sql query
            db_result = str(data['count(distinct u.uid)'])
            response_result = response.json()['num_audience']

            if str(db_result) != str(response_result):
                raise Exception("User count from the end point- "+str(response_result)+" and User count from the db query- "+str(db_result))

            cnx.close()

       return response_result

def segment_size_post_single_multiple_objects(main_type,generic_input_dict,db_validation):

    cnx = mysql_connect("test_cab")

    request_obj = build_request_payload_for_single_attribute(main_type,generic_input_dict)
    path = API_URL + "/segment_size?query="+str(request_obj)

    logger.debug("Request Path: "+path)

    if request_obj is not None:
        logger.debug("Request Body: " +request_obj)

        response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))

    if response.status_code is 200:

       response_result = response.json()['num_audience']
       # response_time = response.json()['response_time']
       #
       # # Make sure that the response time is less than 500 ms
       # response_time_final = response_time.replace("us","")
       # if int(response_time_final) > 500000:
       #   raise Exception(" The response time cannot be more than 500 milliseconds")

       if db_validation is True:

            # DB Validations
            input_for_query_builder = token_converter_for_query_builder(generic_input_dict)
            main_query= segment_sql_query_builder(main_type,input_for_query_builder)
            logger.debug("SQL Query: "+main_query)
            data = get_result(cnx, main_query)
            logger.debug("SQl Query Result: "+str(data))

            # Compare the result of the rest call with the results of the sql query
            db_result = str(data['count(distinct u.uid)'])
            response_result = response.json()['num_audience']

            if str(db_result) != str(response_result):
                raise Exception("User count from the end point- "+str(response_result)+" and User count from the db query- "+str(db_result))

            cnx.close()

       return response_result


def segment_size_post_single_object(type,value,db_validation):

    cnx = mysql_connect("test_cab")

    query = {
        "type": type,
        "value": value
    }
    path = API_URL + "/segment_size?query="+json.dumps(query)
    logger.debug("Request Path: "+path)

    logger.debug("Request Body: "+json.dumps(query))

    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))

    if response.status_code is 200:

       response_result = response.json()['num_audience']
       # response_time = response.json()['response_time']
       #
       # # Make sure that the response time is less than 500 ms
       # response_time_final = response_time.replace("us","")
       # if int(response_time_final) > 500000:
       #   raise Exception(" The response time cannot be more than 500 milliseconds")

       if db_validation is True:

            # DB Validations
            main_query= "select count(distinct uid) from userstore where token='"+str(token_converter_for_query_builder(type))+"'AND token_value= '"+str(value)+"'"
            logger.debug("SQL Query: "+main_query)
            data = get_result(cnx, main_query)
            logger.debug("SQl Query Result: "+str(data))

            # Compare the result of the rest call with the results of the sql query
            db_result = str(data['count(distinct uid)'])

            if str(db_result) != str(response_result):
                raise Exception("User count from the end point- "+str(response_result)+" and User count from the db query- "+str(db_result))

            cnx.close()

       return response_result




