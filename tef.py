import pandas as pd
from datetime import datetime

# Simulated DFLT (Default Enrollment Output)
DFLT = pd.DataFrame({
    'ID': [1, 2, 3],
    'Over65': ['Y', 'N', 'Y'],
    'HARP': ['N', 'Y', 'N'],
    'ClassNumber': ['0000', '0033', '0054'],
    'LTSS_Indicator': ['N', 'Y', 'N'],
    'InsertDate': [datetime.today().date()] * 3,
    'Default_Eligible_Indicator': ['Y', 'Y', 'N'],
})

# Simulated PPX (Crosswalk)
PPX = pd.DataFrame({
    'PBP': ['001', '003', '004'],
    'Over65': ['Y', 'N', 'Y'],
    'HARP': ['N', 'Y', 'N'],
    'ClassNumber': ['0000', '0056', '0054'],
    'LTSS_Indicator': ['N', 'Y', 'N'],
    'EffectiveDate': [datetime(2023,1,1), datetime(2023,6,1), datetime(2023,1,1)],
    'TermDate': [datetime(2025,12,31), datetime(2024,12,31), datetime(2025,12,31)],
    'MedicalProductNumber': ['MCP1', 'MCP2', 'MCP3'],
})
# Loop through DFLT
for i, dflt_row in DFLT.iterrows():
    if (
        dflt_row['Default_Eligible_Indicator'] == 'Y'
    ):
        for j, ppx_row in PPX.iterrows():
            # Check all conditions (mimic SQL NVL/OR)
            if (
                (ppx_row['Over65'] == dflt_row['Over65'] or ppx_row['Over65'] == ' ')
                and (ppx_row['HARP'] == dflt_row['HARP'] or ppx_row['HARP'] == ' ')
                and (ppx_row['ClassNumber'] == dflt_row['ClassNumber'] or ppx_row['ClassNumber'] == '0000')
                and (ppx_row['LTSS_Indicator'] == dflt_row['LTSS_Indicator'])
                and (ppx_row['EffectiveDate'].date() <= ppx_row['EffectiveDate'].date() <= ppx_row['TermDate'].date())
            ):
                # If matched, update DFLT
                DFLT.at[i, 'PBPID'] = ppx_row['PBP']
                DFLT.at[i, 'MedicalProductNumber'] = ppx_row['MedicalProductNumber']
                break  # stop at first match

print(DFLT)
