Data Processing App

This repository contains a Python script and a Streamlit user interface (UI) for processing and visualizing datasets. It supports uploading datasets in CSV or Excel format, applying data transformations (grouping, aggregation, dimensionality reduction), and visualizing the results interactively.

How to Run the Python Script

Before running the script, ensure you have the following installed:
* Python 3.7 or later
* Streamlit
* Pandas
* Plotly
* Openpyxl (for reading Excel files)

Running the Script
To run the script and launch the Streamlit UI, use the following command:

Open a terminal or command prompt.
Navigate to the directory containing the UI.py file.
Run the Streamlit application with the following command: python -m streamlit run UI.py

How to Interact with the Streamlit UI
Once the app is running, follow these steps:

1. Upload Your Dataset:
	In the UI, you'll see a button to upload your dataset. Click on the "Browse files" button and select either a CSV or Excel (.xlsx) 	file from your local system.
2. Choose Grouping and Aggregation:
	After uploading the dataset, you can choose a column to group by (e.g., a categorical column like 'city_name').
	Next, you can select an aggregation function (e.g., sum, mean) to apply to the data for each group and reduce the number of columns according to the specified threshold.
3. Set Dimensionality Reduction Parameters:
	The app allows you to select the number of principal components for dimensionality reduction (e.g., 2 components for a 2D 	visualization).
4. Choose the Type of Visualization:
	You can select whether to process and visualize the data city-wise or party-wise. This will change how the data is aggregated and 	visualized.
5. View Data and Visualizations:
	The processed data and the results of dimensionality reduction will be displayed in the app.
	A scatter plot will be shown, where each point represents a group (city or party), and the axes correspond to the principal 	components of the reduced data.

Files in the Repository

UI.py: The Streamlit user interface that handles file uploads, user input, and visualization.
dataAnalyst.py: The Python script that contains the logic for data processing (loading, grouping, dimensionality reduction, etc.).