import pandas as pd


def preprocess(input_data):
    input_data_df = pd.DataFrame.from_dict(input_data)
    input_data_df['education'] = input_data_df['education'].apply(lambda x: 1 if x == 'Graduate' else 0)
    input_data_df['self_employed'] = input_data_df['self_employed'].apply(lambda x: 1 if x == 'Yes' else 0)
    input_data_df = input_data_df.drop('loan_id', axis = 1)
    input_data_df['asset_values']  = input_data_df['residential_assets_value'] + input_data_df['commercial_assets_value'] + input_data_df['luxury_assets_value'] + input_data_df['bank_asset_value']
    input_data_df.drop(['loan_status', 'loan_id' , 'residential_assets_value', 'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'], axis = 1, inplace = True)
    return input_data_df
        