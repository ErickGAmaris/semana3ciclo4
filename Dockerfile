#
FROM python:3.11.0

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install -r /code/requirements.txt

#
COPY ./* /code/app

#
CMD ["uvicor", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
