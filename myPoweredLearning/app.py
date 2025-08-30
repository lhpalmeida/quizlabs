from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [{"question": "What is the key mathematical difference between discriminative and generative models?",
              "options": ["Discriminative models estimate P(x, y)", "Generative models estimate P(y|x)",
                          "Discriminative models estimate P(y|x)", "Generative models estimate P(x|y)"],
              "answer": "Discriminative models estimate P(y|x)"},
             {"question": "Which model type is more suitable for semi-supervised learning tasks?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which AI model type is more likely to suffer from overfitting in high-dimensional data?",
              "options": ["Generative AI", "Discriminative AI", "Unsupervised AI", "Reinforcement AI"],
              "answer": "Generative AI"}, {
                 "question": "Which of the following models is considered both generative and discriminative depending on its configuration?",
                 "options": ["Naive Bayes", "Conditional Random Fields", "Variational Autoencoders",
                             "Hidden Markov Models"], "answer": "Hidden Markov Models"},
             {"question": "Which AI model type is more robust to missing data?",
              "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in zero-shot learning scenarios?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type typically requires more computational resources during training?",
              "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in transfer learning applications?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more suitable for modeling complex dependencies between features?",
              "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in adversarial training setups?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in probabilistic graphical models?",
              "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in structured prediction tasks?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
              "answer": "Discriminative AI"},
             {"question": "Which model type is more likely to be used in Bayesian inference?",
              "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in active learning scenarios?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
              "answer": "Discriminative AI"},
             {"question": "Which model type is more likely to be used in unsupervised pretraining?",
              "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in multi-modal learning?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in few-shot learning?",
              "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
              "answer": "Generative AI"},
             {"question": "Which model type is more likely to be used in feature extraction tasks?",
              "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
              "answer": "Discriminative AI"},
             {"question": "Which model type is more likely to be used in reinforcement learning policy generation?",
              "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
              "answer": "Generative AI"}, {
                 "question": "Which model type is more likely to be used in synthetic data generation for privacy preservation?",
                 "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
                 "answer": "Generative AI"}]


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
        return redirect(url_for("quiz", q_id=q_id + 1, score=score))

    score = request.args.get("score", 0)
    return render_template("question.html", question=questions[q_id], q_id=q_id, score=score)


@app.route("/result")
def result():
    score = request.args.get("score", 0)
    return render_template("result.html", score=score, total=len(questions))


if __name__ == "__main__":
    app.run(debug=True)
