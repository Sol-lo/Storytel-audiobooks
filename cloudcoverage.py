import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

def cloudy(date):
    client_ID = "5b083d5a-6244-436c-af71-caca0e531c1e"
    url = "https://frost.met.no/observations/v0.jsonld"
    params = {
         "sources" : "SN90450",
        "elements" : "cloud_area_fraction",
        "referencetime" : date,
    }
    response = requests.get(url, params=params, auth = (client_ID, ''))
    response.raise_for_status()
    data = response.json()
    clouds = data['data'][0]['observations'][0]['value']
    return clouds

cloudy(2026-11-18)
print("hello")