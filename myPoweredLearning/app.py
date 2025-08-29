from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    # {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    # {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    # {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"}
    {
        "question": "What does discriminative AI primarily focus on?",
        "options": ["Generating new data", "Classifying existing data", "Creating images", "Writing text"],
        "answer": "Classifying existing data"
    },
    {
        "question": "Which type of AI is used to generate realistic images or text?",
        "options": ["Discriminative AI", "Generative AI", "Supervised AI", "Reinforcement AI"],
        "answer": "Generative AI"
    },
    {
        "question": "Which AI model learns the boundary between classes?",
        "options": ["Generative AI", "Discriminative AI", "Unsupervised AI", "Symbolic AI"],
        "answer": "Discriminative AI"
    },
    {
        "question": "Which AI type models the joint probability distribution of data and labels?",
        "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
        "answer": "Generative AI"
    },
    {
        "question": "Which of the following is an example of a generative AI model?",
        "options": ["Logistic Regression", "Support Vector Machine", "GPT", "Decision Tree"],
        "answer": "GPT"
    },
    {
        "question": "Which AI type is better suited for classification tasks?",
        "options": ["Generative AI", "Discriminative AI", "Creative AI", "Cognitive AI"],
        "answer": "Discriminative AI"
    },
    {
        "question": "Which AI type can be used to create synthetic data?",
        "options": ["Discriminative AI", "Generative AI", "Analytical AI", "Statistical AI"],
        "answer": "Generative AI"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz/<int:q_id>", methods=["GET", "POST"])
def quiz(q_id):
    score = int(request.args.get("score", 0))

    if q_id >= len(questions):
        return redirect(url_for("result", score=score))

    if request.method == "POST":
        selected = request.form.get("option")
        correct = questions[q_id]["answer"]
        if selected == correct:
            score += 1
            print(score)
        return redirect(url_for("quiz", q_id=q_id+1, score=score))

    score = request.args.get("score", 0)
    return render_template("question.html", question=questions[q_id], q_id=q_id, score=score)

@app.route("/result")
def result():
    score = request.args.get("score", 0)
    return render_template("result.html", score=score, total=len(questions))

if __name__ == "__main__":
    app.run(debug=True)