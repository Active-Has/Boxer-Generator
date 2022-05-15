FROM python:3.8:latest
WORKDIR /stamina-api 
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 5000 
ENTRYPOINT ["python3", "app.py"]