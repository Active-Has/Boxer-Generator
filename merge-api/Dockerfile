FROM python:3.8:latest
WORKDIR /merge-api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]