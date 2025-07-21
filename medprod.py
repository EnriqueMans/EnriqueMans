import pandas as pd
import numpy as np
df_output = pd.DataFrame({
    'InsertDate': pd.to_datetime(['2025-07-21', '2025-07-21', '2025-07-21']),
    'Default_Eligible_Indicator': ['Y', 'Y', 'N'],
    'ClassNumber': ['0000', '1000', '0000'],
    'LTSSFlag': ['A', 'B', 'C'],
    'EffectiveDate': pd.to_datetime(['2025-07-01', '2025-07-02', '2025-07-03']),
})

# Crosswalk table (PPX)
df_pbp_xwalk = pd.DataFrame({
    'Over65': ['', '', 'X'],
    'HARP': ['', 'X', ''],
    'ClassNumber': ['0000', '1000', '0000'],
    'LTSS_Indicator': ['A', 'B', 'C'],
    'EffDate': pd.to_datetime(['2025-06-01', '2025-06-01', '2025-06-01']),
    'TermDate': pd.to_datetime(['2025-12-31', '2025-12-31', '2025-12-31']),
    'CSPT_ID': ['CSPT1', 'CSPT2', 'CSPT3'],
})
# Keep only rows where Default_Eligible_Indicator == 'Y'
df_output['MedicalProductNumber'] = None
# Function for row-by-row assignment (still simple)
def get_medical_product(row):
    if row['Default_Eligible_Indicator'] != 'Y':
        return np.nan
    match = df_pbp_xwalk[
        (df_pbp_xwalk['ClassNumber'] == row['ClassNumber']) &
        (df_pbp_xwalk['LTSS_Indicator'] == row['LTSSFlag'])
    ]
    if not match.empty:
        return match.iloc[0]['CSPT_ID']
    return np.nan

df_output['MedicalProductNumber'] = df_output.apply(get_medical_product, axis=1)
