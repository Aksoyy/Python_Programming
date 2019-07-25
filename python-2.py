rehber = {
    "hakan": 5554443322 ,
    "aksoy": 5556667788,
    "deneme": 5554446677
}

def kayitli_kisiler(result):
    for a in result:
        print(a)
"""
    kayitli_kisiler(rehber) : Kayitli kisileri getirir
Cikti:  hakan
        aksoy
        deneme
"""

def kayitli_numaralar(result):
    for b in result.values():
        print(b)
"""
    kayitli_numaralar(rehber) : Kayitli numaralari getirir
Cikti:  5554443322
        5556667788
        5554446677
"""

def kayit_guncelle(result, kisi, numara):
    for a in result:
        if a==kisi:
            result[a]=numara
            print("Guncelleme sonucu = ", a, ":", result[a])
"""
    kayit_guncelle(rehber,'hakan',111)
Cikti: Guncelleme sonucu =  hakan : 111
"""

def kayit_ekle(result, kisi, numara):
    result[kisi]=numara
    print("Eklenen kayit : ", list(result.keys())[-1], ":", list(result.values())[-1])
    
# (list(rehber.items())[-1])[0]=kisi ve (list(rehber.items())[-1])[1]=numara
    
"""
    kayit_ekle(rehber,"hasan",5552223311)
Cikti: Eklenen kayit :  hasan : 5552223311
"""
