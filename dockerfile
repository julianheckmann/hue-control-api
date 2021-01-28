FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["api.py"]
ENTRYPOINT ["python3"]