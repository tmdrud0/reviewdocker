FROM openjdk:11
COPY . /app
WORKDIR /app/review

RUN ./gradlew build

ENTRYPOINT ["java","-jar","build/libs/review-0.0.1-SNAPSHOT.jar"]
