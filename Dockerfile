from python:3.12
run pip install poetry
copy . /src
workdir /src
run poetry install
expose 8501
entrypoint ["poetry","run","streamlit","run", "app.py","--server.port=8501","--server.address=0.0.0.0"]