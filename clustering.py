import pandas as pd
import prince
from prep import get_data
import numpy as np


df = get_data()
df.drop(columns=["environmentsatisfaction", "education"\
    , "gender", "over18", "employeecount", "standardhours"], inplace=True)

