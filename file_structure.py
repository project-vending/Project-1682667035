 
import os

# Define the root directory of the project
project_root = 'Real-time-weather-data-processing-platform'

# Define the subdirectories in the project
directories = ['data', 'processing', 'analytics', 'dashboard']

# Define the filenames for the empty files
files = {
    'data': ['nexrad.csv', 'goes.csv'],
    'processing': ['data_processing.py'],
    'analytics': ['weather_analytics.py'],
    'dashboard': ['streamlit_app.py']
}

# Create the project root directory
if not os.path.exists(project_root):
    os.mkdir(project_root)

# Create the subdirectories and empty files
for d in directories:
    dir_path = os.path.join(project_root, d)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    for f in files[d]:
        file_path = os.path.join(dir_path, f)
        open(file_path, 'w').close()
        
# Print success message
print(f'Created file structure and empty files for {project_root}')
