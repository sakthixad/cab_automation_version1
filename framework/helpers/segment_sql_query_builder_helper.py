import json

def token_converter_for_query_builder(input):
    input_string = json.dumps(input)
    new_string = input_string.replace("segment","seg")
    new_string = new_string.replace("brand","b")
    new_string = new_string.replace("age","a")
    new_string = new_string.replace("gender","g")
    new_string = new_string.replace("income","i")
    new_string = new_string.replace("behavior","bAud")
    new_string = new_string.replace("country","co")
    new_string = new_string.replace("state","st")
    new_string = new_string.replace("zip","z")
    new_string = new_string.replace("dma","d")
    new_string = new_string.replace("category","l")

    input_json = json.loads(new_string)
    return input_json

def token_converter_for_single_token(input):

    new_string = None

    token_map = dict()
    token_map["segment"] = "seg"
    token_map["brand"] = "b"
    token_map["age"] = "a"
    token_map["gender"] = "g"
    token_map["income"] = "i"
    token_map["behavior"] = "bAud"
    token_map["country"] = "co"
    token_map["state"] = "st"
    token_map["zip"] = "z"
    token_map["dma"] = "d"
    token_map["category"] = "l"

    for key in token_map:
        if input == key:
            new_string = input.replace(key,token_map[key])
    return new_string

def segment_sql_query_builder(main_type, token_map):

    main_query = None
    unum = 1
    if main_type is None:

        if len(token_map) is 1:

            for key in token_map:

                if key != "NOT" and key != "AND" and key != "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key

                        if key2 == "direct":

                            value = value1[key2]
                            for i in value:
                                query = "select count(distinct uid) from test_userstore1 where token='"+key1+ "' AND token_value= '"+str(i)+"'"
                                main_query = query

                elif key == "AND":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        values = value1[key2]
                        subquery = "select count(distinct u.uid) from test_userstore1 u where "
                        for i,value in enumerate(values):
                            if i > 0:
                                subquery += ' AND '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery

                elif key == "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = "select count(distinct u.uid) from test_userstore1 u where "
                        for i, value in enumerate(value_list):
                            if i > 0:
                              subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery

                elif key == "NOT":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = "select count(distinct uid) from test_userstore1 u where "
                        for i,value in enumerate(value_list):
                            if i > 0:
                                subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value<> '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        main_query = subquery
    else:

            sub_query_list = []

            for key in token_map:

                if key != "NOT" and key != "AND" and key != "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key

                        if key2 == "direct":

                            value = value1[key2]
                            for i in value:

                                query = "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key1+"' AND u{num}.token_value= '"+ \
                                        str(i)+"')"
                                subquery = query.format(num=unum)
                                unum += 1
                            sub_query_list.append("("+subquery+ ")")

                elif key == "AND":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        values = value1[key2]
                        subquery = ""
                        for i,value in enumerate(values):
                            if i > 0:
                                subquery += ' AND '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        sub_query_list.append("("+subquery+ ")")

                elif key == "OR":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery= ""
                        for i, value in enumerate(value_list):
                            if i > 0:
                              subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value= '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                    sub_query_list.append("("+subquery+ ")")

                elif key == "NOT":

                    key1 = key
                    value1 = token_map[key1]

                    for key in value1:

                        key2 = key
                        value_list = value1[key2]
                        subquery = ""
                        for i,value in enumerate(value_list):
                            if i > 0:
                                subquery += ' OR '
                            subquery += "u.uid IN (select u{num}.uid from test_userstore1 u{num} " \
                                        "where u{num}.token= '"+key2+"' AND u{num}.token_value<> '"+ \
                                        str(value)+"')"
                            subquery = subquery.format(num=unum)
                            unum += 1
                        sub_query_list.append("( "+subquery+ ")")

            full_query = ""
            for i,value in enumerate(sub_query_list):
                if i > 0:
                    full_query += ' ' + main_type + ' '
                full_query += value
            main_query = "select count(distinct u.uid) from test_userstore1 u where ("+full_query+")"

    return main_query






