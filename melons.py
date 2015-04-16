"""This file should have our melon-type classes in it."""
from abc import ABCMeta, abstractmethod

BASE_PRICE = 5
BASE_PRICE_CAS_OG = BASE_PRICE + 1

class Parent_Melon(object):
    # stops users from instatiating abstract class Parent_Melon
    # with abstract methods get_price
    # -- get_price is named the same as the subclass methods
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_price(self):
    # Need to make sure you use self.species!
        if (self.species == "Ogen") or (self.species == "Casaba"):
            return BASE_PRICE_CAS_OG
        else:
            return BASE_PRICE



class WatermelonOrder(Parent_Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 3:
            total = (BASE_PRICE * int(qty))*0.75   # TODO, calculate the real amount!
        else:
            total = (BASE_PRICE * int(qty))
        return total

class CantaloupeOrder(Parent_Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 5:
            total = (BASE_PRICE * int(qty))*0.5   # TODO, calculate the real amount!
        else:
            total = (BASE_PRICE * int(qty))
        return total

class CasabaOrder(Parent_Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE_CAS_OG * int(qty))*1.5   # TODO, calculate the real amount!

        return total

class SharlynOrder(Parent_Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE * int(qty))*1.5   # TODO, calculate the real amount!

        return total


class SantaClausOrder(Parent_Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE * int(qty))*1.5   # TODO, calculate the real amount!

        return total


class ChristmasOrder(Parent_Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * int(qty)   # TODO, calculate the real amount!

        return total

class HornedParent_MelonOrder(Parent_Melon):
    species = "Horned Parent_Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE * int(qty))*1.5   # TODO, calculate the real amount!

        return total


class XiguaOrder(Parent_Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE * int(qty))*1.5*2   # TODO, calculate the real amount!

        return total


class OgenOrder(Parent_Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE_CAS_OG * int(qty)   # TODO, calculate the real amount!

        return total