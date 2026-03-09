from bson import ObjectId
from app.ai_plan import generate_study_plan

from fastapi import FastAPI
import uuid
from bson import ObjectId

from app.database import sessions_collection, questions_collection

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Adaptive Diagnostic Engine running"}


# START TEST SESSION
@app.post("/start-session")
def start_session():
    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "ability_score": 0.5,
        "questions_answered": []
    }

    sessions_collection.insert_one(session)

    return {
        "session_id": session_id,
        "ability_score": 0.5,
        "questions_answered": []
    }


# GET NEXT QUESTION BASED ON ABILITY
@app.get("/next-question/{session_id}")
def get_next_question(session_id: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    ability = session["ability_score"]

    question = questions_collection.find_one(
        {"difficulty": {"$gte": ability - 0.1, "$lte": ability + 0.1}}
    )

    if not question:
        question = questions_collection.find_one()

    return {
        "question_id": str(question["_id"]),
        "question": question["question"],
        "options": question["options"],
        "difficulty": question["difficulty"],
        "topic": question["topic"]
    }


# SUBMIT ANSWER AND UPDATE ABILITY
@app.post("/submit-answer")
def submit_answer(session_id: str, question_id: str, selected_answer: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    question = questions_collection.find_one({"_id": ObjectId(question_id)})

    if not question:
        return {"error": "Question not found"}

    correct_answer = question["correct_answer"]

    is_correct = selected_answer == correct_answer

    ability = session["ability_score"]

    # Adaptive update
    if is_correct:
        ability += 0.1
    else:
        ability -= 0.1

    ability = max(0.1, min(1.0, ability))

    sessions_collection.update_one(
        {"session_id": session_id},
        {
            "$set": {"ability_score": ability},
            "$push": {
                "questions_answered": {
                    "question_id": question_id,
                    "selected_answer": selected_answer,
                    "correct_answer": correct_answer,
                    "is_correct": is_correct
                }
            }
        }
    )

    return {
        "correct": is_correct,
        "new_ability_score": ability
    }
@app.get("/study-plan/{session_id}")
def get_study_plan(session_id: str):

    session = sessions_collection.find_one({"session_id": session_id})

    if not session:
        return {"error": "Session not found"}

    answers = session["questions_answered"]

    wrong_topics = []

    for ans in answers:
        if not ans["is_correct"]:
            q = questions_collection.find_one({"_id": ObjectId(ans["question_id"])})
            wrong_topics.append(q["topic"])

    ability = session["ability_score"]

    study_plan = generate_study_plan(wrong_topics, ability)

    return {
        "study_plan": study_plan
    }