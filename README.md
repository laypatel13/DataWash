# 🧹 DataWash

**Automated CSV Data Cleaning & Exploratory Data Analysis Web App**

DataWash is a Flask-based web application that lets you upload any CSV file and instantly get a cleaned version along with a full exploratory data analysis report with charts and statistics — no code required.

---

## 🚀 Live Demo

> Upload a CSV → Get clean data + full analysis in seconds.

---

## ✨ Features

- **Auto Data Cleaning**
  - Removes duplicate rows
  - Fixes missing values (median for numeric, mode for text)
  - Detects and removes outliers using IQR method
  - Auto-fixes data types

- **Exploratory Data Analysis**
  - Distribution histograms for all numeric columns
  - Box plots to visualize spread and outliers
  - Correlation heatmap
  - Value count bar charts for categorical columns
  - Full statistics table (mean, std, min, max, quartiles)

- **Download**
  - Download the cleaned CSV directly from the report page

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📁 Project Structure

```
datawash/
├── app.py
├── modules/
│   ├── init.py
│   ├── cleaner.py
│   └── analyzer.py
├── templates/
│   ├── index.html
│   └── report.html
├── static/
│   └── charts/
├── uploads/
│   └── .gitkeep
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation & Usage

```bash
# Clone the repo
git clone https://github.com/laypatel13/datawash.git
cd datawash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 📊 How It Works

1. Upload any CSV file from the homepage
2. DataWash automatically cleans the data
3. A full EDA report is generated with charts and stats
4. Download the cleaned CSV with one click

---

## 🔭 Future Plans

This is an actively developing project. Planned features include:

- [ ] Interactive charts using Plotly
- [ ] AI-powered data insights and suggestions
- [ ] Support for Excel (.xlsx) files
- [ ] Column-by-column cleaning controls
- [ ] Dark/Light theme toggle
- [ ] Deploy to web (Render / Railway)
- [ ] REST API endpoint for programmatic access
- [ ] ML-based outlier detection

---

## 👨‍💻 Author

**Lay Patel**
B.Tech CSE (AI/ML) | Adani University

- GitHub: [github.com/laypatel13](https://github.com/laypatel13)
- LinkedIn: [linkedin.com/in/laypatel13](https://www.linkedin.com/in/laypatel13)

---

## 📄 License

MIT License — feel free to use and build on this project!