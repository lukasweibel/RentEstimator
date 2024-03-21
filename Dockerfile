# Usage
# docker buildx build --platform linux/amd64 -t lukasweibel99/rentestimator . 
# docker buildx build --platform linux/arm64 -t lukasweibel99/rentestimator . --load 
# add envs command is on the desktop
# docker run --name rentestimator -p 9001:5000 -d lukasweibel99/rentestimator

# docker stop rentestimator  
# docker rm rentestimator  

FROM python:3.12.1

# Copy Files
WORKDIR /usr/src/app
#COPY backend/service.py backend/service.py
COPY . .
COPY frontend/public/build frontend/build


# Install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Docker Run Command
EXPOSE 80
ENV FLASK_APP=/usr/src/app/backend/service.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]