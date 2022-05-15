# Boxer Generator
> **Created By:** Hasnaath Ali

# Contents
* [ Project Objective ](#obj)
* [ Project Planning ](#plans)
* [ Front End Design ](#FED)
* [ Testing and Automation](#TA)
* [ Future Development](#FD)

<a name="obj"></a>
## 1. Project Objective
In this project four service was created to containerise the boxer generator application. Service one 
renders the Jinja2 templates needed to interact with the application. In other words, service one is 
seen as the front-end-api which is responsible for communicating with the other 3 services and rendering 
an HTML template. Service two and three are used to generate objects. In this scenario of the boxer 
generator, service two generates a random boxer name and a random integer between 0-50 for its stamina. 
Service three however only generates a number between 0-50 which represents the boxer’s strength. 
Service four uses the results generated by service two and three to come out with how skilled the boxer 
is. So, if the boxer was Gennady Golovkin with a stamina of 35 and a strength of 48; service four 
determines that his level will be World Class which will be viewed in the front-end.

Requirements | Information
------------ | -------------
Kanban Board | Trello board for project tracking
Cloud Server | GCP for Virtual Machines
Feature Branching | Git is used for the Version Control system
Containerisation | Docker is used for the containerisation of services
Orchestration | Docker Swarm is used to replicate containers across multiple VM's
Reverse Proxy | NGINX allows the user to access the project using a reverse proxy server
CI Server | Jenkins is used for continuous integration
Webhooks | Triggers a Jenkins redeployment if the code gets changed
Configuration | Ansible is used for the configuration management and application-deployment


<a name="plans"></a>
## 2. Project Planning
Perhaps one of the key aspects of the project as the planning can inform the developer on 
what is there to implement, the user interaction with the application and what risks you may 
be faced with. But mainly a developer must keep track of what they are doing by using a 
project tracker of some sort.

### Project Tracker ###
There are many project management tools which could have been used to track the progress of 
the project; main ones being Jira and the Trello Board. This keeps the developer on track on
what needs to be completed and what is still remaining to complete. In this project the Trello
Board was used as seen in the image below.

![Trello](https://user-images.githubusercontent.com/101266487/168450738-986fcf7b-17a4-4981-81e1-6ae2338bd52f.JPG)

### Risk Assessment ###
When developing an application that requires user interaction, several issues which must be
addressed regarding the user’s privacy. A risk assessment had to be done for this project so 
some action could be taken to counteract any risk that could have cropped at anytime. A risk 
assessment also gives the developer a chance to perhaps implement any measures which could be taken 
before any risks actually happen. 

![Risk Assessment](https://user-images.githubusercontent.com/101266487/168496863-e0a7f272-f0fd-4ec5-8780-02afdead9d6d.JPG)

### Functional Requirements & User Stories ###
The functional requirements are how the application will function and highlighting all the 
features that will included in the application. Also, the functional requirements are primarily 
based at the use cases (the user, system functional requirements, goals) for this project and will 
guarantee a fully purposeful application.

![Functional requirements](https://user-images.githubusercontent.com/101266487/168497215-0b45eac8-b9b9-45ad-b1fc-3260240035af.JPG)

A user story is used to see the end goal which is expressed in the user’s perspective. Furthermore, a user story works well with 
the functional requirements stated above as it would give a developer whatmust be required for this project to be a success. A few
user stories are listed below:
- As a user I want to view the boxer's name so that I can see which boxer has been selected
- As a user I want to view the boxer's strength so that I can see the strength of the boxer
- As a user I want to view the boxer's stamina so that I can see the stamina of the boxer
- As a user I want to view the boxer's stats so that I can see what level my boxer is at
- As a user I want to click a button so that it generates a new boxer

### CI Pipeline ###
CI commonly known as Continuous Integration is the automated integration of code from the contributors into a project. The purpose 
of the CI pipeline is to allow developers to integrate newly generated code easily and frequently. This is achieved through the 
use of automated testing tools to check if the code is correct before fully integrating it. So, in this instance of the CI pipeline 
for this project, (in the picture below) code produced on the local machine by Python3 would get pushed to GitHub, which in turn is
pushed into Jenkins. Jenkins then automatically runs tests which produces a report. Since all the services in this project is 
containerised using docker, the images are pushed to Docker Hub. The images created are pushed to Ansible for the building orchestration. 
Continuous deployment by multiple replica’s created across Docker Swarm means that the application uses four VM’s where three VM’s are 
used for deployment.

![CI Pipeline2](https://user-images.githubusercontent.com/101266487/168499507-9c12c862-c01a-45b2-a544-1c38e3d66b7e.jpg)

<a name="FED"></a>
## Front End Design
