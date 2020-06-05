FROM python:3
ENV PYTHONUNBUFFERED 1

RUN addgroup --system django \
    && adduser --system --ingroup django django

RUN mkdir /backend
WORKDIR /backend

COPY ./docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown django /start

COPY requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/

