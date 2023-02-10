import pandas as pd
import numpy as np
import csv

output = []

with open('shared_articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    output = data[1:21]




