from dvc import api
import pandas as pd
from io import StringIO
import  sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data...')

data_path = api.read('data/data.csv', remote='d-track') # DVC associated paths

df = pd.read_csv(StringIO(data_path))
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

#breakpoint() # Data is loaded

numeric_columns_mask = (df.dtypes == float) | (df.dtypes==int)
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]

df = df[numeric_columns]

logger.info('Data fetched and prepared.')

