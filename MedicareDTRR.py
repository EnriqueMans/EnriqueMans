#!/usr/bin/env python
# coding: utf-8

# In[48]:


import datetime
import pandas as pd
import numpy as np
import pandas as pd
import random
import string


# In[50]:


#create dtrr columns


# In[52]:


df_columns = [
        "Beneficiary ID", "Surname", "First Name", "Middle Initial", "Gender Code", "Date of Birth", 
        "Record Type", "Contract Number", "State Code", "County Code", "Disability Indicator", "Hospice Indicator",
                "Institutional Indicator", "ESRD Indicator", "Transaction Reply Code", 
        "Transaction Code", "Entitlement Type Code", "Effective Date", "WA Indicator", "Plan Benefit Package ID", "Filler", 
        "Transaction Date", "UI Initiated Change Flag", 
        "Positions Dependent on TRC value", "District Office Code", "Previous Part D Contract PBP Transfer", 
        "SEP Reason Code", "Filler", "Source ID", "Prior Plan Benefit Package ID", "Application Date", 
        "UI User Organization Designation", "Out of Area Flag", "Segment Number", "Part C Beneficiary Premium", 
        "Part D Beneficiary Premium",  "Election Type Code", "Enrollment Source Code", "Part D Opt-Out Flag",
        "Premium Withhold Option/Parts C-D", "Cumulative Number of Uncovered Months", "Creditable Coverage Flag", 
        "Employer Subsidy Override Flag", "Processing Timestamp", "End Date", "Submitted Number of Uncovered Months", "Ethnicity", "Preferred Language Other Than English", 
        "Accessible Format", "Secondary Drug Insurance Flag", "Secondary Rx ID", "Secondary Rx Group", "EGHP", 
        "Part D Low-Income Premium Subsidy Level", "Low-Income Co-Pay Category","Low-Income Period Effective Date", "Part D Late Enrollment Penalty Amount", "Part D Late Enrollment Penalty Waived Amount", "Part D Late Enrollment Penalty Subsidy Amount", "Low-Income Part D Premium Subsidy Amount", "Part D Rx BIN", "Part D Rx PCN", "Part D Rx Group", "Part D Rx ID", "Secondary Rx BIN", "Secondary Rx PCN", 
        "De Minimis Differential Amount", "MSP Status Flag", "Low Income Period End Date", "Low Income Subsidy Source Code","Enrollment Type Flag, PBP Level", "Application Date", "TRC Short Name", "Disenrollment Reason Code", "MMP Opt Out Flag", "Cleanup ID", "CARA Status Add/Update/Delete Flag", "POS Drug Edit Status", "Drug Class", 
        "POS Drug Edit Code", "CARA Status Notification Start Date", "CARA Status Implementation Start Date","CARA Status Notification End Date", "Hospice Provider Number", "IC Model Type Indicator", "IC Model End Date Reason Code", "IC Model Benefit Status", "Updated Medicaid Status for Community RAF Beneficiary", 
        "CARA Status Implementation End Date", "Prescriber Limitation", "Pharmacy Limitation", "Race", "Filler", "System Assigned Transaction Tracking ID", "Plan Assigned Transaction Tracking ID"
    ]


# In[53]:


# Setting the index to the first column 
dtrr_columns = pd.DataFrame(df_columns, columns=["Field Name"])
dtrr_columns.reset_index(drop=True, inplace=True)


# In[54]:


size_columns = [12, 12, 7, 1, 1, 8, 1, 5, 2, 3, 1, 1, 1, 1, 3, 2, 1, 8, 1, 3, 1, 8, 1, 8, 3, 8, 2, 6, 5, 3, 8, 2, 1, 3, 8, 8, 1, 1, 1, 1, 3, 1, 1, 15, 8, 3, 7, 1, 1, 1, 20, 15, 1, 3, 1, 8, 8, 8, 8,
             8, 6, 10, 15, 20, 6, 10, 8, 1, 8, 1, 1, 1, 15, 2, 1,10, 1, 1, 3, 3, 8, 8, 8, 13, 2, 2, 2, 1, 8, 1, 1, 16, 3, 11, 15]


# In[55]:


# Creating a dataframe with the list and assigning an index
df_size = pd.DataFrame(size_columns, columns=["Size"])


# In[60]:


df_size.reset_index(drop=True, inplace=True)


# In[61]:


dtrr_Specs = pd.concat([dtrr_columns, df_size], axis=1)


# In[62]:


df = pd.DataFrame(columns=df_columns)


# In[63]:


for idx, col in enumerate(df.columns):
    df[col] = df[col].apply(lambda x: x.ljust(size_columns[idx]))


# In[64]:


# Generating fake data based on the sizes provided in size_columns
def generate_fake_data(size):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

# Applying the fake data to each column based on its size
test_data = {df.columns[idx]: [generate_fake_data(size_columns[idx])] for idx in range(len(size_columns))}

# Creating the dataframe with fake data
test_data_df = pd.DataFrame(test_data)


# In[69]:


test_data_df


# In[ ]:





# In[75]:


file_content = ""

# Iterating over each row to format it according to size_columns
for index, row in test_data_df.iterrows():
    line = "".join(row[col].ljust(size_columns[idx]) for idx, col in enumerate(test_data_df.columns))
    file_content += line + "\n"

# Saving to a text file
file_path = "DTRR_File.txt"
with open(file_path, "w") as f:
    f.write(file_content)

file_path


# In[ ]:




