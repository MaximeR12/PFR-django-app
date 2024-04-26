FROM python:3.10.9 

WORKDIR /app  

COPY requirements.txt /app

RUN pip install -r requirements.txt  

COPY . /app

RUN python manage.py switchenv DJANGO_ENV prod
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]