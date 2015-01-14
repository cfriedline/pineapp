import os, django, gspread
import pandas as pd
from dateutil.parser import parse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pineapp.settings")
django.setup()

from metadata.models import Sample

def get_data(user, password):
    gc = gspread.login(user, password)
    wks = gc.open("pine_sampling").sheet1
    data = wks.get_all_records()
    return pd.DataFrame(data)

def get_float(val):
    try:
        return float(val)
    except ValueError as e:
        return None

def run_import(data):
    for i, row in data.iterrows():
        print i
        s = Sample(name=row['Sample'],
                   sample_date=parse(row['Date']),
                   lat = get_float(row['Lat']),
                   lon = get_float(row['Long']),
                   dbh = get_float(row['DBH (cm)']),
                   angle_low = get_float(row['LowAngle']),
                   angle_high = get_float(row['HighAngle']),
                   angle_distance = get_float(row['AngleDistance']),
                   height = get_float(row['Height (m)']),
                   bark1 = get_float(row['Bark1 (in)']),
                   bark2 = get_float(row['Bark2 (in)']),
                   bark3 = get_float(row['Bark3 (in)']),
                   bark4 = get_float(row['Bark4 (in)']))

        s.save()

if __name__ == '__main__':
    accounts = open("/Users/chris/.google").readlines()
    vcu = accounts[0].split()
    user = vcu[0]
    password = vcu[1]
    data = get_data(user, password)
    run_import(data)
