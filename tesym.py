# Example dictionary
pbp_dict = {
    (2024, 'H12'): {'subgroup': 'SG1', 'group': 'G1'},
    (2025, 'H56'): {'subgroup': 'SG2', 'group': 'G2'},
}

# Step 1: Create a Series mapping (tuple key → subgroup/group)
subgroup_map = {k: v['subgroup'] for k, v in pbp_dict.items()}
group_map = {k: v['group'] for k, v in pbp_dict.items()}

# Step 2: Create a tuple Series for lookup
key_series = list(zip(df['year'], df['pbp']))

# Step 3: Map values
df['subgroup'] = pd.Series(key_series).map(subgroup_map)
df['group'] = pd.Series(key_series).map(group_map)