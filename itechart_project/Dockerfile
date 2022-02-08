FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /itechart_project
COPY requirements.txt /itechart_project/
RUN pip install -r requirements.txt
COPY . /itechart_project/

