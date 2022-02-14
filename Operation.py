from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from turtle import  back
from flask_migrate import Migrate
from flask import request
from werkzeug.exceptions import abort



#################################
#Connexion a la base de donnée
################################



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:wolkk3fass@localhost:5432/Bibliotheque'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

migrate=Migrate(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATH,POST,DELETE,OPTION')
    return response

################################
#Creation de la table categories
###############################
class Categorie(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True )
    libelle_catégorie=db.Column(db.String(50), nullable=False)
    livre =db.relationship('Livre')


    def __init__(self,libelle_catégorie):
        self.libelle_catégorie=libelle_catégorie


    def format(self):
        return {
            'id ' : self.id ,
            'libelle_catégorie' : self.libelle_catégorie
        }

    def ajouter(self):
        db.sion.add(self)
        db.session.commit()


    def paginer(request):
       items=[ item.format()  for item in request ]
       return items


    def inserer(self):
        db.session.add(self)
        db.session.commit()

    def supprimer(self):
        db.session.delete(self)
        db.session.commit()

    def modifier(self):
        db.session.commit()


db.create_all()


################################
#Creation de la table livres
###############################
class Livre(db.Model):
    __tablename__='livres'
    id= db.Column(db.Integer,primary_key=True )
    isbn=db.Column(db.String(50),nullable=False)
    titre=db.Column(db.String(50),nullable=False)
    date_publication=db.Column(db.Date,nullable=False)
    auteur=db.Column(db.String(50),nullable=False)
    editeur=db.Column(db.String(50),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'))



    def __init__(self,isbn,titre,date_publication,auteur,editeur,categories_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categories_id


    def format(self):
        return {
            'id ' : self.id ,
            'isbn' : self.isbn,'titre' :self.titre,
            'date_publication': self.date_publication,
            'auteur' : self.auteur,
            'editeur': self.editeur,
            'categorie':self.categorie_id
        }

    def paginer(request):
        items = [item.format() for item in request]
        return items


    def inserer(self):
        db.session.add(self)
        db.session.commit()

    def supprimer(self):
        db.session.delete(self)
        db.session.commit()
    def modifier(self):
        db.session.commit()
db.create_all()









##### ########################
# Afficher tous les livres
# #############################
@app.route('/Livres')
def afficher_les_livres():
    try:
        livres=Livre.query.all()
        livres=Livre.paginer(livres)
        return jsonify({
            'success': True,
            'statut' : 200,
            'id_livre' : livres,
            'Livre_total' : len(livres)
        })
    except:
        abort(404)
    finally:
        db.session.close()




##### ##########################
# recherhe d'un livre par son id
# ###############################

@app.route('/Livres/<int:id>')
def chercher_un_livre(id):
        livres=Livre.query.get(id)
        if livres is None:
            abort(404)
        else:
             return livres.format()
##### ############################
# Afficher les livres d'une categorie
# ################################
@app.route('/Categories/<int:id>/Livres')
def afficher_livre_cat(id):
    try:
        categories= Categorie.query.get(id)
        livre=Livre.query.filter_by(categorie_id=id).all()
        livre=Livre.paginer(livre)
        return jsonify({
            'success': True,
            'statut': 200,
            'total':len(livre),
            'categorie': categories.format(),
            'livre':livre


        })
    except:
        abort(404)
    finally:
        db.session.close()
##### ########################
# Afficher toutes les categories
# #############################
@app.route('/Categories')
def afficher_les_categories():

        categories=Categorie.query.all()
        categories=Categorie.paginer(categories)
        if categories is None:
            abort(404)
        else:
            return jsonify({
                'success' :True,
                'statut':200,
                'categorie':categories,
                'total':len(categories)

            })


##### ########################
# Afficher  une categorie par son id
# #############################
@app.route('/Categories/<int:id>')
def chercher_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()

##### ########################
# Supprimer un livre
# #############################
@app.route('/Livres/<int:id>',methods= ['DELETE'])
def supprimer_livre(id):
    try:
        livre=Livre.query.get(id)
        livre.supprimer()
        return jsonify({
            'success':True,
            'id_livre': id,
            'total_livre':livre.query.count()
        })
    except:
        abort(404)
    finally:
        db.session.close()
##### ########################
# Supprimer une categorie
# #############################
@app.route('/Categories/<int:id>',methods= ['DELETE'])
def supprimer_categorie(id):
    try:
        categorie=Categorie.query.get(id)
        categorie.supprimer()
        return jsonify({
            'success':True,
            'id_categorie': id,
            'total_categorie':categorie.query.count()
        })
    except:
        abort(404)
    finally:
        db.session.close()

##### ########################
# Modifier un livre
# #############################
@app.route('/Livres/<int:id>',methods= ['PATCH'])
def modifier_livre(id):
    try:
        body=request.get_json()
        livre=Livre.query.get(id)

        if "titre" in body and "editeur" in body and "auteur" in body and "date_publication" in body and "isbn" in body:
            livre.titre=body["titre"]
            livre.editeur=body["editeur"]
            livre.auteur=body["auteur"]
            livre.date_publication=body["date_publication"]
            livre.isbn=body["isbn"]
        livre.modifier()
        return jsonify({
                'success':True,
                'Livre': livre.format()
            })
    except:
        abort(404)

##### ########################
# Modifier une categorie
# #############################

@app.route('/Categories/<int:id>',methods= ['PATCH'])
def modifier_categories(id):
    body = request.get_json()
    categorie =Categorie.query.get(id)
    try:
        if "libelle_catégorie" in body:
            categorie.libelle_catégorie= body["libelle_catégorie"]
        categorie.modifier()
        return jsonify({
                'success': True,
                'catégorie': categorie.format()
            })
    except:
        abort(404)


##### ########################
# Gestion des ereurs
# #############################
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success':False,
        'error': 404,
        'message':'not found'
    }),404

@app.errorhandler(500)
def not_found(error):
    return jsonify({
        'success':False,
        'error': 500,
        'message':'Erreur du serveur interne'
    }),500

@app.errorhandler(400)
def not_found(error):
    return jsonify({
        'success':False,
        'error': 400,
        'message':'Mauvaise requete'
    }),400









if __name__=='__main__':
    app.run(debug=True)
