# 📊 Data Insight Hub – Interactive Dataset Explorer with Streamlit

Welcome to your all-in-one platform for **exploring, transforming, and visualizing** data with ease! This repository brings together the power of **Python**, the flexibility of **Streamlit**, and the clarity of **Plotly** to turn raw CSV or Excel files into insightful, dimensionality-reduced plots – all from a sleek, interactive interface.

## 🚀 What This App Does

With just a few clicks, you can:

* Upload datasets (`.csv` or `.xlsx`)
* Group and aggregate data on the fly (e.g., by city or party)
* Reduce dimensionality for intuitive 2D visualizations
* Explore trends and patterns with interactive scatter plots

Ideal for analysts, students, or curious minds who want quick insights without coding!

---

## 🛠️ Getting Started

### 🔧 Prerequisites

Ensure you have the following installed:

* Python ≥ 3.7
* `streamlit`
* `pandas`
* `plotly`
* `openpyxl` (for Excel support)

Install them with:

```bash
pip install streamlit pandas plotly openpyxl
```

### ▶️ Launch the App

1. Open a terminal
2. Navigate to this project folder
3. Run:

```bash
python -m streamlit run UI.py
```

---

## 🧭 How to Use the App

### 1. 📂 Upload Your Dataset

Upload a `.csv` or `.xlsx` file directly from the interface.

### 2. 🧮 Group & Aggregate

Choose a column to group by (like `city_name`) and pick an aggregation method (sum, mean, etc.). You can also limit the number of columns used.

### 3. 🔻 Dimensionality Reduction

Choose how many **principal components** (e.g., 2D or 3D) to reduce the data to for visualization.

### 4. 🤠 Select a Perspective

Toggle between **city-wise** or **party-wise** aggregation to gain different analytical views.

### 5. 📈 Explore Results

* See the grouped and reduced dataset in table format.
* Dive into an interactive scatter plot where each point represents a group in the reduced feature space.

---

## 📁 Project Structure

| File             | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| `UI.py`          | The Streamlit front-end: handles user inputs, file uploads, and plots.      |
| `dataAnalyst.py` | Backend logic: handles loading, transformation, grouping, PCA, and cleanup. |

---


