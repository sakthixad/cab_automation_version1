from config import API_URL
from framework.helpers.mysql_helper import *
from framework.helpers.segment_sql_query_builder_helper import *
from framework.helpers.segment_request_builder_helper import *
import requests
import logging
import sys

root_logger = logging.getLogger("mf.tests")
handler = logging.StreamHandler(sys.stderr)
level = logging.getLevelName("DEBUG")
root_logger.setLevel(level)
handler.setLevel(level)
DEFAULT_FORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
formatter = logging.Formatter(DEFAULT_FORMAT)
handler.setFormatter(formatter)
root_logger.addHandler(handler)
root_logger.setLevel(level)

# Set level for all child handlers
[h.setLevel(level) for h in root_logger.handlers]

logger = logging.getLogger("cab.helpers.segmentsavehelper")


def segment_save_post(request_obj):

    path = API_URL + "/segment/save?query="
    logger.debug("Request Path: "+path)

    if request_obj is not None:
        logger.debug("Request Body: " +request_obj)
        response = requests.post(path, data=request_obj)
    else:
        logger.debug("Request Body: None")
        response = requests.post(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))


def segment_save_post_single_object(type,value):

    cnx = mysql_connect("xadcms")

    query = {
        "type": type,
        "value": value
    }
    path = API_URL + "/segment_save?query="+json.dumps(query)+"&segment_md5=333"
    logger.debug("Request Path: "+path)
    logger.debug("Request Body: "+json.dumps(query))
    response = requests.get(path)

    logger.debug("Response Body: " + str(response.content))
    logger.debug("Response Code: " + str(response.status_code))

    if response.status_code is 200:

        # Print the user ids
        main_query= "select distinct uid from userstore where uid in (select uid from userstore where token='ir' AND token_value='0') and (token='"+str(token_converter_for_query_builder(type))+"'AND token_value= '"+str(value)+"')"
        db_uid_list=[]
        db_uid_list= get_result_set_list(cnx,main_query,"uid")
        print db_uid_list
        cnx.close()

        # DB Validations
        cnx=mysql_connect("xadcms")
        main_query= "select count(distinct uid) from userstore where uid in (select uid from userstore where token='ir' AND token_value='0') and (token='"+str(token_converter_for_query_builder(type))+"'AND token_value= '"+str(value)+"')"
        logger.debug("SQL Query: "+main_query)
        data = get_result(cnx, main_query)
        logger.debug("SQl Query Result: "+str(data))

        # Compare the result of the rest call with the results of the sql query
        db_result = str(data['count(distinct uid)'])
        response_result = response.json()['num_audience']

        if str(db_result) != str(response_result):
            raise Exception("User count from the end point- "+str(response_result))
            raise Exception("User count from the db query- "+str(db_result))
            raise Exception(" The user counts do not match")

        cnx.close()