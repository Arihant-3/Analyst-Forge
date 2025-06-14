import os

def save_to_data(df, filename):
    # Go up two levels from current working directory (e.g., from Daily_Questions/)
    project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
    data_dir = os.path.join(project_root, 'Data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, filename), index=False)


# import sys
# import os

# # Add project root to sys.path
# project_root = os.path.abspath('..')  # goes from Daily_Questions/ to ANALYST FORGE/
# if project_root not in sys.path:
#     sys.path.append(project_root)

# # Now import works!
# from utils import save_to_data

