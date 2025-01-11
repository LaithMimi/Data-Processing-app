import pandas as pd
import numpy as np
import plotly.express as px
import sys

sys.stdout.reconfigure(encoding='utf-8')

def load_data(file):
    
    if isinstance(file, str):  # Filepath scenario
        if file.endswith(".xlsx") or file.endswith(".xls"):
            df = pd.read_excel(file, engine='openpyxl')
        elif file.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            raise ValueError("Unsupported file type. Please upload a .csv or .xlsx file.")
    elif hasattr(file, 'name'):  # Streamlit UploadedFile object
        if file.name.endswith(".xlsx") or file.name.endswith(".xls"):
            df = pd.read_excel(file, engine='openpyxl')
        elif file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            raise ValueError("Unsupported file type. Please upload a .csv or .xlsx file.")
    else:
        raise ValueError("Invalid file input. Please provide a file path or an UploadedFile object.")
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def group_and_aggregate_data(df: pd.DataFrame, group_by_column: str, agg_func) -> pd.DataFrame:
    if group_by_column not in df.columns:
        raise ValueError("Group by column not found in dataframe")
    grouped_df = df.groupby(group_by_column).agg(agg_func).reset_index()
    return grouped_df

def remove_sparse_columns(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    sparse_columns = []
    for col in df.columns[2:]:
        if df[col].sum() < threshold:
            sparse_columns.append(col)

    df = df.drop(sparse_columns, axis=1)
    return df

def dimensionality_reduction(df: pd.DataFrame, num_components: int, meta_columns: list[str]) -> pd.DataFrame:
    metadata = df[meta_columns]
    features = df.drop(columns=meta_columns)

    # Center the data
    centered_features = (features - features.mean(axis=0))/features.std(axis=0)

    # Compute covariance matrix
    covariance_matrix = np.cov(centered_features, rowvar=False)

    # Perform eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # Select top components
    sorted_indices = np.argsort(eigenvalues)[::-1] # selecting the top eigenvalues
    top_eigenvectors = eigenvectors[:, sorted_indices][:, :num_components]

    # Project data onto new dimensions
    reduced_features = np.dot(centered_features, top_eigenvectors)
    reduced_data = np.real(reduced_features) # removes imaginary components

    # Create a DataFrame for the reduced data
    reduced_df = pd.DataFrame(reduced_data, columns=[f'PC{i+1}' for i in range(num_components)], index=df.index)

    return pd.concat([metadata, reduced_df], axis=1) # Combines PC's with metadata

def visualize_city_comparison(df: pd.DataFrame):
    df = group_and_aggregate_data(df, 'city_name', sum)
    df = remove_sparse_columns(df, 1000)
    reduced_df = dimensionality_reduction(df, 2, ['city_name', 'ballot_code'])

    fig = px.scatter(reduced_df, x='PC1', y='PC2',hover_data=['city_name'], title="City Comparison")
    fig.show()

def visualize_party_comparison(df: pd.DataFrame):
    df = group_and_aggregate_data(df, 'city_name', sum)
    df.drop(columns=['ballot_code'], inplace=True)
    transposed_df = df.set_index('city_name').T.reset_index().rename(columns={'index': 'party_name'})
    
    # Ensure city_name isn't in the columns or index
    transposed_df.columns.name = None
    if 'city_name' in transposed_df.columns:
        transposed_df.drop(columns=['city_name'], inplace=True)
    transposed_df = remove_sparse_columns(transposed_df, 1000)
    reduced_df = dimensionality_reduction(transposed_df, 2, ['party_name'])
    
    fig = px.scatter(reduced_df, x='PC1', y='PC2', hover_data=['party_name'], title="Party Comparison")
    fig.show()

df = load_data('../data/knesset_25.xlsx')

#visualize_city_comparison(df)
#visualize_party_comparison(df)
