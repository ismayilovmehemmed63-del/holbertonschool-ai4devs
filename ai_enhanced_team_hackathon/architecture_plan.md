# Architecture Plan - AI Code Auditor

## Technology Stack
- **Frontend:** React with Tailwind CSS for a modern, responsive UI.
- **Backend:** FastAPI (Python) to handle file uploads and AI processing.
- **Database:** PostgreSQL (via Supabase) for storing audit history.
- **AI Integration:** OpenAI API (GPT-4o) for analyzing code snippets.

## System Workflow
1. **Upload:** User uploads a file or pastes code into the React frontend.
2. **Request:** Frontend sends the code to the FastAPI backend.
3. **Audit:** Backend sends a structured prompt to the OpenAI API.
4. **Processing:** AI returns a JSON object containing findings and severity scores.
5. **Storage:** Backend saves the session and findings into PostgreSQL.
6. **Output:** Frontend displays the results and generates a Markdown report for download.
