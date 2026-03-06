The FastAPI application inside the container is failing to start.

Your task is to debug and fix the environment so that the API becomes healthy.

The application depends on a PostgreSQL database.

Expected behaviour:

Running the stack should start the API successfully.

The endpoint below must work:

GET /health

Expected response:

{"status": "ok"}

You may inspect logs, update configuration, or fix connection settings.
