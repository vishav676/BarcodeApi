FROM python:3.8.9
ENV PYTHONUNBUFFERED=1
WORKDIR /BarcodeApi
ADD . /BarcodeApi
COPY requirements.txt /BarcideApi/
RUN pip install -r requirements.txt
COPY . /BarcodeApi/
