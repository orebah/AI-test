FROM nvidia/cuda:12.4.1-base-ubuntu24.04
RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt .
COPY main.py .

RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages

CMD ["python3", "main.py"]