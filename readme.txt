For the task were chosen Flask framework and PostgreSQL database.

Flask
Application wasn't build for handling very high RPS, so there was no need for async.
It is a small application with minimal functionality so there was no need for Django.
The Flask was chosen because of its minimalism and simplicity.

PostgreSQL
Posgtre is a stable and easily scalable database with all the necessary features.
For this project, it works just fine.


The application was built according to MVC structure

manage.py - file for running the application with cli support
config.py - main config of the application
models - all models used in the application
services.py - all business logic and database access
apis.py - endpoints that use services with business logic


Ad requests and impressions were implemented as simple counters in user and sdk models
to facilitate saving and retrieving data.
