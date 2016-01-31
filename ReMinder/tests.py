from django.test import TestCase
import json
import pickle
# Create your tests here.

# test json serialization


results = [(player, 0) for player in [1,2,3,4]]
for result in results:
    result[1] = 0
