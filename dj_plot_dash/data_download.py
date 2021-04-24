import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel("INFO")
    
import pandas as pd
from getpass import getpass, getuser
import six
import dateutil.parser as dp
import tempfile
import shutil
import os
from collections import OrderedDict
from earthranger_sarf import utils
import numpy as np
import os
import pandas as pd
import numpy as np
import datetime as dt
import pymet
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt

MY_USERNAME = 'jwall'
MY_PASSWORD = getpass("User Name : %s " % MY_USERNAME )
erc = utils.initialize_er_client(er_server, MY_USERNAME, MY_PASSWORD)

obs_io = utils.ObservationsIO(erc=erc)
subjects_io = utils.SubjectsIO(erc=erc)


subjectgroup_name = 'MEP_elephants_everywhere'
include_inactive = True
start = dt.datetime(2011,1,1)
end = dt.datetime(2021,4,1)

df = obs_io.download_observations(subjectgroup_name=subjectgroup_name,
                                include_inactive=include_inactive,
                                start=start,
                                  end=end,)

out_folder = os.path.join('.', 'outputs', subjectgroup_name)
if not os.path.exists(out_folder ):
    os.makedirs(out_folder )
df.to_csv(os.path.join(out_folder, 'movdata_2019.csv'), header=True)

df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
df['fixtime'] = pd.to_datetime(df['fixtime'], utc=True)