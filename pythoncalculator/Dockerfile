# Build-Image, Python 3.12 Alpine Version
FROM python:3.12-alpine as builder

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    g++

# Set the working directory in the container
WORKDIR /app

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

COPY ./src/requirements.in /app

# Install the required dependencies
RUN pip install -r requirements.in

# Copy the application code
COPY ./src /app

# Compile Python files to bytecode
RUN python -m compileall /app


# Remove the .py files and __pycache__ directories
RUN find . -name '*.py' ! -name 'main.py' -delete

# Stage 2: Runtime
FROM python:3.12-alpine

# Install runtime dependencies (libs needed for sklearn)
RUN apk add --no-cache libgomp libstdc++

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copy the app from the builder stage
COPY --from=builder /app /app

# Name the image
LABEL name="pythoncalculator"

# The command that is executed when the container starts
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
