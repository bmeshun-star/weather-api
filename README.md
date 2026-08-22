🌦️ Weather API — FastAPI, Docker & Docker Compose

A hands-on Python project built to learn the fundamentals of REST APIs, FastAPI, Docker, containerisation, multi-service applications and Docker Compose.

This project started as a simple Weather API running locally and evolved into a containerised application with a separate weather service and alert service.

It was my first time building this type of application, so the main focus was learning by doing — understanding what each component does, how the pieces connect, and how to use AI as a development assistant without relying on it to replace my own understanding.

⸻

📚 Table of Contents

* Project Overview + Tech Stack
* Quick Start
* Architecture
* Project Goals
* Manual Version
* Dockerising the App
* AI-Assisted Version
* Manual vs AI Comparison
* Alert Service
* Docker Compose
* Testing & Validation
* Screenshots
* Key Learnings
* Future Improvements
* Closing Summary

⸻

🚀 Project Overview + Tech Stack

The project provides weather information through a FastAPI application and demonstrates how the application can be developed, containerised and extended into a multi-service setup.

Tech Stack

Technology	Purpose
Python	Main programming language
FastAPI	API framework
Uvicorn	ASGI server used to run FastAPI
Requests	HTTP requests to external APIs
Open-Meteo	Weather data provider
Docker	Application containerisation
Docker Compose	Multi-service orchestration
Git/GitHub	Version control and project sharing

The project was developed in stages:

FastAPI API
    ↓
Local application
    ↓
Docker image
    ↓
Docker container
    ↓
Second service
    ↓
Docker Compose
    ↓
Multi-service application

⸻

⚡ Quick Start

Docker Compose

Clone the repository and move into the project directory:

git clone https://github.com/bmeshun-star/weather-api.git
cd weather-api

Build and start both services:

docker compose up --build

To run the services in the background:

docker compose up --build -d

Check the running services:

docker compose ps

Stop the services:

docker compose down

Services

Service	URL	Port	Purpose
Weather Service	http://localhost:8000/docs	8000	Retrieves weather information
Alert Service	http://localhost:8001	8001	Provides weather alert functionality

The Weather Service exposes FastAPI’s interactive Swagger documentation at:

http://localhost:8000/docs

Manual Run

Install the dependencies:

pip install -r requirements.txt

Run the Weather API:

uvicorn app:app --reload

The API will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

Test with curl

Test the main service:

curl http://localhost:8000/weather

If your API accepts a city parameter:

curl "http://localhost:8000/weather?city=London"

Test the alert service:

curl http://localhost:8001

For the exact alert endpoint implemented in the current version, see the Alert Service section below.

⸻

🏗️ Architecture

The application consists of two services managed by Docker Compose.

flowchart TD
    User[User / Client]
    Weather[Weather Service<br/>FastAPI :8000]
    API[Open-Meteo API]
    Alert[Alert Service<br/>FastAPI :8001]
    User -->|Weather request| Weather
    Weather -->|HTTP request| API
    API -->|Weather data| Weather
    Weather -->|Weather information| Alert
    Alert -->|Alert response| User

Weather Service

The Weather Service is the main FastAPI application.

Its responsibilities include:

* Receiving a weather request.
* Calling the external Open-Meteo API.
* Processing the response.
* Returning weather information to the client.

The service runs on:

http://localhost:8000

Interactive API documentation:

http://localhost:8000/docs

Alert Service

The Alert Service is a separate FastAPI service designed to evaluate weather information and return an alert when defined conditions are met.

It runs independently from the Weather Service on:

http://localhost:8001

The two services are managed together using Docker Compose.

Example JSON Response

A simplified weather response can look like:

{
  "current": {
    "temperature_2m": 18.5,
    "wind_speed_10m": 12.4
  }
}

The exact response depends on the weather data returned by the external API.

⸻

🎯 Project Goals

The main goals of this project were to:

