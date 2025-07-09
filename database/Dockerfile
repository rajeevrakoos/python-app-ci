# Start with the official MySQL image from Docker Hub
FROM mysql:8.0

# Set environment variables (like passwords)
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=myapp
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=userpass

# Run MySQL on the standard port
EXPOSE 3306

# (Optional) Add a custom SQL file to be executed on startup
# COPY init.sql /docker-entrypoint-initdb.d/