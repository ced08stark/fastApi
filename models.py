
from tortoise import fields, models
from typing import Union

from tortoise.contrib import pydantic
from tortoise.contrib.pydantic import pydantic_model_creator


# Create Class Repas
class Repas(models.Model):
    repas_id = fields.IntField(pk=True)
    restaurant_id = fields.IntField()
    nom = fields.CharField(max_length=250)
    image = fields.CharField(max_length=500)
    description = fields.CharField(max_length=300)
    price = fields.FloatField()
    rating = fields.FloatField()

   # class Meta:
    #    table: str = 'repas'


Repas_Pydantic = pydantic_model_creator(Repas, name="Repas")
RepasIn_Pydantic = pydantic_model_creator(Repas, name="RepasIn", exclude_readonly=True)


# Create class Restaurant
class Restaurant(models.Model):
    restaurant_id = fields.IntField(pk=True)
    image = fields.CharField(500,default="images0134519cf6628c4f7e56.jpg")
    nom = fields.CharField(max_length=250, default="Undefinied")
    description = fields.CharField(max_length=250, default="Base description")
    rating = fields.FloatField()

    class PydanticMeta:
        pass

    #class Meta:
      #  table: str = 'restaurant'


Restaurant_Pydantic = pydantic_model_creator(Restaurant, name="Restorant")
RestaurantIn_Pydantic = pydantic_model_creator(Restaurant, name="RestorantIn", exclude_readonly=True)


# Create Class User
class User(models.Model):
    user_id = fields.IntField(pk=True)
    localisation_id = fields.IntField(default=1)
    nom = fields.CharField(null=False, max_length=255, unique=True)
    email = fields.CharField(null=False, max_length=255, unique=True)
    password = fields.CharField(null=False, max_length=255)
    phone = fields.IntField(null=False, unique=True)
    image = fields.CharField(max_length=500, default="images446d9dae442bab2269d6.jpg")

    class Meta:
        table: str = '_user'

class Panier(models.Model):
    panier_id = fields.IntField(pk=True)
    produit_panier_id = fields.IntField()

    #class Meta:
        #table: str = 'panier'


Panier_Pydantic = pydantic_model_creator(Panier, name="Panier")
PanierIn_Pydantic = pydantic_model_creator(Panier, name="PanierIn", exclude_readonly=True)





User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True,
                                         exclude=('hashed_password', 'confirmation'))



class ProduitPanier(models.Model):
    produit_panier_id = fields.IntField(pk=True)
    repas_id = fields.IntField()
    quantite = fields.IntField()
    user_id = fields.IntField()

    #class Meta:
        #table: str = 'ProduitPanier'


ProduitPanier_Pydantic = pydantic_model_creator(ProduitPanier, name="ProduitPanier")
ProduitPanierIn_Pydantic = pydantic_model_creator(ProduitPanier, name="ProduitPanierIn", exclude_readonly=True)


class Category(models.Model):
    category_id = fields.IntField(pk=True)
    image = fields.CharField(max_length=500)
    nom = fields.CharField(max_length=50)

    #class Meta:
        #table: str = 'Category'


Category_Pydantic = pydantic_model_creator(Category, name="Categrory")
CategoryIn_Pydantic = pydantic_model_creator(Category, name="CategroryIn", exclude_readonly=True)


class Localisation(models.Model):
    localisation_id = fields.IntField(pk=True)
    ville = fields.CharField(max_length=50)
    quartier = fields.CharField(max_length=50)
    #class Meta:
        #table: str = 'Localisation'
Localisation_Pydantic = pydantic_model_creator(Localisation, name="Localisation")
LocalisationIn_Pydantic = pydantic_model_creator(Localisation, name="LocalisationIn", exclude_readonly=True)

## La classe commande

class Commande(models.Model):
    commande_id = fields.IntField(pk=True)
    user_id = fields.IntField()
    panier_id = fields.IntField()
    prix_total = fields.FloatField()
    class Meta:
        table: str = 'commande'

Commande_Pydantic = pydantic_model_creator(Localisation, name="Commande")
CommandeIn_Pydantic = pydantic_model_creator(Localisation, name="CommandeIn", exclude_readonly=True)







