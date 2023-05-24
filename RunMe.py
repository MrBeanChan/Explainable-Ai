import subprocess
import os
# Run pip install command
# Install required libraries
libraries = [
    'pandas',
    'seaborn',
    'scikit-learn',
    'matplotlib',
    'numpy',
    'interpret',
    'shap',
    'xgboost',
    'streamlit'
]

for library in libraries:
    subprocess.check_call(['pip', 'install', library])

#Checking location just in case
current_directory = os.getcwd()
print(current_directory)

print("All required packages have been installed!")


# Run GUI
file_name = 'streamlit_app.py'
subprocess.check_call(['streamlit', 'run', file_name])