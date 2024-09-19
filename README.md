# streamlit-app

# Calculator Streamlit App

This is a simple calculator implemented using Streamlit and containerized with Docker.

## How to Run

### Running Locally

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>

2. pip install -r requirements.txt
3. streamlit run calculator.py

### Running with Docker

docker build -t calculator .

docker run -p 8501:8501 calculator


