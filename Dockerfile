FROM python:3.6-slim
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY ./src /
EXPOSE 80
CMD ["python", "/foo/bar.py"]
