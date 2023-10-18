# InnoGlobalHack
--------------------
[winners solution on InnoGlobalHack](https://media.innopolis.university/news/innoglobalhack-final)

## Task
Currently, many mobile
applications face the need
identify users by their faces. Task
Facial identification is generally resolved. However
one of the pressing problems remains ensuring
reliability of such identification: it is necessary to distinguish
real face from static images, screenshots and
other types of fraud. As part of this assignment, you
authentication system to be developed
face images. The service being developed must be able to
work in picture mode - the user loads
photograph, receives a verdict.

## Demo
[Link to presentation demonstrating the solution](https://docs.google.com/presentation/d/135gFnvXTuMY0s2Gx6RO2vu4_WM_sKIHk/edit?usp=sharing&ouid=113877914532993525052&rtpof=true&sd=true)

## Solution
processing - network training, obtaining a dataset 
backend/app/main_model - first model  
backend/app/screen_detecting - [second model](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing/)  

<p float="left">
  <img src="https://github.com/BurykinaA/InnoGlobalHack/assets/92402616/851359f2-9678-48df-adbf-f6d39422c9bd" width="300">
  <img src="https://github.com/BurykinaA/InnoGlobalHack/assets/92402616/bcb9e9b0-f875-4760-a399-37d9ca937e75" width="350">
</p>



## Launching the application
This instruction will allow you to run the application using Docker on Linux and Windows operating systems.

> Make sure Docker is already installed on your machine. If Docker is not installed, you can download it from [official Docker website](https://www.docker.com/get-started/).

### Step 1: Clone the repository
```bash
git clone https://github.com/BurykinaA/InnoGlobalHack.git
cd InnoGlobalHack
```
### Step 2: Run Docker Compose
#### Linux:
```bash
docker-compose up --build
или  
docker-compose up --build -d
```

#### Windows:
```bash
docker-compose up --build 
или  
docker-compose up --build -d
```
### Step 3: Check functionality
The application should now be available and ready to use at:

**Linux**: 
http://localhost:5173

**Windows**: 
http://localhost:5173

### Step 4: Stop containers
This will shut down all containers associated with the application.
```bash
docker-compose down
```


## We're in media

https://habr.com/ru/companies/misis/articles/767384/  
https://m.gazeta.ru/amp/tech/news/2023/10/16/21512545.shtml  
https://misis.ru/news/8759/
