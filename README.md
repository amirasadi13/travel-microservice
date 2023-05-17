# Travel Microservice System

<div>
  <img src="https://img.freepik.com/free-vector/hand-drawn-travel-background_52683-85109.jpg" style="margin:auto;"/>
</div>

<div>
  # Travel Microservice Project is created to book flights and hotels 
</div>


# What's Travel Project:
  - we developed two services as Travel-admin-backend and Travel-users-backend, both services have same models
    - Travel Admin Backend is for all the operators and managers, we use the service to handle incoming data and data actions
    - Travel Users Backend is for all the users who are looking for flights and hotels to booked, this service is listining to Travel Admin Backend on data actions. 


# What's New In This Project:
  - publish data from travel admin service to travel users service (Kafka)
  - used signals to handle models actions 


# How To Run This Project:
  - clone the project from:
    - https://github.com/amirasadi13/travel-microservice.git
  - run docker on your system or download from https://docs.docker.com/engine/install/
  - attention to services proriorit
  - run commands:
    - docker compose build 
    - docker compose up


# In future
  - TODO complete Apis
  - TODO add more operator types, add diffrent rules and permissions on travel admin backend 
  - TODO add redis chache system on travel users Apis
