import gradio as gr

questions = [
  {
    "question": "What is the primary focus of CHM1311 in the Health Sciences program?",
    "options": [
      "Advanced organic synthesis",
      "Fundamental principles of general chemistry",
      "Biochemistry of proteins and enzymes",
      "Clinical laboratory techniques"
    ],
    "answer": "Fundamental principles of general chemistry"
  },
  {
    "question": "Which of the following best describes the scientific method introduced in CHM1311?",
    "options": [
      "A strict set of lab rules",
      "A process of observation, hypothesis, experimentation, and conclusion",
      "A memorization technique for chemical formulas",
      "A mathematical formula used to predict reactions"
    ],
    "answer": "A process of observation, hypothesis, experimentation, and conclusion"
  },
  {
    "question": "Which system of measurement is primarily used in CHM1311?",
    "options": [
      "Imperial system",
      "Customary US units",
      "SI (International System of Units)",
      "British engineering system"
    ],
    "answer": "SI (International System of Units)"
  },
  {
    "question": "What is the correct definition of a significant figure in a measurement?",
    "options": [
      "Digits that are uncertain",
      "Digits that are always zero",
      "Digits that reflect the precision of a measurement",
      "Digits used only in chemical equations"
    ],
    "answer": "Digits that reflect the precision of a measurement"
  },
  {
    "question": "What does the term 'element' refer to in chemistry?",
    "options": [
      "A substance that cannot be broken down into simpler substances by chemical means",
      "A mixture of two or more compounds",
      "A physical combination of substances",
      "A unit of energy in chemical reactions"
    ],
    "answer": "A substance that cannot be broken down into simpler substances by chemical means"
  },
  {
    "question": "Which subatomic particle determines the identity of an element?",
    "options": [
      "Neutrons",
      "Electrons",
      "Protons",
      "Isotopes"
    ],
    "answer": "Protons"
  },
  {
    "question": "Which of the following best describes a compound?",
    "options": [
      "A pure substance composed of two or more elements chemically bonded",
      "A heterogeneous mixture",
      "A single type of atom",
      "A physical state of matter"
    ],
    "answer": "A pure substance composed of two or more elements chemically bonded"
  },
  {
    "question": "In the periodic table, elements are arranged primarily according to:",
    "options": [
      "Atomic mass",
      "Alphabetical order",
      "Atomic number",
      "Number of neutrons"
    ],
    "answer": "Atomic number"
  },
  {
    "question": "Which law states that mass is neither created nor destroyed in a chemical reaction?",
    "options": [
      "Law of Multiple Proportions",
      "Law of Definite Composition",
      "Law of Conservation of Mass",
      "Law of Ideal Gases"
    ],
    "answer": "Law of Conservation of Mass"
  },
  {
    "question": "Why is chemistry considered a central science in health studies?",
    "options": [
      "It focuses only on mathematical calculations",
      "It bridges physics, biology, and medicine by explaining matter and its interactions",
      "It is unrelated to biology or health",
      "It is only needed for lab work"
    ],
    "answer": "It bridges physics, biology, and medicine by explaining matter and its interactions"
  }
]

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
            gr.update(visible=True),   # restart button
            q_id,
            score
        )

    q = questions[q_id]
    title = "RAG Quiz"
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

    # Update score if correct
    if q_id < len(questions) and selected == questions[q_id]["answer"]:
        score += 1

    # Move to next question
    q_id += 1
    return build_view(q_id, score)

def restart_quiz():
    return build_view(0, 0)

with gr.Blocks(title="RAG Quiz", css=".choices label { display: block; }") as demo:
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