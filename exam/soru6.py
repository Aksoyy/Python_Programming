def error_handler():
    try:
        name = int('1232a')
        lastname = ['yilmaz', 'keskin'][3]
        other_dict = {"name":"merve", "lastname": "demir"}
        other_name = other_dict['other_name']
        age = 1/0
        print('OK!')

    except ValueError as error:
        print("Gonderılen tur hatalı! : ", error)  
    except IndexError as error2:
        print("Gonderılen index(konum) hatalı! : ", error2)
    except KeyError as error3:
        print("Gonderılen key hatalı! : ", error3)    
    except NameError as error4:
        print("Gonderılen name hatalı! : ", error4)
    except ZeroDivisionError as error5:
        print("Bir sayıyı 0'a bölemezsiniz! : ", error5)

error_handler()
