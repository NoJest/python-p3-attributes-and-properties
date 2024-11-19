#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed="Mastiff", name="franky"):
        self._breed = None
        self._name = None
        self.breed = breed
        self.name = name
        
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name:str):
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            return
        if len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return 
        self._name = name
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed:str):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return
        self._breed = breed