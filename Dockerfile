FROM python:3.11

#Set our working directory as app
WORKDIR /app 

# Copy the model's all files
COPY . .

#Installing Python packages through requirements.txt file
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#Exposing port 5000 from the container
EXPOSE 3000

#Starting the Python application
CMD ["python3", "app.py"]
