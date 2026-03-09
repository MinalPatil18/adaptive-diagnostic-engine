from app.database import questions_collection

questions = [

{
"question": "What is 2x + 6 = 14?",
"options": ["3","4","5","6"],
"correct_answer": "4",
"difficulty": 0.3,
"topic": "Algebra",
"tags": ["equations"]
},

{
"question": "What is 5²?",
"options": ["10","15","20","25"],
"correct_answer": "25",
"difficulty": 0.2,
"topic": "Arithmetic",
"tags": ["powers"]
},

{
"question": "Synonym of 'Rapid'?",
"options": ["Slow","Fast","Heavy","Weak"],
"correct_answer": "Fast",
"difficulty": 0.4,
"topic": "Vocabulary",
"tags": ["synonyms"]
},

{
"question": "What is 12 × 8?",
"options": ["96","88","108","92"],
"correct_answer": "96",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["multiplication"]
},

{
"question": "What is √81?",
"options": ["7","8","9","10"],
"correct_answer": "9",
"difficulty": 0.4,
"topic": "Arithmetic",
"tags": ["square-root"]
},

{
"question": "What is 3x = 18?",
"options": ["3","4","5","6"],
"correct_answer": "6",
"difficulty": 0.2,
"topic": "Algebra",
"tags": ["equations"]
},

{
"question": "Opposite of 'Scarce'?",
"options": ["Rare","Abundant","Few","Empty"],
"correct_answer": "Abundant",
"difficulty": 0.5,
"topic": "Vocabulary",
"tags": ["antonyms"]
},

{
"question": "What is 15 + 27?",
"options": ["42","40","38","45"],
"correct_answer": "42",
"difficulty": 0.2,
"topic": "Arithmetic",
"tags": ["addition"]
},

{
"question": "What is 9 × 9?",
"options": ["72","81","90","99"],
"correct_answer": "81",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["multiplication"]
},

{
"question": "Meaning of 'Eloquent'?",
"options": ["Fluent","Silent","Weak","Angry"],
"correct_answer": "Fluent",
"difficulty": 0.6,
"topic": "Vocabulary",
"tags": ["meaning"]
}

]

questions_collection.insert_many(questions)

print("Questions inserted successfully!")