# 🛒 Amazon Product Data Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Library-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green.svg)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel%20Files-brightgreen.svg)
![Excel](https://img.shields.io/badge/Excel-Data%20Export-217346.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Github](https://img.shields.io/badge/API-GitHub-black.svg)
![Data Cleaning](https://img.shields.io/badge/Focus-Data%20Analysis-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 📌 Project Overview

This project analyzes product data from **Amazon** to understand market trends, pricing strategies, and customer engagement patterns. The data was collected through web scraping and processed to extract actionable business insights.

The main goals of this analysis were to:
- 📊 **Explore** the relationship between product price, rating, and popularity.
- 💰 **Identify** the most common price ranges and potential market gaps.
- 🏷️ **Discover** which brands dominate the market and how they are priced.
- 🔍 **Find outliers** and products with exceptional performance.

This project demonstrates practical skills in:
- Web Scraping (`BeautifulSoup`, `Requests`)
- Data Cleaning and Preprocessing (`Pandas`, `NumPy`)
- Exploratory Data Analysis (EDA)
- Data Visualization (`Matplotlib`, `Seaborn`)
- Statistical Analysis and Insight Generation

---

## 📂 Dataset

The dataset was collected by scraping product pages on Amazon.

Each product entry contains the following information:
- `Product Name`
- `Price` (in USD)
- `Rating` (out of 5 stars)
- `Number of Reviews`
- `Availability` (In Stock / Out of Stock)
- `ASIN` (Amazon Standard Identification Number)
- `Product Link`

**Dataset size:**
- **500 products**
- **6 key features**
- **0 duplicate records** (after cleaning)

---

## 🛠 Technologies Used

| Tool | Purpose |
| :--- | :--- |
| **Python** | Programming language |
| **BeautifulSoup** | HTML parsing for web scraping |
| **Requests** | HTTP requests for data collection |
| **Excel** | Manual data review and editing |
| **Pandas** | Data manipulation and cleaning |
| **NumPy** | Numerical analysis |
| **Matplotlib** | Data visualization |
| **Jupyter Notebook** | Analysis environment |

---

## 🔄 Project Workflow
Amazon Product Pages
↓
Web Scraping
↓
Raw Data (Excel)
↓
Data Cleaning
↓
Feature Engineering
↓
Exploratory Analysis
↓
Visualizations
↓
Key Insights

---

## 🧹 Data Cleaning and Feature Engineering

The dataset was processed to ensure accuracy and consistency:

1.  **Price Formatting:** Cleaned the price strings to convert them to a consistent numeric format (float), removing currency symbols and commas.
2.  **Rating Handling:** Converted rating strings to numeric values for statistical analysis.
3.  **Review Count:** Cleaned and standardized the review count column.
4.  **Missing Values:** Checked and handled any missing or null entries.

**Results:**
- ✅ Consistent data types across all columns.
- ✅ No duplicate product entries.
- ✅ Ready for exploratory analysis.

---

## 📊 Exploratory Data Analysis

### 💲 Price Distribution

![Price Distribution](/charts/price_distribution.png)

The distribution of laptop prices shows a clear market concentration. The majority of competitors' products are priced in the **$100–$400 range**, indicating that this budget segment is the most competitive area of the market. In contrast, very few products are priced at **$3,700 and above**, suggesting that competition in this high-end premium segment is weakest and potentially underserved.

### ⭐ Price vs. Rating Correlation

![Price vs. Rating Correlation](/charts/price_vs_rating.png)

The analysis reveals a strong positive correlation between price and rating. Expensive laptops almost never receive low ratings, while most budget models score below 4–4.5. This confirms a clear link between price and quality, with customers consistently more satisfied by higher-priced products. Budget laptops with top ratings are rare exceptions..

### 🏆 Top Performing Products

- **Most Reviewed:** The product with the most reviews has over **2,000 reviews**, indicating strong market presence.

---

## 🔍 Key Insights

### 1. Competitive Pricing Zone
Most products are clustered in the **$100–$400 price range**, which is the most competitive zone for sellers. To stand out, a product would need a strong differentiator, such as a unique feature or significantly higher rating.

### 2. Price is the Main Driver of Satisfaction
The strong correlation between price and rating indicates that customers do equate higher price with higher quality in this product category. This limits opportunities for new entrants, as competing on quality at a lower price point is difficult given that budget laptops rarely achieve high ratings.

### 3. The Power of Reviews
Popular products with thousands of reviews solidify their market leadership. The analysis shows that achieving a high number of reviews is crucial for market dominance, as products with fewer reviews have a much lower chance of being discovered.

---

## 📁 Project Structure
```text
amazon_analysis/
│
├── scraper/ # Web scraping scripts
│ └── amazon_scraper.py
│
├── charts/ # Generated visualizations
│ ├── price_distribution.png
│ ├── price_vs_rating.png
│ └── reviews_vs_rating.png
│
├── analysis.ipynb # Jupyter Notebook with full analysis
├── products.xlsx # Final cleaned and processed dataset
├── README.md # Project overview
└── requirements.txt # List of Python dependencies
```
---

## 🎯 Conclusion

This project successfully demonstrates a complete workflow for web scraping, data cleaning, and performing exploratory data analysis on an e-commerce dataset. The analysis of Amazon product data reveals several insights:
- The market has a highly competitive pricing sweet spot.
- Pricing strategy must be built on the clear "higher price = higher quality" assumption
- Building a strong review base is critical for long-term success and visibility.

This project serves as a showcase of data science skills applied to a real-world e-commerce use case, capable of providing actionable intelligence for market entry or pricing strategy refinement.

---
