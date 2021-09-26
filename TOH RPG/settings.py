import json
from enum import Enum

with open('assets/ataques.json', 'r') as json_file:
    ATAQUES = json.load(json_file)
    
class BaseStatsAzura(Enum):
    atk = 100
    
    