* Build a simple REST API using FastAPI.
* Understand how an API receives and returns data.
* Make HTTP requests to an external weather API.
* Run the application locally using Uvicorn.
* Create a Dockerfile.
* Build a Docker image.
* Run the application inside a Docker container.
* Understand the difference between an image and a container.
* Introduce a second service.
* Use Docker Compose to manage multiple services.
* Understand basic service-to-service architecture.
* Compare a manually developed version with an AI-assisted version.
* Learn by building rather than only following theory.

⸻

🐍 Manual Version

The first version was built manually to understand the fundamentals before introducing AI assistance.

Flow

flowchart LR
    A[Python Code] --> B[FastAPI]
    B --> C[Uvicorn]
    C --> D[localhost:8000]
    D --> E[Weather Response]

Technology Used

* Python
* FastAPI
* Uvicorn
* Requests
* Open-Meteo API

The first objective was simply to get the API working locally and understand the basic request/response flow.

This gave me a foundation before moving into containerisation.

⸻

🐳 Dockerising the App

Once the API was working locally, I containerised the application.

Dockerfile Steps

The Dockerfile defines the instructions required to package the application into a Docker image.

The main steps are:

1. Select a Python base image.
2. Set the working directory.
3. Copy the application files.
4. Install dependencies.
5. Expose the application port.
6. Start the FastAPI application with Uvicorn.

Build the Docker Image

docker build -t weather-api .

Check the image:

docker images

Run the Container

docker run -p 8000:8000 weather-api

The API can then be accessed through:

http://localhost:8000/docs

Check the running container from another terminal:

docker ps

Basic Docker Relationship

Dockerfile
    ↓
Docker Image
    ↓
Docker Container
    ↓
Running Application

⸻

🤖 AI-Assisted Version

The second version was developed with AI assistance.

The purpose was not to have AI build the entire project without understanding it. Instead, AI was used as a development assistant to help explore ideas, troubleshoot problems and understand implementation options.

Location

The AI-assisted version is maintained in the project repository as the multi-service version of the application.

Enhancements

The AI-assisted version introduced:

* A separate Alert Service.
* Multiple FastAPI services.
* Separate Docker images/services.
* Docker Compose configuration.
* Multi-container execution.
* A clearer service-based architecture.

Build and Run

Build and start the services:

docker compose up --build

Run in detached mode:

docker compose up --build -d

Check the services:

docker compose ps

Stop the services:

docker compose down

⸻

⚖️ Manual vs AI Comparison

Feature	Manual Version	AI-Assisted Version
FastAPI	✅	✅
External weather API	✅	✅
Local execution	✅	✅
Docker	✅	✅
Docker image	✅	✅
Docker container	✅	✅
Alert Service	❌	✅
Docker Compose	❌	✅
Multiple services	❌	✅
AI assistance	❌	✅

Development Reflection

Building the first version manually helped me understand the fundamentals before adding more complexity.

Using AI in the second version made development faster and helped me explore solutions and troubleshoot issues. However, I still needed to understand the code and the commands being used.

For example, when Docker returned an error, understanding the difference between an image name and a container helped me identify whether the problem was with the application, the image or the command being used.

Key Finding

AI can accelerate development, but it does not replace understanding.

The most useful approach for me was to use AI to explain, suggest and troubleshoot while still testing the application myself and understanding why each component was needed.

⸻

🚨 Alert Service

The Alert Service is a separate FastAPI application running on port 8001.

Workflow

flowchart TD
    A[Weather Data] --> B[Alert Service]
    B --> C{Threshold Reached?}
    C -->|No| D[Normal Response]
    C -->|Yes| E[Weather Alert]

Endpoint

The Alert Service is exposed on:

http://localhost:8001

The exact endpoint should match the route defined in the Alert Service application.

For example:

curl http://localhost:8001/<alert-endpoint>

Alert Thresholds

The Alert Service evaluates weather conditions against thresholds defined in the application.

Example concept:

Weather value
     ↓
Compare with threshold
     ↓
Threshold exceeded?
     ↓
Yes → Generate alert
No  → Return normal response

