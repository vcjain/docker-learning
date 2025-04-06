# Stage 1 to compile src code and generate jar file
FROM maven:3.8.1-openjdk-17-slim AS builder

# This will create a directory app in conatiner and will move pom.xml and src folder into it. 
WORKDIR /app

COPY src/ ./src/
COPY pom.xml .

# Will compile and generate a demo-1.0.jar file in target folder
RUN mvn clean package

# Final Stage - It will only include jar file and src code will not be included

FROM openjdk:17-slim
WORKDIR /app
COPY --from=builder /app/target/demo-1.0.jar .

EXPOSE 8080

CMD ["java", "-jar", "target/demo-1.0.jar"]