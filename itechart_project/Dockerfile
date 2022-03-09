FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /itechart_project
COPY requirements.txt /itechart_project/
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install uwsgi
RUN pip install -r requirements.txt
COPY . /itechart_project/


CMD ["uwsgi", "--ini", "itechart_project_uwsgi.ini"]