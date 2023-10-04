FROM python:3.11

#Set our working directory as app
WORKDIR /app 

# Copy the model's all files
COPY . .

#Installing Python packages through requirements.txt file
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#Exposing port 5000 from the container
EXPOSE 5000

#Starting the Python application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]