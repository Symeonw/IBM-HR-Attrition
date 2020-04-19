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

