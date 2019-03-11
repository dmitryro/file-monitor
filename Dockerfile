FROM python:3.6.8-slim
ADD watched /watched
ADD monitor.py monitor.py 
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python, "/watched"]
