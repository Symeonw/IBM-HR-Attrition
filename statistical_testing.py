import pandas as pd
from prep import get_data
from stats import check_chi, check_normal_dist
import seaborn as sns
from scipy.stats import ttest_ind

df = get_data()

check_normal_dist(df)# 2 not normall distributed [employeecount, standardhours]
df.employeecount.describe() # all == 1
df.standardhours.describe()# all == 80
df.drop(columns=["employeecount", "standardhours"], inplace=True)

for col in df.columns:
    if df[col].dtype.name == "category":
        print(f"checking: {col}")
        check_chi(df.attrition, df[col])


# jobrole: dependent, H0 rejected.
# joblevel: dependent, H0 rejected.
# overtime: dependent, H0 rejected.
# department: dependent, H0 rejected.
# maritalstatus: dependent, H0 rejected.
# businesstravel: dependent, H0 rejected.
# jobinvolvement: dependent, H0 rejected.
# educationfield: dependent, H0 rejected.
# jobsatisfaction: dependent, H0 rejected.
# worklifebalance: dependent, H0 rejected.
# stockoptionlevel: dependent, H0 rejected.
# environmentsatisfaction: dependent, H0 rejected.

# relationshipsatisfaction: independent, failed to reject H0.
# performancerating: independent, failed to reject H0.
# education: independent, failed to reject H0.
# gender: independent, failed to reject H0.
# over18: independent, failed to reject H0.

for col in df.columns:
    if df[col].dtype.name != "category":
        print(f"checking: {col}")
        print(ttest_ind(df.attrition.cat.codes, df[col]))

# All below variables are statistically significant
# All T statistics are negative amounts. 
# age
# dailyrate
# distancefromhome
# employeenumber
# hourlyrate
# monthlyincome
# monthlyrate
# numcompaniesworked
# percentsalaryhike
# totalworkingyears
# trainingtimeslastyear
# yearsatcompany
# yearsincurrentrole
# yearssincelastpromotion
# yearswithcurrmanager

# Based on results we're going to drop the following columns:
# environmentsatisfaction, education, gender, over18, employeecount, and standardhours.

