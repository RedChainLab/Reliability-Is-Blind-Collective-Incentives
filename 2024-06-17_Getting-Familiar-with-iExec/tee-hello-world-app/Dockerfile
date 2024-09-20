FROM python:3.10-alpine

### install python dependencies if you have some
RUN pip3 install pyfiglet

COPY ./src /app
ENTRYPOINT ["python3", "/app/app.py"]
