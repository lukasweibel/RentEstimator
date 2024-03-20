# Usage
# docker buildx build --platform linux/amd64 -t weibelu1/restestimator . 
# docker run --name rentestimator -p 9001:80 -d weibelu1/restestimator

FROM python:3.12.1

# Copy Files
WORKDIR /usr/src/app
COPY backend/service.py backend/service.py
COPY frontend/public/build frontend/build

# Install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Docker Run Command
EXPOSE 80
ENV FLASK_APP=/usr/src/app/backend/service.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]