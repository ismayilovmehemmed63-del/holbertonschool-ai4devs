# Microservices Architecture – CarPool Connect

## Overview
The microservices architecture decomposes the application into small,
independent services. Each service owns its data, can be deployed
separately, and communicates via REST APIs or a message broker.

## Services

- **API Gateway**: Single entry point for all client requests. Routes
  traffic to appropriate microservices, handles load balancing, and
  enforces rate limiting and SSL termination.

- **Auth Service**: Manages user registration, login, JWT token
  generation, and identity verification. Has its own isolated database.

- **Ride Matching Service**: Core service responsible for creating rides,
  searching for matches, and booking. Publishes events to the message
  broker when a ride is confirmed.

- **Payment Service**: Processes in-app payments, handles cost splitting,
  refunds, and receipt generation. Integrates with external payment gateways.

- **GPS Tracking Service**: Receives real-time location updates from
  drivers and broadcasts them to passengers. Uses a time-series database
  for efficient location storage.

- **Notification Service**: Subscribes to events from the message broker
  and sends push notifications, SMS, and email alerts to users.

- **Rating Service**: Manages post-ride ratings and reviews for drivers
  and passengers. Stores and retrieves rating data independently.

- **Chat Service**: Provides real-time messaging between matched drivers
  and passengers using WebSocket connections.

- **Message Broker**: Central event bus (e.g. RabbitMQ or Kafka) that
  enables async communication between services such as ride confirmed,
  payment processed, and location updated events.
