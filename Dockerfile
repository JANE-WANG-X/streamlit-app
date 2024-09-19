# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Streamlit app will run
EXPOSE 8501

# Set the command to run the calculator.py script with Streamlit
CMD ["streamlit", "run", "calculator.py"]
