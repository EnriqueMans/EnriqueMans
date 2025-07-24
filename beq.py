import pandas as pd
from datetime import datetime

# ---- Input Setup ----
file_control_number = 123456
today = datetime.now().strftime('%Y%m%d')

# ---- Header Row ----
header_row = {
    'SortOrder': 0,
    'FileRow': 'MMABEQRH' + 'H5599' + ' ' + today + str(file_control_number).zfill(9)
}

# ---- Simulated Detail Data ----
detail_data = [
    {'MBI': 'A123456789', 'DOB': '19800101', 'GenderCode': 'M'},
    {'MBI': 'B987654321', 'DOB': '19751212', 'GenderCode': 'F'}
]

# ---- Build Detail Rows ----
detail_rows = []
for idx, row in enumerate(detail_data):
    seq_num = str(idx + 1).zfill(7)  # 7-digit sequence number
    file_row = (
        'DTL01'
        + row['MBI'].ljust(12)
        + '9'.rjust(9)
        + row['DOB'].ljust(8)
        + row['GenderCode'].ljust(1)
        + seq_num
        + ' '.rjust(708)  # Padding to match expected file width
    )
    detail_rows.append({'SortOrder': idx + 1, 'FileRow': file_row})

# ---- Footer Row ----
footer_row = {
    'SortOrder': 9999999,
    'FileRow': 'MMABEQRT' + 'H5599' + ' ' + today + str(file_control_number).zfill(9)
}

# ---- Combine All Rows ----
all_rows = [header_row] + detail_rows + [footer_row]
df_beq = pd.DataFrame(all_rows).sort_values(by='SortOrder').reset_index(drop=True)

# ---- Optional: Add Sequence Number Column (zero-padded) ----
df_beq['SequenceNumber'] = df_beq.index + 1
df_beq['SequenceNumber'] = df_beq['SequenceNumber'].astype(str).str.zfill(7)

# ---- Write to Fixed-Width Text File ----
output_file = 'beq_request_file.txt'
with open(output_file, 'w') as f:
    for line in df_beq['FileRow']:
        f.write(f"{line}\n")

print(f"BEQ file written to: {output_file}")