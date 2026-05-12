# Microservices Architecture - CarPool Connect

## Overview
The microservices architecture decomposes the application into small,
independent services. Each service owns its data, can be deployed
separately, and communicates via REST APIs or a message broker.
This approach enables independent scaling, fault isolation, and
faster deployment cycles for each service.

## Services

- **API Gateway**: Single entry point for all client requests. Routes
  traffic to appropriate microservices, handles load balancing, rate
  limiting, SSL termination, and request authentication validation.

- **Auth Service**: Manages user registration, login, JWT token
  generation, session management, and identity verification.
  Uses its own isolated PostgreSQL database (Auth DB) storing
  user credentials, tokens, and verification documents.

- **Ride Matching Service**: Core service responsible for creating rides,
  searching for matches based on location and schedule, and confirming
  bookings. Uses its own PostgreSQL database (Ride DB) storing ride
  records, routes, and booking history. Publishes ride-confirmed events
  to the Message Broker.

- **Payment Service**: Processes in-app payments, handles cost splitting
  between passengers, refunds, and receipt generation. Integrates with
  external payment gateways. Uses its own PostgreSQL database (Payment DB)
  storing transaction records and payment methods.

- **GPS Tracking Service**: Receives real-time location updates from
  drivers every 5 seconds and broadcasts them to passengers via WebSocket.
  Uses a time-series database (Location DB) optimized for storing and
  querying frequent location data points efficiently.

- **Notification Service**: Subscribes to events from the Message Broker
  (ride confirmed, payment processed, emergency alert) and sends push
  notifications, SMS, and email alerts to users via third-party providers.

- **Rating Service**: Manages post-ride ratings and reviews for drivers
  and passengers. Stores rating data in its own PostgreSQL database
  (Rating DB) and exposes APIs to retrieve average scores per user.

- **Chat Service**: Provides real-time bidirectional messaging between
  matched drivers and passengers using WebSocket connections. Stores
  chat history in its own database (Chat DB) for 24 hours after ride completion.

- **Message Broker (RabbitMQ/Kafka)**: Asynchronous event bus that
  decouples services from each other. Services publish events such as
  ride-confirmed, payment-processed, and location-updated. Subscribing
  services like Notification Service consume these events independently
  without blocking the publisher, ensuring resilience and scalability.
