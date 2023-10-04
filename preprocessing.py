import pandas as pd


def preprocess(input_data):
    input_data_df = pd.DataFrame.from_dict(input_data)
    input_data_df['education'] = input_data_df['education'].apply(lambda x: 1 if x == 'Graduate' else 0)
    input_data_df['self_employed'] = input_data_df['self_employed'].apply(lambda x: 1 if x == 'Yes' else 0)
    input_data_df = input_data_df.drop('loan_id', axis = 1)
    return input_data_df
        