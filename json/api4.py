import requests
import logging
from functools import wraps

url_link='https://randomuser.me/api/?results=200'
get_=requests.get(url_link)

def client_method(link_control):
    def wrapTheFunction(*args, **kwargs):

        json_response = link_control(*args,**kwargs)

        if not json_response:
            print("Error")
            return 0

        #dict_ = {}
        list_ = []
        for index in range(200):
            dict_ = {}
            dict_["title"] = json_response["results"][index]["name"]["title"]
            dict_["first"] = json_response["results"][index]["name"]["first"]
            dict_["last"] = json_response["results"][index]["name"]["last"]
            dict_["username"] = str(json_response["results"][index]["login"]["username"])
            dict_["password"] = json_response["results"][index]["login"]["password"]
            #str(dict_)
            # str casting
            # print(dict_)
            list_.append(dict_)
            #dict_.clear()
        #print(list_)
        #print(list_[0])

        logging.basicConfig(filename='json_log.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
        # logging.info('Admin logged in')
        
        # if 'json_log.log':
        with open("json_log.log", "w"): #as j_log:    
            for item in list_:
                logging.info("%s\n" % item)
                    # j_log.write("%s\n" % item)
                    #j_log.write("test")
        # else:
        #     print("Dosya mevcut degildir")
        
    return wrapTheFunction

@client_method
def make_request(link):
    get_ = requests.get(link)
    if get_.status_code == 200:
        json_response = get_.json()
        return json_response
    elif get_.status_code == 404:
        print('Not Found')
        return 0
    else:
        print('An error has occurred')
        return 0

make_request(url_link)