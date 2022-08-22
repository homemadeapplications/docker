FROM python:3.10.5-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# EXPOSE 80
ENV DB_CHUCK_NORRIS toto
CMD ["python", "main.py"]
