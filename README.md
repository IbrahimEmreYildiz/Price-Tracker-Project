# 📦 Price Tracker Project

A Python-based product price tracking and data analysis system that scrapes product data from the web, stores it locally, and generates statistical reports using NumPy and Pandas.

---

## 🚀 What It Does

1. **Scrapes** product data from [books.toscrape.com](https://books.toscrape.com) (a public training site)
2. **Saves** the data to a local CSV file with duplicate-safe append logic
3. **Loads** and validates the stored data back into typed Python objects
4. **Analyzes** prices using NumPy and Pandas to generate reports

---

## 📁 Project Structure

```
price_tracker_project/
│
├── main.py           # Entry point — orchestrates all modules
├── models.py         # Product dataclass
├── scraper.py        # Web scraping logic + iterator/generator
├── storage.py        # CSV read/write operations
├── analysis.py       # NumPy + Pandas analysis and reporting
├── utils.py          # Decorator, higher-order functions, closures
├── exceptions.py     # Custom exception hierarchy
├── data/
│   └── products.csv  # Persisted product records
└── requirements.txt
```

---

## 🛠️ Setup

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

You will be prompted to enter a minimum price threshold for filtering products.

---

## 📊 Sample Output (20 products scraped)

```
Total products scraped : 20
Products above £45     : 10

--- General Statistics ---
Product count          : 20
Average price          : £38.05
Max price              : £57.25
Min price              : £13.99
Median price           : £41.38

--- Average Price by Rating ---
Rating 1 → £40.02
Rating 2 → £36.83
Rating 3 → £42.32
Rating 4 → £31.11
Rating 5 → £39.75

--- Top 5 Most Expensive ---
1. Our Band Could Be Your Life   £57.25  ★3
2. Sapiens                       £54.23  ★5
3. Tipping the Velvet            £53.74  ★1
4. Scott Pilgrim's Precious...   £52.29  ★5
5. The Black Maria               £52.15  ★1
```

---

## 🧠 Key Concepts Practiced

| Concept | Where |
|---|---|
| Custom exceptions & hierarchy | `exceptions.py` |
| `@dataclass` | `models.py` |
| Decorator (`@timer`) | `utils.py` |
| Higher-order functions | `utils.py` |
| Closures | `utils.py` |
| Web scraping (requests + BS4) | `scraper.py` |
| Iterator protocol (`__iter__`, `__next__`) | `scraper.py` |
| Generator (`yield`) | `scraper.py` |
| CSV read/write | `storage.py` |
| NumPy (mean, max, min, median) | `analysis.py` |
| Pandas (DataFrame, groupby, sort) | `analysis.py` |

---

## 👤 Author

**İbrahim Emre Yıldız**  
4th Year Computer Engineering Student — Çukurova University  
GitHub: [IbrahimEmreYildız](https://github.com/IbrahimEmreYildız)
