<p align="center">
  <a href="https://www.python.org/" target="blank"><img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" width="120" alt="Nest Logo" /></a>
</p>

# ETL Demo: From API -> DataFrame -> Parquet

This basic example of a ETL pipeline using Python

### How it works?

1. We **Extract** JSON data from an public API (`jsonplaceholder`)
2. It is transformed:
   - Key Fields selecction
   - Columns renamed
   - Email format standarized
3. Upload on Parquet file

### Run commands:

1. Clone the repository
2. Navigate to the cloned project by CMD.
3. Create the virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

```
venv\Scripts\activate
```

5. Install all the dependencies:

```
pip install -r requirements.txt
```

6. Run the project:

```
python src/main.py
```
