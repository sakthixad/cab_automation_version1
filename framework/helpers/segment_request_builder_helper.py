import json

def build_request_payload_segment_size(main_type,token_map):

    main_value = []

    for key in token_map:

            key1 = key
            value1 = token_map[key1]

            for key in value1:

                key2 = key

                if key2 == "direct" and key1 != "brand" and key1!="category":

                    value = value1[key2]
                    if len(value) is 1:
                        dict1 = dict()
                        dict1['type'] = key1
                        dict1['value'] = value[0]
                        main_value.append(dict1)

                elif key2 == "direct" and key1 == "brand":

                    value = value1[key2]
                    if len(value) is 1:
                        dict1 = dict()
                        dict1['type'] = key1
                        dict1['value'] = {"id" : value[0]}
                        main_value.append(dict1)

                elif key2 == "direct" and key1 == "category":

                    value = value1[key2]
                    if len(value) is 1:
                        dict1 = dict()
                        dict1['type'] = key1
                        dict1['value'] = {"id" : value[0]}
                        main_value.append(dict1)
                else:

                    if key2 != "brand" and key2 != "category":

                        value = value1[key2]

                        if len(value) is 1:
                            list = value1[key]
                            dict1 = dict()
                            dict1['type'] = key1
                            map = dict()
                            map['type'] = key
                            map['value'] = list[0]
                            dict1['value'] = map
                            main_value.append(dict1)
                        else:

                            list1 = value1[key]
                            value_list = []
                            dict1 = dict()
                            dict1['type'] = key1

                            for i in list1:
                                map = dict()
                                map['type'] = key
                                map['value'] = i
                                value_list.append(map)
                            dict1['value'] = value_list
                            main_value.append(dict1)
                    else:

                        value = value1[key2]

                        if len(value) is 1:
                            list = value1[key]
                            dict1 = dict()
                            dict1['type'] = key1
                            map = dict()
                            map['type'] = key
                            map['value'] = {"id":list[0]}
                            dict1['value'] = map
                            main_value.append(dict1)
                        else:

                            list1 = value1[key]
                            value_list = []
                            dict1 = dict()
                            dict1['type'] = key1

                            for i in list1:
                                map = dict()
                                map['type'] = key
                                map['value'] = {"id":i}
                                value_list.append(map)
                            dict1['value'] = value_list
                            main_value.append(dict1)

    request = {
        "type": main_type,
        "value": main_value
    }
    return json.dumps(request)
