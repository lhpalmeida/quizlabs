import gradio as gr
import json
import random


# Function to load and shuffle questions and options
def load_questions():
    with open("i_shouldnt_feel_t_w_chap1.json", "r") as file:
        questions = json.load(file)

    # Shuffle the questions
    random.shuffle(questions)

    # Shuffle the options for each question
    for question in questions:
        random.shuffle(question["options"])

    return questions


# Load questions from the file and shuffle them
questions = load_questions()


def build_view(q_id: int, score: int):
    total = len(questions)
    if q_id >= total:
        title = f"Quiz Complete!"
        progress = f"Your score: {score} / {total}"
        return (
            title,  # header
            progress,  # progress text
            gr.update(value="Thanks for playing!", visible=True),  # question text
            gr.update(choices=[], value=None, visible=False),  # options
            gr.update(visible=False),  # submit button
            gr.update(visible=True),  # restart button
            q_id,
            score
        )

    q = questions[q_id]
    title = "Non-Tech Quiz"
    progress = f"Question {q_id + 1} of {total} | Current Score: {score}"
    question_text = q["question"]
    options = q["options"]
    return (
        title,
        progress,
        gr.update(value=question_text, visible=True),
        gr.update(choices=options, value=None, visible=True),
        gr.update(visible=True),
        gr.update(visible=True),
        q_id,
        score
    )


def submit_answer(selected, q_id, score):
    # If nothing selected, don't advance; just re-render the same question
    if selected is None:
        return build_view(q_id, score)

    # Check if the selected option is correct
    if selected == questions[q_id]["answer"]:
        score += 1

    # Move to next question
    q_id += 1
    return build_view(q_id, score)


def restart_quiz():
    # Reload and shuffle questions and options each time the quiz is restarted
    global questions
    questions = load_questions()
    return build_view(0, 0)


with gr.Blocks(title="Non-Tech Quiz", css=".choices label { display: block; }") as demo:
    q_id = gr.State(0)
    score = gr.State(0)

    header = gr.Markdown("")
    progress_md = gr.Markdown("")
    question_md = gr.Markdown("")
    options_radio = gr.Radio(choices=[], label="Choose one", interactive=True, elem_classes=["choices"])
    with gr.Row():
        submit_btn = gr.Button("Submit")
        restart_btn = gr.Button("Restart")

    # Wire events
    demo.load(fn=lambda: build_view(0, 0),
              outputs=[header, progress_md, question_md, options_radio, submit_btn, restart_btn, q_id, score])

    submit_btn.click(
        fn=submit_answer,
        inputs=[options_radio, q_id, score],
        outputs=[header, progress_md, question_md, options_radio, submit_btn, restart_btn, q_id, score]
    )

    restart_btn.click(
        fn=restart_quiz,
        inputs=[],
        outputs=[header, progress_md, question_md, options_radio, submit_btn, restart_btn, q_id, score]
    )

if __name__ == "__main__":
    demo.launch()
