# Python version definition
ARG PYTHON_VERSION=3.10-slim-bullseye

# define an alias for the specific python version
FROM python:${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=dev

# Install apt packeages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev 

# Requirements are copied from local to container 
COPY ./requirements .

# Create python depedency and sub-dependency wheel
RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

# Python run stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=dev
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # cleaning up ununsed files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# wkhtmltopdf
RUN apt-get update && apt-get install -y \
    wkhtmltopdf

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# use wheels to insatll python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY ./compose/django/dev/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/dev/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


# copy application code to WORKDIR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
