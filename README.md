# dh-twilio-dashboard

A sample application that creates a Twilio dashboard to display data from Twilio's API.

## Components

* `Dockerfile`: The Dockerfile that extends the Deephaven server image to install the project dependencies
* `docker-compose.yml`: The docker-compose file that defines the local Dockerfile build, the Deephaven application mode directory, and the environmental variables
* `requirements.txt`: The Python dependencies for the project
* `data/app.d/`: The Deephaven application mode directory
* `data/layouts/layout.json`: The IDE layout file

## Environmental variables

The following environmental variables need to be set to run the app.

```
TWILIO_AUTH_TOKEN
TWILIO_ACCOUNT_SID
```

An easy way to do this is to put it in a `.env` file in the project.

```
TWILIO_AUTH_TOKEN=""
TWILIO_ACCOUNT_SID=""
```

## Launch

Simply run

```
docker compose up
```

to launch the app, then go to http://localhost:10000 to view the app.
