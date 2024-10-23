# vehalloc
A vehicle allocation application 

#### Folder Structure
Here the folders are managed to have a better framework to work with. The naming and the corresponding usage is shown below as a map,
* `conf`    => This is for managing app level configurations such as managing `db_connections`, `loggers`, `task_runners`, `test_suite_configurations` etc.
* `optim`   => This is for optimizing the application via caching or connection pooling etc.
* `repos`   => This is for mimicking `service-repositor-pattern` style.
* `routers` => To isolately manage routes and better management of the request handling.
* `schemas` => This is used for validating the data beforehand to avoid common issues regarding typing and misinformation.
* `utils`   => This will include helper functions.
* `logs`    => This contains the generated logs files. This is auto rotated and can be configured in the `conf/loggers.py` file.
#### Setup Guide
* clone the repo
* `cp .env.example .env` to create a `.env` file
* do `docker compose up` to start the application
* do `docker compose down` to stop the application
* do `docker compose up --build` to rebuild the application
[Note: Make sure the environment variables are set correctly in the `.env` file]

#### Furthur Development and Deployment Plans
* For a robust and secure application, we can use a combination of `JWT` and `OAuth2` for authentication and authorization.
* We can use complex logic to allocate vehicles based on various other factors.
* For deployment we can just use a basic `VPS` and deploy the application using `docker` and `docker-compose`.
* In that case, we can use a `CI/CD` pipeline to automate the deployment process. And use nginx as a reverse proxy to serve the application.

