import requests

url_link='https://randomuser.me/api/?results=200'

def make_request(url_code):
    
    response = requests.get(url_code)

    if response.status_code == 200:
        json_response = response.json()
    elif response.status_code == 404:
        print('Not Found')
    else:
        print('An error has occurred')

    """test command
    print(json_response["results"][0]["name"]["title"])
    print(json_response["results"][0]["name"]["first"])
    print(json_response["results"][0]["name"]["last"])
    print(json_response["results"][0]["login"]["username"])
    print(json_response["results"][0]["login"]["password"])
    """

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

make_request(url_link)