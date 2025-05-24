# Resume Scanner App

This is a simple Flask web application that compares a resume to a job description using AI. It returns a similarity score and feedback on how well the resume matches the job description.

## Features

- Upload a resume (PDF)
- Paste a job description
- Get a similarity score (0 to 100%)
- See feedback based on how closely the resume matches the job

## Technologies Used

- Python
- Flask
- Sentence Transformers (all-MiniLM-L6-v2)
- PyMuPDF (for reading PDFs)
- HTML + CSS (Jinja2 templating)

## How to Run

1. Clone the repository
2. Install the requirements:
3. Run the Flask app:

4. Go to `http://localhost:5000` in your browser

## Feedback Based on Score

- **0–39%**: Resume does not match the job. Revise it to include relevant skills and experience.
- **40–59%**: Some match. Improve it by adding missing details.
- **60–79%**: Strong match. You can still add more keywords.
- **80–100%**: Great match. Resume is well-tailored to the job.

## Future Improvements

- Add keyword highlighting
- Better error handling
- Improve design with CSS or Bootstrap
- Deploy the app online
