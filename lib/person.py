#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

   
class Person:
    
    def __init__(self, job="spanking people", name="Guido"):
        self._job = None
        self.job = job
        self.name = name
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Name must be string between 1 and 25 characters.")
            return
        if len(value) < 1 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value.title()
  
  
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return 
        self._job = value
