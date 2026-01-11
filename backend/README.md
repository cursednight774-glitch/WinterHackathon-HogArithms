Project Name:

Course and Job credibility system

Description
The product being developed checks if the course or job opening we're looking at is credible or not.

Features
.Credibility system
.Easy access
.Modularisation

Frontend (Browser Extension)
Plasmo Framework – For rapid, cross-browser extension development.

React & TypeScript – For building a responsive, type-safe user interface.

Tailwind CSS – For styling the "Shield" overlay without CSS conflicts on host sites.

Backend & Infrastructure
Python (FastAPI) – High-performance async API to handle requests.

Docker – Containerization for consistent deployment.

Redis – Caching scan results for millisecond latency.

Google Technologies Used
Google Vertex AI

 We use Gemini's advanced context window to analyze complex job descriptions and course syllabi.Allowing us to calculate a semantic "ROI Score" and detect subtle scam language patterns that rule-based systems miss.

Google Cloud Run

To host our Python backend. We chose Cloud Run for its serverless architecture, allowing our API to scale instantly from zero to thousands of concurrent requests during high-traffic periods (like career fairs) while maintaining low latency.

Google Web Risk API

 To provide an instant "first line of defense." Before our AI even analyzes the text, this API checks the URL against Google's constantly updated index of over a million unsafe web resources, blocking known phishing and social engineering sites immediately.

Google Cloud Firestore

Used as our high-speed NoSQL database to store verified recruiter profiles and cache previous scan results. Its real-time capabilities allow us to sync the "Verified" status across all users instantly.

Google Custom Search JSON API

To perform "Grounding" checks. We programmatically search the web to verify if a recruiter actually works at the company they claim to represent, without violating terms of service by scraping platforms like LinkedIn directly.

Setup Instructions
Steps to run the project locally:
1. Clone the repository
2. Install dependencies
3. Add environment variables (if any)
4. Run the project

 Team Members
- Raahil Ibrahim
- Milind Manoj Naik
- Taahir Abdulla
- Asher Pinto
