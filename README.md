# 🛒 Blinkit Real-Time Grocery Analytics - Executive Dashboard

![Blinkit Banner](background%20kpi.png)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-green.style=for-the-badge)](#license)

---

## 📌 Project Overview

This repository contains an **Executive Grocery Analytics Dashboard** for **Blinkit** (India's Last-Minute App). The project provides real-time business performance metrics, customer behavior analysis, item category sales trends, and store outlet efficiency across various tiers and sizes.

Built with an interactive **Streamlit** Web Application and backed by **Power BI DAX & SQL analytical queries**, this dashboard delivers actionable insights to optimize inventory, improve customer ratings, and maximize revenue across all distribution centers.

---

## 📊 Key Business Metrics (KPI Highlights)

| Metric | Value | Description |
|---|---|---|
| 💰 **Total Sales** | **$1.20 Million** | Overall revenue generated across all outlets |
| 📦 **Total Items Sold** | **8,523** | Total volume of grocery products ordered |
| 🏷️ **Average Sales** | **$141** | Average order transaction value |
| ⭐ **Average Rating** | **3.9 / 5.0** | Overall customer satisfaction rating |

---

## 🚀 Key Dashboard Features

- 🎯 **Executive KPI Cards**: Real-time snapshot of Total Sales, Average Sales, Total Items, and Average Customer Ratings.
- 📦 **Fat Content Breakdown**: Analysis of Low Fat vs Regular items impact on revenue.
- 🏪 **Outlet Size & Location Analysis**: Revenue distribution across High, Medium, Small outlets and Tier 1 / 2 / 3 cities.
- 📈 **Outlet Establishment Trend**: Historical sales trajectory by outlet establishment year (2011–2022).
- 🏷️ **Item Type Performance**: Granular category analysis (Fruits & Vegetables, Snack Foods, Household, Dairy, etc.).
- 🎛️ **Interactive Filters**: Dynamic filtering by Outlet Size, Location Tier, Item Fat Content, and Establishment Year range.

---

## 📂 Project Structure

```bash
Real-Time-Power-BI-Project-main/
│
├── app.py                         # Interactive Streamlit Web Application
├── BlinkIT Grocery Data.csv      # Dataset (CSV format)
├── BlinkIT Grocery Data.xlsx     # Dataset (Excel format)
├── Query Doc (1).docx             # DAX & SQL Analytical Queries Documentation
├── Blinkit Analysis.pptx          # Executive Presentation Deck
│
├── Sales.png                      # KPI Visual Asset - Total Sales
├── Avg Sales.png                  # KPI Visual Asset - Average Sales
├── Items.png                      # KPI Visual Asset - Total Items
├── rating (1).png                 # KPI Visual Asset - Rating
├── background kpi.png             # Dashboard Banner Header
└── README.md                      # Project Documentation
```

---

## 🛠️ Tech Stack & Prerequisites

- **Language**: Python 3.9+
- **Frontend Framework**: Streamlit
- **Data Manipulation**: Pandas, NumPy
- **Interactive Visualization**: Plotly Express, Plotly Graph Objects
- **BI Tools**: Power BI (DAX queries included in `Query Doc (1).docx`)

---

## 💻 Quick Start & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/Sagar-DataAnalyst/Blinkit-Real-Time-Grocery-Analytics-Executive-Power-BI-Dashboard.git
cd Blinkit-Real-Time-Grocery-Analytics-Executive-Power-BI-Dashboard
```

### 2. Install dependencies
```bash
pip install streamlit pandas plotly openpyxl
```

### 3. Launch the Streamlit App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🔍 Key Insights & Strategic Findings

1. **Top Selling Categories**: *Fruits & Vegetables* and *Snack Foods* represent over 30% of total revenue.
2. **Outlet Type Dominance**: **Supermarket Type 1** contributes the largest share of overall volume ($787.5K total sales).
3. **Location Tier Performance**: **Tier 3 cities** generated the highest overall sales volume, indicating strong demand in suburban and developing markets.
4. **Fat Content Preference**: **Low Fat** items lead customer demand, contributing ~$776K compared to ~$425K for Regular items.

---

## 👤 Author

Developed by **Sagar Maharana**  
- GitHub: [@Sagar-DataAnalyst](https://github.com/Sagar-DataAnalyst)  
- Email: `maharanasagar14312@gmail.com`

---
*If you find this repository helpful, please give it a ⭐ on GitHub!*