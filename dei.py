import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Create fake output table
output = pd.DataFrame({
    'ID': [1, 2, 3],
    'CLASSNUMBER': ['CSCS01', 'CSCS02', 'CSCS03'],
    'LTSS_Indicator': ['N', 'Y', 'N'],
    'InsertDate': [pd.Timestamp.today().normalize()] * 3,
    'Default_Eligible_Indicator': [None] * 3
})

# Create fake xwalk table
xwalk = pd.DataFrame({
    'CLASSNUMBER': ['CSCS01', 'CSCS02'],
    'LTSS_INDICATOR': ['N', 'Y'],
    'EligibleFlag': ['Y', 'N'],
    'EffectiveDate': [
        pd.Timestamp.today() - pd.Timedelta(days=10),
        pd.Timestamp.today() - pd.Timedelta(days=10)
    ]
})
# Create a lookup dictionary keyed by (CLASSNUMBER, LTSS_INDICATOR)
xwalk_lookup = {
    (row.CLASSNUMBER, row.LTSS_INDICATOR): row.EligibleFlag
    for _, row in xwalk.iterrows()
}
def assign_flag(row):
    key = (row['CLASSNUMBER'], row['LTSS_Indicator'])
    return xwalk_lookup.get(key, 'X')  # default to 'X' if no match

# Apply the function row-wise
output['Default_Eligible_Indicator'] = output.apply(assign_flag, axis=1)

print("\n🔷 Final Output:\n", output)
