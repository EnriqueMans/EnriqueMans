import pandas as pd

# Sample DataFrame representing EAF (replace with your actual data)
data = {
    'TRANSLEVELPLAN1': ['12J', 'AEP', 'UNK', 'LAW', 'MCD'],
    'TRANSLEVELPLAN3': ['DIF', '12J', 'AEP', 'UNK', 'ICE']
}
EAF = pd.DataFrame(data)

# Sample DataFrame representing ELX with CONNECTURECODE and corresponding mappings
elx_data = {
    'CONNECTcode': ['12J', 'AEP', 'DIF', 'LAW', 'MCD', 'ICE'],
    'EAMCODE': ['SEPS', 'AEP', 'SEPS', 'SEPS', 'SEPU', 'ICEP']
}
ELX = pd.DataFrame(elx_data)

# Create a dictionary from ELX DataFrame for mapping
connect_code_map = ELX.set_index('CONNECtcode')['EAMCODE'].to_dict()

# Update 'TRANSLEVELPLAN1' and 'TRANSLEVELPLAN3' in EAF using the mapping
EAF['TRANSLEVELPLAN1'] = EAF['TRANSLEVELPLAN1'].map(connect_code_map).fillna(EAF['TRANSLEVELPLAN1'])
EAF['TRANSLEVELPLAN3'] = EAF['TRANSLEVELPLAN3'].map(connect_code_map).fillna(EAF['TRANSLEVELPLAN3'])

# Display the updated DataFrame
import ace_tools as tools; tools.display_dataframe_to_user(name="Updated TRANSLEVELPLANs", dataframe=EAF)