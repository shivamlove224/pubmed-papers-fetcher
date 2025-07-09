# PubMed Papers Fetcher

A Python command-line tool that fetches research papers from PubMed and filters for papers with at least one author affiliated with a pharmaceutical or biotech company.

---

## 🔧 Features
- Uses **PubMed API** to search and fetch paper metadata
- Detects **non-academic authors** based on affiliation keywords
- Outputs results to **console or CSV file**
- CLI built with **argparse**
- Fully managed using **Poetry**

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pubmed-papers-fetcher.git
cd pubmed-papers-fetcher
```

### 2. Install dependencies with Poetry
```bash
poetry install
```

---

## 🚀 Usage

### Basic usage (print to console)
```bash
poetry run get-papers-list "cancer AND therapy"
```

### Save results to CSV
```bash
poetry run get-papers-list "covid-19 vaccine" -f results.csv
```

### Debug mode
```bash
poetry run get-papers-list "immunotherapy" -d
```

---

## 🧠 How It Works
- Papers are fetched from PubMed using the `esearch` and `efetch` APIs
- Author affiliations are scanned for common **non-academic** keywords (e.g., `biotech`, `pharma`, `LLC`)
- Academic institutions (e.g., `university`, `hospital`, `institute`) are filtered out
- Corresponding author emails are heuristically extracted from affiliation strings

---

## 🗂 Project Structure
```
pubmed_papers_fetcher/
├── cli.py
├── papers/
│   ├── fetcher.py
│   ├── parser.py
│   └── utils.py
├── pyproject.toml
├── README.md
```

---

## 🔗 Tools & Resources
- [PubMed API (NCBI eUtils)](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Poetry](https://python-poetry.org/)
- [Requests Library](https://docs.python-requests.org/)

---

## 🧪 Bonus (Optional)
To publish your module to [TestPyPI](https://test.pypi.org/):
```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry publish -r test-pypi --build
```

---

## 🪪 License
MIT License

---

## 👨‍💻 Author
Your Name - [GitHub Profile](https://github.com/your-username)

---
