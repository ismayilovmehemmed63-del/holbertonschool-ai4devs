# Monolithic Architecture - CarPool Connect

## Overview
The monolithic architecture packages all application components into a
single deployable unit. All modules share the same codebase, runtime,
and database, making it simple to develop and deploy in early stages.

## Components

- **Mobile/Web Frontend**: The user-facing interface for iOS, Android,
  and web browsers. Sends all requests to the backend monolith via REST API.

- **Authentication Module**: Handles user registration, login, session
  management, and identity verification using JWT tokens.

- **Ride Matching Module**: Core business logic that pairs drivers and
  passengers based on location, schedule, and route compatibility.

- **Payments Module**: Processes in-app payments, splits costs between
  passengers, and generates receipts. Integrates with payment gateways.

- **GPS Tracking Module**: Receives and broadcasts real-time location
  data for active rides, enabling live tracking for both drivers and passengers.

- **Notification Service**: Sends push notifications, SMS alerts, and
  email messages for ride confirmations, updates, and emergency alerts.

- **Rating and Review Module**: Manages post-ride ratings and reviews
  for both drivers and passengers to maintain platform quality.

- **Chat Module**: Provides in-app messaging between matched drivers
  and passengers for ride coordination.

- **Central Database**: Single shared database storing all application
  data including users, rides, payments, and messages.

- **PostgreSQL**: Primary relational database for persistent structured data.

- **Redis Cache**: In-memory cache for session data, real-time location
  updates, and frequently accessed data to improve performance.
