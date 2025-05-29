<p align="center">
  <a href="https://www.python.org/" target="blank"><img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" width="120" alt="Nest Logo" /></a>
</p>

# ETL Demo: From API -> DataFrame -> Parquet

This basic example of an ETL pipeline using Python

### 🔄 How it works?

1. We **Extract** JSON data from an public API (`jsonplaceholder`)
2. **Transform**:
   - Key Fields are selected.
   - Columns are renamed.
   - Email addresses are standardized (lowercased).
3. **Load**: The cleaned data is saved to a Parquet file.

### 🧪 How to run it:

1. Clone the repository
2. Navigate into the project directory.
3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

```
venv\Scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Run the project:

```
python src/main.py
```

### Output

A file named users.parquet will be created in the output/ directory.

### Requirements:

- Python 3.8+
- pandas, requests, pyarrow
