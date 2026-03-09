# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimension Adaptive Testing System** that dynamically adjusts question difficulty based on a student's responses. The system estimates the student's ability level and generates a personalized AI study plan.

The backend is built using **FastAPI**, **MongoDB**, and **Gemini AI**.

---

## Project Workflow

1. Student starts a test session
2. System selects a question based on ability score
3. Student submits an answer
4. Ability score updates based on correctness
5. Next question difficulty adjusts dynamically
6. AI generates a personalized study plan based on weak topics

---

## Tech Stack

* **Backend:** FastAPI
* **Database:** MongoDB Atlas
* **Language:** Python
* **AI Integration:** Google Gemini API

---

## Database Schema

### Questions Collection

Each question document contains:

```
{
  "question": "What is 2x + 6 = 14?",
  "options": ["3","4","5","6"],
  "correct_answer": "4",
  "difficulty": 0.3,
  "topic": "Algebra",
  "tags": ["equations"]
}
```

Difficulty ranges from **0.1 (easy) to 1.0 (hard)**.

---

### User Session Collection

```
{
 "session_id": "uuid",
 "ability_score": 0.5,
 "questions_answered": []
}
```

---

## Adaptive Algorithm Logic

The system uses a simplified **Item Response Theory (IRT)** approach.

Rules used:

* Initial ability score = **0.5**
* Correct answer → ability increases by **0.1**
* Incorrect answer → ability decreases by **0.1**
* Ability score is restricted between **0.1 and 1.0**

The next question is selected from MongoDB where difficulty is **closest to the current ability score**.

---

## API Endpoints

### Start Test Session

```
POST /start-session
```

Creates a new testing session.

Example Response:

```
{
 "session_id": "uuid",
 "ability_score": 0.5
}
```

---

### Get Next Question

```
GET /next-question/{session_id}
```

Returns a question near the student's ability level.

Example Response:

```
{
 "question_id": "123",
 "question": "Synonym of Rapid?",
 "options": ["Slow","Fast","Heavy","Weak"],
 "difficulty": 0.4,
 "topic": "Vocabulary"
}
```

---

### Submit Answer

```
POST /submit-answer
```

Parameters:

* session_id
* question_id
* selected_answer

Example Response:

```
{
 "correct": true,
 "new_ability_score": 0.6
}
```

---

### Generate AI Study Plan

```
GET /study-plan/{session_id}
```

Uses Gemini AI to generate a personalized study plan based on weak topics.

Example Output:

```
1. Review algebra fundamentals.
2. Practice vocabulary exercises daily.
3. Take timed quizzes to improve accuracy.
```

---

## How to Run the Project

### 1 Clone the repository

```
git clone <your_repo_link>
cd adaptive-diagnostic-engine
```

### 2 Install dependencies

```
pip install -r requirements.txt
```

### 3 Create environment variables

Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_gemini_api_key
```

### 4 Start the server

```
python -m uvicorn app.main:app --reload
```

### 5 Open API documentation

```
http://127.0.0.1:8000/docs
```

---

## AI Log

AI tools used during development:

* ChatGPT
* Gemini API

How AI was used:

* Assisted in designing the FastAPI backend structure
* Helped generate MongoDB schema for questions and sessions
* Assisted in implementing the adaptive testing algorithm
* Helped integrate Gemini API for personalized study plan generation
* Assisted in debugging Python environment and dependency issues

Challenges encountered:

* Handling MongoDB ObjectId serialization in FastAPI responses
* Managing multiple Python environments and dependencies
* Implementing adaptive question selection based on ability score

---

## Future Improvements

* Implement full Item Response Theory model
* Add question difficulty calibration
* Build a frontend interface for students
* Add analytics dashboard for performance tracking
