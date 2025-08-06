import pandas as pd
import cx_Oracle



# Fetch next N sequence values
num_rows = len(df)
cursor.execute(f"SELECT your_sequence.NEXTVAL FROM dual CONNECT BY LEVEL <= {num_rows}")
ids = [row[0] for row in cursor.fetchall()]

# Assign to DataFrame
df['id'] = ids

