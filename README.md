# Langchain RAG 

Install dependencies.

```python
pip install -r requirements.txt
```

Create the Chroma DB.

```python
python3 create_database.py
```

Query the Chroma DB.

```python
python3 query_data.py "Which is the first project mentioned and which technologies are used?"
```

You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.
