# Project-1: Enterprise CICD
# Dockerfile: builds the application jar into an image
FROM openjdk:17-jdk-slim
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
