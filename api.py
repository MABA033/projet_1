import requests

url = 'http://www.ulaval.ca/'

rep = requests.get(url)

if rep.status_code == 200:
    # la réponse est bonne, afficher son contenu
    print(rep.text)
    
else:
    # afficher un message d'erreur
    print(f"Le GET sur {url} a produit le code d'erreur {rep.status_code}.")

url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

rep = requests.get(url_base+'lister/', params={'idul': 'xxxxx'})
if rep.status_code == 200:
    # la requête s'est déroulée normalement; décoder le JSON
    rep = rep.json()
    print(rep)
    
else:
    print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

rep = requests.post(url_base+'débuter/', data={'idul': 'xxxxx'})
rep.json()