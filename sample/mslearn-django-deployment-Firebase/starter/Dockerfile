# # Use the official lightweight Python image.
# # https://hub.docker.com/_/python
# FROM python:3.8

# # Allow statements and log messages to immediately appear in the Knative logs
# ENV PYTHONUNBUFFERED True

# # Copy local code to the container image.
# #ENV dog_shelters /app
# WORKDIR /app
# COPY requirements.txt requirements.txt

# #ENV PORT 8080

# # Install production dependencies.
# RUN pip install -r requirements.txt

# COPY . .

# ENV PORT=8080
# # Run the web service on container startup. Here we use the gunicorn
# # webserver, with one worker process and 8 threads.
# # For environments with multiple CPU cores, increase the number of workers
# # to be equal to the cores available.
# #CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

# CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT --workers 1 -threads 8 app:app
# #EXPOSE 8080
# #CMD python manage.py runserver 0.0.0.0:$PORT

# #ENTRYPOINT [ "python" "manage.py"]


# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
#CMD exec gunicorn project.wsgi:application --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
CMD python manage.py runserver 0.0.0.0:$PORT