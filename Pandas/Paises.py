import pandas as pd
import numpy as np
import requests as req
from sqlalchemy import false, true

url = "https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv"
c = pd.read_csv(url,sep=";")
print(c["continent"])

