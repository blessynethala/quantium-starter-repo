# Quantium Starter Repo — Pink Morsel Sales Visualiser

## 📌 Project Overview

Quantium wants to understand how the sales of "Pink Morsels" were affected before and after a price increase. This project processes raw sales data, builds an interactive dashboard to visualise the trend, and includes automated tests to verify the dashboard works correctly.

## 🗂️ Project Structure

quantium-starter-repo/
│
├── data/                # Raw CSV sales data provided for the task
├── process_data.py      # Cleans and formats raw data into a single output CSV
├── app.py                # Dash application - interactive sales visualiser
├── test_app.py           # Automated test suite (pytest + Selenium)
├── requirements.txt      # Python dependencies
└── README.md

## ✅ Tasks Completed

 1. Data Processing ('process_data.py')
- Read multiple raw CSV files from the 'data/' folder.
- Filtered records to only include "Pink Morsel" sales.
- Calculated 'Sales = Quantity x Price' for each row.
- Combined all data into a single, clean, formatted output CSV with columns: 'Sales', 'Date', 'Region'.

 2. Data Visualisation ('app.py')
 Built an interactive Dash web application featuring:
- A header titled "Pink Morsel Sales Visualiser".
- A "line chart" showing sales over time, making it easy to see the impact of the price increase (which occurred on 15th Jan 2021).
- A "region filter" (radio buttons) allowing users to view sales data for a specific region ('north', 'east', 'south', 'west') or all regions combined.
- Custom styling for a clean, user-friendly interface.

 3. Automated Testing ('test_app.py')
 Using 'pytest' and 'dash.testing' (Selenium under the hood), the following was verified:
- The header element is present and displays the correct text.
- The sales line chart renders correctly on the page.
- The region filter/radio picker is present and functional.

All 3 tests pass successfully:
========================= 3 passed in ~23s =========================

## 🚀 How to Run

1. "Clone the repo"
  
   git clone https://github.com/blessynethala/quantium-starter-repo.git
   cd quantium-starter-repo
   
2. "Set up a virtual environment"
   
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # Mac/Linux

3. "Install dependencies"
   
   pip install -r requirements.txt

4. "Process the data"
  
   python process_data.py

5. "Run the visualiser"
  
   python app.py
  
   Then open the link shown in the terminal (e.g. `http://127.0.0.1:8050/`) in your browser.

## 🧪 How to Run Tests

   pytest test_app.py

## 🎓 Outcome

  Completed as part of the "Quantium Software Engineering Virtual Internship", covering:
- Data wrangling with Python (pandas)
- Building interactive dashboards with Dash/Plotly
- Writing automated UI tests with pytest and Selenium

---
*This repo was originally forked from the Quantium starter template for internship participants.*
