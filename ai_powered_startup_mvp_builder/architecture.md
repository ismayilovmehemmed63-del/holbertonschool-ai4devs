# System Architecture

## High-Level Diagram
```mermaid
graph TD
    Student((Student)) -->|Interacts| Frontend[React + Tailwind]
    Frontend -->|API Requests| Backend[Node.js + Express]
    Backend -->|Queries| DB[(PostgreSQL/Supabase)]
    Backend -->|Prompt/Response| AI[OpenAI API]
