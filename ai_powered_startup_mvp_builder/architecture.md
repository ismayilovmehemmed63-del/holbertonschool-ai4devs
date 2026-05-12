# System Architecture

## Overview
The AI Study Planner is a full-stack web application built with a modern decoupled architecture.

## Components
- **Frontend:** React.js with Tailwind CSS (Deployed on Vercel).
- **Backend:** Node.js/Express API (Deployed on Render).
- **AI Engine:** Integration with OpenAI API for schedule generation.
- **Database:** PostgreSQL (Hosted on Supabase) for storing user tasks and subjects.

## Workflow
1. User interacts with the React frontend.
2. Frontend sends requests to the Express API.
3. API fetches/saves data from PostgreSQL and communicates with AI for plan generation.
4. Data is returned to the user interface.
