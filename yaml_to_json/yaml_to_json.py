import yaml, json

def yaml_to_json(yaml_file):
    
    #file.yaml --> python object
    with open(yaml_file, 'r') as yaml_ :
        yaml_text = yaml.safe_load(yaml_)
        #print(yaml_text) --> python object
    
    #file.json file
    json_text = json.dumps(yaml_text)

    if 'file.json':
        with open("file.json", "w") as json_out:    
            json_out.write(json_text)
            print("İslem tamamlandi")
    else:
        print("Dosya mevcut degildir")

yaml_to_json("file.yaml")