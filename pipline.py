import pandas as pd
class csv_reader:
    def interpret(file_path):
        df = pd.read_csv(file_path)
        return df
