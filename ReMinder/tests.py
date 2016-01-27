from django.test import TestCase
import json
import pickle
# Create your tests here.

# test json serialization


class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

