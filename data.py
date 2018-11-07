import quandl
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

quandl.ApiConfig.api_key = "ToK1ZytHvkj1ozV_-svx"


data = quandl.get_table('ZACKS/FC', paginate=True, ticker=['AAPL', 'MSFT'], per_end_date={'gte': '2015-01-01'}, qopts={'columns':['ticker', 'per_end_date']})


print(data)
