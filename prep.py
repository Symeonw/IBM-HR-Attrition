import pandas as pd

def get_data():
    df = pd.read_csv("data/data.csv")
    df.columns = [x.lower() for x in df.columns]
    to_cat = ["businesstravel", "attrition", "department", "education",\
        "educationfield", "environmentsatisfaction", "gender", "jobinvolvement"\
            , "joblevel", "jobrole", "jobsatisfaction", "maritalstatus"\
                ,"over18", "overtime", "performancerating", "relationshipsatisfaction",\
                    "stockoptionlevel", "worklifebalance"]
    for cat in to_cat:
        df[cat] = df[cat].astype("category")
    return df

df = get_data()
for col in df.columns:
    if col == "Age":
        df.loc[df.sample(frac=0.5).index, col] = pd.np.nan #Makes fake Nan's
    if col == "Education":
        df.loc[df.sample(frac=0.7).index, col] = pd.np.nan #Makes fake Nan's

col_nan_pct = df.isin([' ',np.nan]).mean() #Calculates percent of Nans
col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans