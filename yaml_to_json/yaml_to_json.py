import yaml, json

def yaml_to_json(yaml_file):
    
    #file.yaml file read
    with open(yaml_file, 'r') as yaml_ :
        yaml_text = yaml.safe_load(yaml_)
    
    #file.json file write
    json_text = json.dumps(yaml_text)

    if 'file.json':
        with open("file.json", "w") as json_out:    
            json_out.write(json_text)
            print("İslem tamamlandi")
    else:
        print("Dosya mevcut degildir")

yaml_to_json("file.yaml")