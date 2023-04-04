FROM python:3-alpine

# Create app directory
WORKDIR /neilolo

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

WORKDIR /neilolo/app

EXPOSE 5000
CMD ["sh", "-c", "exec gunicorn -w 4 -b 0.0.0.0:5000 app:app"]