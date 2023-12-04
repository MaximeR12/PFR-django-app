FROM python:3.10.11  
WORKDIR /myapp  

COPY requirements.txt /myapp

RUN pip install -r requirements.txt  

COPY . /myapp

CMD ["python", "myapp/manage.py", "runserver", "0.0.0.0:8000"]