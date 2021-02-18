# base image
FROM python:3.9-alpine

# copy stuff
COPY . .

# install dependencies
RUN pip install -r ./requirements.txt

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["api.py"]