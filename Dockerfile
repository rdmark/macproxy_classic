FROM python:alpine3.22
ENV PORT="5001"
WORKDIR /macproxy
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 proxy.py --port ${PORT}
