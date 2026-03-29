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

---

---

# 📦 Fiyat Takip Projesi

Web'den ürün verisi çeken, yerel olarak kaydeden ve NumPy ile Pandas kullanarak istatistiksel raporlar üreten Python tabanlı bir ürün fiyat takip ve veri analiz sistemi.

---

## 🚀 Ne Yapıyor?

1. [books.toscrape.com](https://books.toscrape.com) adresinden (eğitim amaçlı açık kaynak site) ürün verisi **çeker**
2. Veriyi tekrar kayıt güvenli ekleme mantığıyla yerel bir CSV dosyasına **kaydeder**
3. Kaydedilen veriyi tekrar okuyup tipli Python nesnelerine **dönüştürür ve doğrular**
4. NumPy ve Pandas kullanarak fiyat **analizi yapar** ve rapor üretir

---

## 📁 Proje Yapısı

```
price_tracker_project/
│
├── main.py           # Giriş noktası — tüm modülleri yönetir
├── models.py         # Product dataclass
├── scraper.py        # Web scraping + iterator/generator
├── storage.py        # CSV okuma/yazma işlemleri
├── analysis.py       # NumPy + Pandas analiz ve raporlama
├── utils.py          # Decorator, higher-order fonksiyonlar, closure
├── exceptions.py     # Özel exception hiyerarşisi
├── data/
│   └── products.csv  # Kaydedilen ürün verileri
└── requirements.txt
```

---

## 🛠️ Kurulum

```bash
# Sanal ortam oluştur ve aktif et
python -m venv venv
venv\Scripts\activate  # Windows

# Bağımlılıkları kur
pip install -r requirements.txt
```

---

## ▶️ Kullanım

```bash
python main.py
```

Program çalıştırıldığında filtreleme için minimum fiyat eşiği girmeniz istenecektir.

---

## 📊 Örnek Çıktı (20 ürün çekildi)

```
Toplam çekilen ürün sayısı : 20
45£ ve üzeri ürün sayısı   : 10

--- Genel İstatistikler ---
Ürün sayısı        : 20
Ortalama fiyat     : £38.05
Maksimum fiyat     : £57.25
Minimum fiyat      : £13.99
Medyan fiyat       : £41.38

--- Rating'e Göre Ortalama Fiyat ---
Rating 1 → £40.02
Rating 2 → £36.83
Rating 3 → £42.32
Rating 4 → £31.11
Rating 5 → £39.75

--- En Pahalı 5 Ürün ---
1. Our Band Could Be Your Life   £57.25  ★3
2. Sapiens                       £54.23  ★5
3. Tipping the Velvet            £53.74  ★1
4. Scott Pilgrim's Precious...   £52.29  ★5
5. The Black Maria               £52.15  ★1
```

---

## 🧠 Kullanılan Temel Kavramlar

| Kavram | Dosya |
|---|---|
| Özel exception'lar ve hiyerarşi | `exceptions.py` |
| `@dataclass` | `models.py` |
| Decorator (`@timer`) | `utils.py` |
| Higher-order fonksiyonlar | `utils.py` |
| Closure | `utils.py` |
| Web scraping (requests + BS4) | `scraper.py` |
| Iterator protokolü (`__iter__`, `__next__`) | `scraper.py` |
| Generator (`yield`) | `scraper.py` |
| CSV okuma/yazma | `storage.py` |
| NumPy (mean, max, min, median) | `analysis.py` |
| Pandas (DataFrame, groupby, sort) | `analysis.py` |

---

## 👤 Yazar

**İbrahim Emre Yıldız**  
Bilgisayar Mühendisliği 4. Sınıf Öğrencisi — Çukurova Üniversitesi  
GitHub: [IbrahimEmreYildız](https://github.com/IbrahimEmreYildız)
