import streamlit as st
import plotly.express as px
from dataAnalyst import load_data, group_and_aggregate_data, remove_sparse_columns, dimensionality_reduction

# Streamlit App
st.title("📊 Interactive Data Analysis and Visualization Tool")

# File Upload
uploaded_file = st.file_uploader("Upload your dataset (.csv or .xlsx)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
        st.write("### Preview of Dataset")
        st.dataframe(df.head())
        
        # Sidebar Settings
        st.sidebar.header("⚙️ Settings")
        group_by_column = st.sidebar.selectbox("Select a column to group by", df.columns)
        aggregation_func = st.sidebar.selectbox("Select aggregation function", ["sum", "mean", "max", "min"])
        threshold = st.sidebar.slider("Sparse Column Threshold", 0, 20000, 1000)
        num_components = st.sidebar.slider("Number of Principal Components", 1, 10, 2)
        visualization_type = st.sidebar.radio("Visualization Type", ["City-wise", "Party-wise"])
        
        if st.sidebar.button("Process Data"):
            df_grouped = group_and_aggregate_data(df, group_by_column, aggregation_func)
            df_sparse_removed = remove_sparse_columns(df_grouped, threshold)
            
            if visualization_type == "City-wise":
                meta_columns = ['city_name', 'ballot_code'] if 'city_name' in df.columns else [group_by_column]
                reduced_df = dimensionality_reduction(df_sparse_removed, num_components, meta_columns)
                fig = px.scatter(reduced_df, x='PC1', y='PC2', hover_data=['city_name'], title="City Comparison")
            
            elif visualization_type == "Party-wise":
                df_sparse_removed.drop(columns=['ballot_code'], errors='ignore', inplace=True)
                transposed_df = df_sparse_removed.set_index('city_name').T.reset_index().rename(columns={'index': 'party_name'})
                reduced_df = dimensionality_reduction(transposed_df, num_components, ['party_name'])
                fig = px.scatter(reduced_df, x='PC1', y='PC2', hover_data=['party_name'], title="Party Comparison")
            
            st.write("### Reduced Dataset")
            st.dataframe(reduced_df)
            
            st.write("### Visualization")
            st.plotly_chart(fig)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
