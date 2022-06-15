FROM ghcr.io/deephaven/server:0.13.0
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
