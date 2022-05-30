FROM python:3.8-bullseye

ADD . /

RUN pip install -r requirements.txt

CMD ["python", "main.py"]