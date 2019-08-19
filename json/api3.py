import requests
from functools import wraps

url_link='https://randomuser.me/api/?results=200'

def make_request(control_func):
    def wrapTheFunction():
        response = requests.get(url_link)
        json_response = control_func(response)
        
        if not json_response:
            print("Error")
        
        list_ = []
        for index in range(200):
            dict_ = {}
            dict_["title"] = json_response["results"][index]["name"]["title"]
            dict_["first"] = json_response["results"][index]["name"]["first"]
            dict_["last"] = json_response["results"][index]["name"]["last"]
            dict_["username"] = json_response["results"][index]["login"]["username"]
            dict_["password"] = json_response["results"][index]["login"]["password"]
            # print(dict_)
            list_.append(dict_)
            #dict_.clear()
        #print(list_)
        #print(list_[0])

        if 'json_log.log':
                with open("json_log.log", "w") as j_log:    
                    for item in list_:
                        j_log.write("%s\n" % item)
                    #j_log.write("test")
        else:
            print("Dosya mevcut degildir")

    return wrapTheFunction

def client_method(get_response):
    if get_response.status_code == 200:
        json_response = get_response.json()
        return json_response
    elif get_response.status_code == 404:
        print('Not Found')
        return 0
    else:
        print('An error has occurred')
        return 0

result = make_request(client_method)
result()
