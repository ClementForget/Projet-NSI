def add_infos(nom, prenom, classe, age):
  dic = {'nom': nom, 'prenom': prenom, 'classe': classe, 'age': age}
  return dic


def aff_data(classe):
  n = 1
  for dico in classe:
    print(f"{n} - {dico.get('prenom')} {dico.get('nom')}, agé de : {dico.get('age')}, en classe de : {dico.get('classe')}")
    n = n+1


def del_data(classe, num):
  classe.del[num]
