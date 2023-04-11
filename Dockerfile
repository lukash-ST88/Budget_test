FROM python:3.9

RUN mkdir -p /app/budget-test
WORKDIR /app/budget-compressed

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
VOLUME ["/app/budget-test"]
EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]