PRD: CV SCREENING APP MVP
Version: 1.0 (Candidate-Centric)
1. Introduction & Problem Statement
The modern job search is highly competitive. Candidates often send out dozens, if not hundreds, of applications without receiving a response. It's difficult to know why a resume was rejected or how to improve it for the next application. Job seekers struggle to understand if they are a good fit for a role and, more importantly, what specific skills they are missing to become a top contender.
The AI Job Match & Skill Gap Analyzer is a personal career tool designed to empower job seekers. By comparing their resume against a specific job description, it provides instant, actionable feedback, highlighting their strengths and pinpointing the exact skills they need to develop or showcase.
2. User Persona
Name: Alex, the Aspiring Data Analyst
Role: A recent graduate or early-career professional looking to land a job in data analytics.
Goals:
•	Stop "spraying and praying"—only apply to jobs where they are a strong fit.
•	Understand exactly what skills are required for a dream job.
•	Get more interviews by tailoring their resume effectively.
•	Create a learning plan based on real-time market demands.
Pain Points:
•	"I apply to 20 jobs a day and never hear back. I don't know what I'm doing wrong."
•	"The job description lists so many 'required skills.' Which ones are actually important?"
•	"I want to improve my skills, but I don't know what I should learn next to be more marketable."
3. Goals & Objectives
The primary goal of the MVP is to provide a user with clear, actionable insights on how their resume stacks up against a single job description.
•	User Goal: To instantly see their match percentage for a job and get a simple list of the key skills they are missing.
•	Project Goal: To build a portfolio piece that demonstrates practical NLP skills by solving a tangible, painful problem for job seekers.
•	Technical Goal: To accurately parse resume and job description text, identify key skills/keywords, and reliably differentiate between matched and missing skills.
4. Features & Scope (MVP)
The MVP will be a focused tool that executes one core workflow brilliantly.
Feature ID	Feature Name	Description	Priority
F-01	Resume Uploader	The user can upload their resume. The system will support .pdf and .docx formats.	Must-Have
F-02	Job Description Input	The user can paste the full text of a job description into a text area.	Must-Have
F-03	Analysis Trigger	A single button (e.g., "Analyze My Match") that initiates the comparison.	Must-Have
F-04	Overall Match Score	After processing, the system displays a clear, quantitative match score (e.g., "You are a 75% match for this role").	Must-Have
F-05	Skill Gap Analysis	(Core Feature) The system displays a prominent list of important skills and keywords found in the job description that are missing from the user's resume.	Must-Have
F-06	Matched Skills Display	To provide positive feedback, the system also displays a list of required skills that were found in the user's resume.	High
5. User Flow & Design
The user journey is designed to be simple and provide immediate value.
1.	Start: The user lands on a clean page with two elements: a file upload control and a text area.
2.	Input: The user uploads their resume and pastes the target job description.
3.	Action: The user clicks "Analyze My Match." A loading animation provides feedback that the system is working.
4.	Results: The page updates to show a results dashboard:
o	At the top: The Overall Match Score.
o	Below the score, two distinct sections:
	A "call-to-action" section titled "Skills to Add or Learn" (the skill gap).
	A "confirmation" section titled "Your Matching Skills".
6. Success Metrics
We will measure the success of the MVP by its ability to provide actionable advice.
•	Actionability Score: After a user sees their results, ask a simple, one-click question: "Was this analysis helpful for improving your resume?" (Yes/No). The goal is a >80% "Yes" rate.
•	Clarity of Feedback: Qualitative feedback from test users on whether the "missing skills" list was clear, relevant, and accurate.
•	Processing Time: Target time from click to results should be under 15 seconds to maintain user engagement.
7. Out of Scope for MVP (Future Considerations)
To ensure the MVP is lean and focused, the following features will not be included in the initial release:
•	Recommending other jobs based on the user's resume.
•	Automatically suggesting how to rephrase sentences in the resume.
•	Providing links to online courses or resources for the missing skills.
•	User accounts for saving history or multiple resumes.

