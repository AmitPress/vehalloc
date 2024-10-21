# vehalloc
A vehicle allocation application 

#### Folder Structure
Here the folders are managed to have a better framework to work with. The naming and the corresponding usage is shown below as a map,
* `conf` => This is for managing app level configurations such as managing `db_connections`, `loggers`, `task_runners`, `test_suite_configurations` etc.
* `optim` => This is for optimizing the application via caching or connection pooling etc means
* `repos` => This is for mimicking `service-repositor-pattern` style
* `routers` => To isolately manage routes and better management of the request handling
* `schemas` => This is used for validating the data beforehand to avoid common issues regarding typing and misinformation
* `utils` => This will include helper functions

#### Setup Guide
* clone the repo
* create `venv` and activate the shell to use the `venv`
* run `pip install -r requirements.txt`



