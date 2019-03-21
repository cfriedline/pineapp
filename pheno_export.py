# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0
#   kernelspec:
#     display_name: pineapp
#     language: python
#     name: pineapp
# ---

# %%
from django_setup import setup_django
import pandas as pd
import os
os.environ['DB_PORT_5432_TCP_ADDR'] = 'localhost'
setup_django()
# %load_ext autoreload
# %autoreload 2
import numpy as np
import itertools
import datetime
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
#import matplotlib.pyplot as plt
import traceback as tb
# %load_ext rpy2.ipython

# %%
from envdata.models import Sample

# %%
for x in Sample.objects.all():
    print(x.bark_avg_mm)

# %%
with open("pheno_export_2019mar20.txt", "w") as o:
    o.write("name\tlat\tlon\theight\tbark1\tbark2\tbark3\tbark4\tbark_avg_mm\tdbh\n")
    for x in Sample.objects.all():
        o.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x.name, x.lat, x.lon, x.height_calc, x.bark1, x.bark2, x.bark3, x.bark4, x.bark_avg_mm, x.dbh))

# %%
# !wc -l "pheno_export_2019mar20.txt"

# %%
