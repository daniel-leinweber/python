#!/usr/bin/env python3
import logging

def initialize_logger(name, file_name):
    global _logger
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

class Animal():
    sound = ""
    category = ""

    def __init__(self):
        _logger.info('Animal instance created')

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    sound = "woof"

    def __init__(self):
        _logger.info('Dog instance created')

class Cat(Animal):

    def __init__(self, sound):
        _logger.info('Cat instance created')
        self.sound = sound

initialize_logger("main_py", "log.txt")

cat = Cat("meow")
cat.make_sound()
