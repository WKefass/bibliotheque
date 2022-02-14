# API PYTHON FLASK

API de gestion une bibliothèque en listant les livres et les catégories
### Installation des outils

#### Python 3.10.2
#### pip 22.0.3 from C:\Users\WIN10USERZZ\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip freeze > requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

. [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

.[SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

.[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

URL de base : à l’heure actuelle, cette application ne peut être exécutée que localement et n’est pas hébergée en tant qu’URL de base. L’application backend est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.

## Type d'erreur
Les erreurs sont renvoyées sous forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
     {
    "livres": [
        {
            "auteur": "David Roch",
            "categorie_id": 2,
            "date_publication": "Sun, 22 Mar 1998 00:00:00 GMT",
            "editeur": "Poitiers",
            "id": 1,
            "isbn": "145-346-08",
            "titre": "Le Méchant Loup"
        },
        {
            "auteur": "Sembene Ousmane",
            "categorie_id": 2,
            "date_publication": "Tue, 14 Sep 1965 00:00:00 GMT",
            "editeur": "Presence Africaine",
            "id": 2,
            "isbn": "057-568-94",
            "titre": "Le Mandat"
        },
        {
            "auteur": "Voltaire",
            "categorie_id": 2,
            "date_publication": "Sat, 16 May 1908 00:00:00 GMT",
            "editeur": "Larousse",
            "id": 3,
            "isbn": "006-123-09",
            "titre": "Candide"
        },
        {
            "auteur": "Charles Perrault",
            "categorie_id": 3,
            "date_publication": "Tue, 14 Sep 1965 00:00:00 GMT",
            "editeur": "Claude Barbin",
            "id": 4,
            "isbn": "067-568-94",
            "titre": "Chaperon Rouge"
        },
        {
            "auteur": "Koumao",
            "categorie_id": 1,
            "date_publication": "Sat, 11 Aug 2007 00:00:00 GMT",
            "editeur": "Le Palais",
            "id": 5,
            "isbn": "056-099-48",
            "titre": "Oxygène"
        },
        {
            "auteur": "Charles Perrault",
            "categorie_id": 4,
            "date_publication": "Wed, 25 Nov 2009 00:00:00 GMT",
            "editeur": "Claude Barbin",
            "id": 6,
            "isbn": "097-555-80",
            "titre": "Autour du feu"
        },
        {
            "auteur": "Lucas Digne",
            "categorie_id": 1,
            "date_publication": "Wed, 25 Jan 2012 00:00:00 GMT",
            "editeur": "La Projection",
            "id": 7,
            "isbn": "077-094-71",
            "titre": "La ville et ses alentours"
        },
        {
            "auteur": "Jules Verne",
            "categorie_id": 3,
            "date_publication": "Mon, 15 Oct 2012 00:00:00 GMT",
            "editeur": "Edicef",
            "id": 9,
            "isbn": "9é7-214-01",
            "titre": "Le tour du monde en 80 jours"
        }
    ],
    "status_code": 200,
    "success": true,
    "total_livres": 8
}

.##Get/livres/id
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.
```
{
    "auteur": "David Roch",
    "categorie_id": 2,
    "date_publication": "Sun, 22 Mar 1998 00:00:00 GMT",
    "editeur": "Poitiers",
    "id": 1,
    "isbn": "145-346-08",
    "titre": "Le Méchant Loup"
}
```


. ## DELETE/livres/id

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.
```
   {
    "id_book": 7,
    "new_total": 6,
    "success": true
  }
```

. ##PATCH/livres/id
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ```
    {
       {
    "auteur": "Konzou",
    "categorie_id": 1,
    "date_publication": "2004-05-12",
    "editeur": "Le Palais_Ice",
    "id": 5,
    "isbn": "056-099-48",
    "titre": "Oxygènes"
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles.

     {
    "Categorie": [
        {
            "id_categorie": 1,
            "libelle_categorie": "Science"
        },
        {
            "id_categorie": 2,
            "libelle_categorie": "Histoire"
        },
        {
            "id_categorie": 6,
            "libelle_categorie": "Harlequin"
        },
        {
            "id_categorie": 3,
            "libelle_categorie": "Fictions"
        }
    ],
    "status_code": 200,
    "success": true,
    "total": 4
}
```

.##GET/categories/id
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

{
    "Categorie": [
        {
            "id_categorie": 1,
            "libelle_categorie": "Science"
        },
        {
            "id_categorie": 2,
            "libelle_categorie": "Histoire"
        },
        {
            "id_categorie": 6,
            "libelle_categorie": "Harlequin"
        },
        {
            "id_categorie": 3,
            "libelle_categorie": "Fictions"
        }
    ],
    "status_code": 200,
    "success": true,
    "total": 4
}

. ## DELETE/categories/id

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.
```
{
    "id_cat": 6,
    "new_total": 3,
    "status": 200,
    "success": true
}
```

. ##PATCH/categories/id
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.
  ```
  ```
   {
    "id_categorie": 3,
    "libelle_categorie": "Fiction"
  }

.##GET/categories/id/livres
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.
```
  {
    "Status_code": 200,
    "Success": true,
    "categorie": {
        "id_categorie": 2,
        "libelle_categorie": "Histoire"
    },
    "livres": [
        {
            "auteur": "David Roch",
            "categorie_id": 2,
            "date_publication": "Sun, 22 Mar 1998 00:00:00 GMT",
            "editeur": "Poitiers",
            "id": 1,
            "isbn": "145-346-08",
            "titre": "Le Méchant Loup"
        },
        {
            "auteur": "Sembene Ousmane",
            "categorie_id": 2,
            "date_publication": "Tue, 14 Sep 1965 00:00:00 GMT",
            "editeur": "Presence Africaine",
            "id": 2,
            "isbn": "057-568-94",
            "titre": "Le Mandat"
        },
        {
            "auteur": "Voltaire",
            "categorie_id": 2,
            "date_publication": "Sat, 16 May 1908 00:00:00 GMT",
            "editeur": "Larousse",
            "id": 3,
            "isbn": "006-123-09",
            "titre": "Candide"
        }
    ],
    "total": 3
}
```
