###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:
    
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.
    
    def add_test(self, test, results):
        self.test = test
        self.results = results

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

    def has_covid(self):
        covid_prob = 0
        
        if self.test == 'covid':
            if self.results:
                covid_prob = 0.99
            if not self.results:
                covid_prob = 0.01
        else:
            covid_symptoms = ['fever', 'cough', 'anosmia']
            covid_prob = 0.05 + 0.1 * len(list(set(self.symptoms).intersection(covid_symptoms)))
            
        return round(covid_prob, 2)
            
######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import random

class Deck:
    
    def __init__(self):
        self.cards = []
        self.build()
     
    def build(self):
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
     
    def draw(self):
        drawn_card = self.cards.pop()
        print('Your card is ' + drawn_card.value + ' of ' + drawn_card.suit)
        
deck = Deck()

    
###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    
    @abstractmethod
    def compute_perimeter(self):
        pass
    
    @abstractmethod
    def compute_surface(self):
        pass


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.height = h
    
    def compute_perimeter(self):
        self.perimeter = self.base + self.c1 + self.c2
        return self.perimeter
    
    def compute_surface(self):
        self.surface = 0.5 * self.base * self.height
        return self.surface
    
# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def compute_perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter
    
    def compute_surface(self):
        self.surface = self.a * self.b
        return self.surface
    
# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

import math

class Circle(PlaneFigure):
    
    def __init__(self, radius):
        self.radius = radius
    
    def compute_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
    
    def compute_surface(self):
        self.surface = math.pi * (self.radius)**2
        return self.surface
    
