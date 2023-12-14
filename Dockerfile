# pull python base image
FROM python:3.9

# set working derictory
WORKDIR /training/

# copy the requirements.txt file
COPY requirements.txt ./

# install the dependencies
RUN pip install -r requirements.txt

# add app
COPY . /training/

