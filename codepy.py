import pandas as pd

# Sample PPX DataFrame with added PBP identifier
ppx_data = {
    'PBP': ['PBP001', 'PBP002', 'PBP003'],
    'Over65': ['', 'Y', 'N'],
    'HARP': ['', 'Y', 'N'],
    'ClassNumber': ['0000', '0043', '0000'],
    'LTSS': ['Y', 'N', 'Y'],
    'TermDate': ['20250101', '20250102', '20251231'],
    'EffDate': ['20240101', '20240105', '20240110']
}
ppx_df = pd.DataFrame(ppx_data)

# Sample DFLT DataFrame
dflt_data = {
    'Over65': ['Y', 'N', ''],
    'HARP': ['Y', '', 'N'],
    'ClassNumber': ['0000', '0043', '0000'],
    'LTSS_Indicator': ['Y', 'N', 'Y'],
    'EffectiveDate': ['20240101', '20240106', '20240111'],
    'Default_Eligible_Indicator': ['Y', 'N', 'Y']
}
dflt_df = pd.DataFrame(dflt_data)

# Convert date columns to datetime
ppx_df['EffDate'] = pd.to_datetime(ppx_df['EffDate'], format='%Y%m%d')
ppx_df['TermDate'] = pd.to_datetime(ppx_df['TermDate'], format='%Y%m%d')
dflt_df['EffectiveDate'] = pd.to_datetime(dflt_df['EffectiveDate'], format='%Y%m%d')

# Function to find matching PBP from PPX
ppx_df['EffDate'] = pd.to_datetime(ppx_df['EffDate'], format='%Y%m%d')
ppx_df['TermDate'] = pd.to_datetime(ppx_df['TermDate'], format='%Y%m%d')
dflt_df['EffectiveDate'] = pd.to_datetime(dflt_df['EffectiveDate'], format='%Y%m%d')

# Function to apply SQL-like logic and find PBP
def find_pbp(row):
    if row['Default_Eligible_Indicator'] != 'Y':
        return None
    matches = ppx_df[
        ((ppx_df['Over65'] == '') | (ppx_df['Over65'] == row['Over65'])) &
        ((ppx_df['HARP'] == '') | (ppx_df['HARP'] == row['HARP'])) &
        ((ppx_df['ClassNumber'] == '0000') | (ppx_df['ClassNumber'] == row['ClassNumber'])) &
        (ppx_df['LTSS'] == row['LTSS_Indicator']) &
        (row['EffectiveDate'] >= ppx_df['EffDate']) &
        (row['EffectiveDate'] <= ppx_df['TermDate'])
    ]
    if not matches.empty:
        return matches.iloc[0]['PBP']  # Return first match
    return None

# Apply function
dflt_df['PBP'] = dflt_df.apply(find_pbp, axis=1)

# Show result
print(dflt_df)
