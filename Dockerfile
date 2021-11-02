# python base image in the container from Docker Hub
FROM python:3.7.9-slim

# copy files to the /app folder in the container
COPY . .
COPY ./requirements.txt /src/requirements.txt
# set the working directory in the container to be /src
WORKDIR /src

# install the packages from the Pipfile in the container
RUN pip install -r requirements.txt
RUN pip install uvicorn


#RUN pipenv install --system --deploy --ignore-pipfile

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["python", "./main.py"]