FROM python:3.9

WORKDIR /usr/src/app
ENV TZ="Europe/Stockholm"

RUN pip install -U pip wheel setuptools
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]