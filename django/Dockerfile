FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /portfolio
RUN apt-get update


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
