#!/bin/bash

# get user name
user=$(whoami)

# update and install required packages
sudo apt-get update

sudo apt-get install bzip2 libxml2-dev libsm6 libxrender1 libfontconfig1

# clone the project repo
git clone https://github.com/sabbih-shah/ML-Cloud-Deployment.git

# download miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh

# install miniconda
bash -b Miniconda3-py38_4.8.3-Linux-x86_64.sh

# set miniconda path variable
export PATH=/home/$user/miniconda3/bin:$PATH

# go to repository root
cd ML-Cloud-Deployment || { echo "Repo not cloned or incorrect path"; exit 1; }

# create conda environment
conda env create -f conda_env.yml

# activate conda environment
conda activate production_environment

# install NGINX
sudo apt-get install nginx-full

# start the nginx server
sudo /etc/init.d/nginx start

# remove default configuration file
sudo rm /etc/nginx/sites-enabled/default

# create a new site configuration file
sudo touch /etc/nginx/sites-available/ML-Cloud-Deployment

sudo ln -s /etc/nginx/sites-available/ML-Cloud-Deployment /etc/nginx/sites-enabled/ML-Cloud-Deployment

# copy server config
sudo -s cat gunicorn_server_config.txt >> /etc/nginx/sites-enabled/ML-Cloud-Deployment

# restart nginx server
sudo /etc/init.d/nginx restart

# change to gce directory
cd gce || { echo "incorrect path or not at repositry root"; exit 1; }

# bind gunicorn to app start point
gunicorn --bind 0.0.0.0:5000 app:app --daemon