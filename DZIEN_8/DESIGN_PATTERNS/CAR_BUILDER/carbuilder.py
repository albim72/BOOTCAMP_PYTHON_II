from abc import ABC, abstractmethod

class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None
    
class Car:
    def __init__(self):
        self._wheels = list()
        self._engine = None
        self._body = None
        
    def setBody(self,body):
        self._body = body
        
    def setEngine(self,engine):
        self._engine = engine
        
    def attachWheel(self,wheel):
        self._wheels.append(wheel)