Update this section with the exact threshold values and endpoint implemented in the current version of the project so the documentation always matches the code.

⸻

🐳 Docker Compose

Docker Compose is used to define and run the Weather Service and Alert Service together.

Services

The Compose configuration contains:

Service	Container Port	Host Port
Weather Service	8000	8000
Alert Service	8001	8001

Internal Networking

Docker Compose creates a network for the services defined in the Compose file.

This means the services can communicate using their Compose service names rather than relying on localhost between containers.

Conceptually:

Docker Compose Network
        │
        ├── weather-service:8000
        │
        └── alert-service:8001

Start the Services

docker compose up --build

Start in Background

docker compose up --build -d

Check Status

docker compose ps

View Logs

docker compose logs

View logs for the Weather Service:

docker compose logs weather-service

View logs for the Alert Service:

docker compose logs alert-service

Stop Services

docker compose down

⸻

🧪 Testing & Validation

The project was tested at different stages to make sure each part worked before moving to the next stage.

* FastAPI application starts successfully.
* Uvicorn starts the application.
* Weather endpoint can be accessed locally.
* Swagger documentation is available through /docs.
* External weather API requests return data.
* Docker image builds successfully.
* Docker container starts successfully.
* Container port is mapped to the local machine.
* Weather API can be accessed from the Docker container.
* Docker Compose builds the services.
* Weather Service starts successfully through Docker Compose.
* Alert Service starts successfully through Docker Compose.
* Both services can run at the same time.
* Service ports are exposed correctly.
* Docker Compose status can be checked with docker compose ps.
* Docker Compose logs can be inspected for troubleshooting.

⸻

📸 Screenshots

Screenshots can be added here to demonstrate the application at different stages.

FastAPI Swagger UI

<!-- ![FastAPI Swagger UI](screenshots/swagger.png) -->

Docker Container Running

<!-- ![Docker Container](screenshots/docker-container.png) -->

Docker Compose Services

<!-- ![Docker Compose](screenshots/docker-compose.png) -->

GitHub Repository

<!-- ![GitHub Repository](screenshots/github-repository.png) -->

⸻

🧠 Key Learnings

The main relationship I learned through this project was:

Python
  ↓
FastAPI
  ↓
Uvicorn
  ↓
Local Application
  ↓
Dockerfile
  ↓
Docker Image
  ↓
Docker Container
  ↓
Docker Compose
  ↓
Multiple Services

Developer Responsibilities

This project also helped me understand that using AI does not remove the need for developer understanding.

As the developer, I still need to:

* Understand what the application is doing.
* Understand the purpose of each service.
* Read and review generated code.
* Test the application.
* Understand error messages.
* Debug problems.
* Validate that commands work.
* Understand how containers are built and run.
* Understand how services communicate.
* Make decisions about the architecture.

The biggest lesson for me was that learning by building makes technical concepts easier to understand and remember.

⸻

🔮 Future Improvements

* Add stronger input validation.
* Add more comprehensive automated tests.
* Improve error handling.
* Add health-check endpoints.
* Improve the alert logic and configuration.
* Add environment variables for configuration.
* Add logging and better observability.
* Add CI/CD with GitHub Actions.
* Deploy the application to AWS.
* Explore infrastructure-as-code with Terraform.
* Improve service-to-service communication.
* Add monitoring and metrics.
* Improve the README with real project screenshots.
* Add API authentication if required for a future production version.

⸻

💭 Closing Summary

“This project started as a simple Weather API and became a practical introduction to APIs, Docker, containerisation and multi-service architecture. More importantly, it taught me that AI is most useful when it supports my learning and problem-solving rather than replacing my understanding.”

References

* FastAPI documentation — https://fastapi.tiangolo.com/
* Docker documentation — https://docs.docker.com/
* Docker Compose documentation — https://docs.docker.com/compose/
* Open-Meteo documentation — https://open-meteo.com/
* Python documentation — https://docs.python.org/3/

Built as a hands-on learning project — one step at a time. 🌦️🐳☁️
