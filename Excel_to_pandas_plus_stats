import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Add path to file
file_path = r'path/to/file.xlxs'

# Run function with header_line set to the line of the header
def xlsx_processor(file_path, header_line):
    try:
        # Read file to pandas dataframe
        df = pd.read_excel(file_path, header=header_line)
        print('<< Successfull loaded file >>')
        
        # Describe basic statistics
        print(df.describe())

        # Print null counts
        print(f'\nNull values: \n{df.isnull().sum()}')

        # Display correlation heatmap of values
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.show()

    except Exception as e:
        # Display error if file cannot be loaded
        print(f'An error has occured: {e}')

# Run example file
xlsx_processor(file_path, 3)
