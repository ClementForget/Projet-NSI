def add_infos(nom, prenom, classe, age):
  dic = {'nom': nom, 'prenom': prenom, 'classe': classe, 'age': age}
  return dic


def aff_data(classe):
  n = 1
  for dico in classe:
    print(f"{n} - {dico.get('prenom')} {dico.get('nom')}, agé de : {dico.get('age')}, en classe de : {dico.get('classe')}")
    n = n+1

def dell_data(classe):
  nbr_classe = len(classe)
  print(f"Il y a actuellement {nbr_classe} dans votre data base")
  delete = int(input("Qui voulez vous supprimer ? Insérez son numeo : "))
  delete=delete-1
  del classe[delete]
  return classe