# Usage
# docker buildx build --platform linux/amd64 -t weibelu1/rentestimator . 
# docker buildx build --platform linux/arm64 -t weibelu1/rentestimator . --load 
# add envs command is on the desktop
# docker run --name rentestimator -p 9001:5000 -d weibelu1/rentestimator

# docker stop rentestimator  
# docker rm rentestimator  

FROM python:3.12.1

# Copy Files
WORKDIR /usr/src/app
#COPY backend/service.py backend/service.py
#COPY frontend/public/build frontend/build
COPY . .

# Install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Docker Run Command
EXPOSE 5000
ENV FLASK_APP=/usr/src/app/backend/service.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]