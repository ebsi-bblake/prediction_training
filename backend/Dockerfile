FROM python:3.9
WORKDIR /app
COPY src/setup_and_run.sh /app/

# Ensure the script is executable
RUN chmod +x /app/setup_and_run.sh

# Verify the script is copied
RUN ls -l /app/

# Set the entry point to the orchestration script
ENTRYPOINT ["./setup_and_run.sh"]
