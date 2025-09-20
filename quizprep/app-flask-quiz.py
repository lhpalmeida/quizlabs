from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

# questions = [
#     {
#         "question": "What best describes Retrieval-Augmented Generation (RAG)?",
#         "options": [
#             "A technique that trains LLMs on larger datasets without external data access",
#             "A method that integrates information retrieval with generative models to produce context-aware responses",
#             "A way to compress prompts to fit within an LLM’s context window",
#             "A tool for converting PDFs into plain text for model training"
#         ],
#         "answer": "A method that integrates information retrieval with generative models to produce context-aware responses"
#     },
#     {
#         "question": "Which limitation of non-RAG LLM systems does RAG directly address?",
#         "options": [
#             "Excessive GPU memory usage during inference",
#             "Inability to generate creative content",
#             "Lack of access to external sources leading to inaccuracies and hallucinations",
#             "Difficulty in tokenizing multilingual text"
#         ],
#         "answer": "Lack of access to external sources leading to inaccuracies and hallucinations"
#     },
#     {
#         "question": "In an RAG system, what is an 'augmented prompt'?",
#         "options": [
#             "A prompt that includes only the user’s input with no additional context",
#             "A prompt that merges the user’s input with retrieved, relevant external text",
#             "A prompt automatically shortened to fit within the model’s token limit",
#             "A prompt that embeds images rather than text"
#         ],
#         "answer": "A prompt that merges the user’s input with retrieved, relevant external text"
#     },
#     {
#         "question": "Why can RAG improve trust in model outputs?",
#         "options": [
#             "Because it prevents the LLM from generating long responses",
#             "Because it enforces deterministic decoding strategies",
#             "Because it cites external documents or sources that can be verified",
#             "Because it always uses the latest LLM architecture"
#         ],
#         "answer": "Because it cites external documents or sources that can be verified"
#     },
#     {
#         "question": "Which is a key advantage of RAG over relying solely on long context windows?",
#         "options": [
#             "It eliminates the need for tokenization",
#             "It retrieves only the most relevant information instead of dumping all source text",
#             "It guarantees zero latency during inference",
#             "It makes embedding models unnecessary"
#         ],
#         "answer": "It retrieves only the most relevant information instead of dumping all source text"
#     },
#     {
#         "question": "Which of the following is NOT listed as a drawback of very long prompts without RAG?",
#         "options": [
#             "Increased processing time and cost due to more tokens",
#             "Potential redundancy that makes it hard to find key facts",
#             "Automatic hallucination suppression",
#             "Users must already possess the necessary source information"
#         ],
#         "answer": "Automatic hallucination suppression"
#     },
#     {
#         "question": "Which step immediately follows 'Gather Sources' in a basic RAG pipeline?",
#         "options": [
#             "Store Vectors",
#             "Embed Sources",
#             "Retrieve Relevant Data",
#             "Obtain a Response"
#         ],
#         "answer": "Embed Sources"
#     },
#     {
#         "question": "What is the purpose of chunking during the 'Embed Sources' step?",
#         "options": [
#             "To compress vectors to smaller dimensions",
#             "To split large documents into smaller pieces for efficient retrieval",
#             "To remove stopwords from the text",
#             "To convert vectors back into text"
#         ],
#         "answer": "To split large documents into smaller pieces for efficient retrieval"
#     },
#     {
#         "question": "Which statement about embedding models in RAG is correct?",
#         "options": [
#             "The same LLM used for generation must also be used for embeddings",
#             "Embedding models are distinct from the LLM used for response generation",
#             "Embedding models do not require tokenization",
#             "Embedding models output raw text, not vectors"
#         ],
#         "answer": "Embedding models are distinct from the LLM used for response generation"
#     },
#     {
#         "question": "What is stored in the vector store in an RAG system?",
#         "options": [
#             "Raw PDF files for later OCR",
#             "Fixed-length numeric vectors representing text chunks",
#             "Full conversation transcripts without processing",
#             "Hashed identifiers only"
#         ],
#         "answer": "Fixed-length numeric vectors representing text chunks"
#     },
#     {
#         "question": "Which of the following are examples of vector databases mentioned in the text?",
#         "options": [
#             "PostgreSQL and MySQL",
#             "Elasticsearch and Solr",
#             "ChromaDB, FAISS, and Milvus",
#             "Redis and MongoDB"
#         ],
#         "answer": "ChromaDB, FAISS, and Milvus"
#     },
#     {
#         "question": "Why should the user’s prompt be embedded with the same embedding model used for sources?",
#         "options": [
#             "To ensure vector dimensionality and semantic space are compatible",
#             "To reduce storage requirements in the vector database",
#             "To enable the LLM to learn new tokens on the fly",
#             "To avoid the need for chunking documents"
#         ],
#         "answer": "To ensure vector dimensionality and semantic space are compatible"
#     },
#     {
#         "question": "Which retrieval strategy is described in the text?",
#         "options": [
#             "Only retrieve the top-1 token by log probability",
#             "Retrieve multiple relevant documents or the entire document containing a relevant chunk",
#             "Retrieve embeddings from unrelated domains to improve diversity",
#             "Retrieve only the earliest chunk in the corpus"
#         ],
#         "answer": "Retrieve multiple relevant documents or the entire document containing a relevant chunk"
#     },
#     {
#         "question": "What role can conversation memory tools play in RAG?",
#         "options": [
#             "They replace the need for a vector store",
#             "They provide OCR for scanned documents",
#             "They help augment the current prompt with relevant prior conversation context",
#             "They compress vectors to reduce dimensionality"
#         ],
#         "answer": "They help augment the current prompt with relevant prior conversation context"
#     },
#     {
#         "question": "Which method for creating an augmented prompt is mentioned in the text?",
#         "options": [
#             "Structured templates that place user input and retrieved text alongside instructions",
#             "Binary encoding of prompts to shorten token length",
#             "Random shuffling of retrieved chunks to avoid bias",
#             "Embedding the LLM’s output back into the prompt"
#         ],
#         "answer": "Structured templates that place user input and retrieved text alongside instructions"
#     },
#     {
#         "question": "How does RAG help with cost and latency compared to very long prompts?",
#         "options": [
#             "By eliminating tokenization and decoding steps",
#             "By using shorter augmented prompts with only relevant retrieved text",
#             "By running all computations on CPU only",
#             "By caching model weights on disk"
#         ],
#         "answer": "By using shorter augmented prompts with only relevant retrieved text"
#     },
#     {
#         "question": "Which of the following is a reason RAG can improve answer freshness?",
#         "options": [
#             "It continuously retrains the LLM with new data",
#             "It uses external data sources that can be kept up-to-date",
#             "It forces the model to ignore its pretraining data",
#             "It increases the model’s context length"
#         ],
#         "answer": "It uses external data sources that can be kept up-to-date"
#     },
#     {
#         "question": "During tokenization in embedding, what is assigned to each token?",
#         "options": [
#             "A unique numerical ID with no intrinsic meaning",
#             "A cosine similarity score",
#             "A TF-IDF weight",
#             "A one-hot vector with dynamic length"
#         ],
#         "answer": "A unique numerical ID with no intrinsic meaning"
#     },
#     {
#         "question": "Which step produces the final answer in the RAG pipeline?",
#         "options": [
#             "Retrieve Relevant Data",
#             "Store Vectors",
#             "Obtain a Response (LLM processes the augmented prompt)",
#             "Embed Sources"
#         ],
#         "answer": "Obtain a Response (LLM processes the augmented prompt)"
#     },
#     {
#         "question": "Which of the following best summarizes how RAG mitigates the 'needle in a haystack' problem?",
#         "options": [
#             "By embedding the entire corpus into a single vector",
#             "By retrieving and passing only the most pertinent chunks to the LLM",
#             "By increasing the LLM’s maximum token limit",
#             "By removing punctuation during preprocessing"
#         ],
#         "answer": "By retrieving and passing only the most pertinent chunks to the LLM"
#     },
#     {
#         "question": "Which preprocessing step is mentioned as part of 'Gather Sources'?",
#         "options": [
#             "Converting documents like PDFs into plain text before embedding",
#             "Training a new LLM from scratch",
#             "Replacing all numbers with placeholders",
#             "Storing raw images directly in the vector store"
#         ],
#         "answer": "Converting documents like PDFs into plain text before embedding"
#     }
# ]

# questions = [
    # {
    #     "question": "Which of the following is an example of a **zero-shot prompt**?",
    #     "options": [
    #         "Explain the concept of quantum entanglement. Provide a step-by-step solution to this physics problem.",
    #         "Summarize the following text: [insert text here].",
    #         "Translate the following sentence into French: 'Hello, how are you?'.",
    #         "You are a helpful assistant. Provide a detailed summary of the main points from the provided article."
    #     ],
    #     "answer": "Translate the following sentence into French: 'Hello, how are you?'."
    # },
    # {
    #     "question": "Which of the following scenarios is a prime example of a **few-shot prompt**?",
    #     "options": [
    #         "Asking a model to define the term 'photosynthesis' without any prior examples.",
    #         "Providing a model with a list of historical events and asking it to chronologically order them.",
    #         "Giving a model three examples of sentiment analysis (e.g., 'This movie is great!' -> Positive) and then asking it to classify a new sentence.",
    #         "Using a single, complex instruction to guide a model through a multi-step problem."
    #     ],
    #     "answer": "Giving a model three examples of sentiment analysis (e.g., 'This movie is great!' -> Positive) and then asking it to classify a new sentence."
    # },
    # {
    #     "question": "What is the primary goal of using **Chain-of-Thought (CoT) prompting**?",
    #     "options": [
    #         "To provide a single, direct answer without any intermediate reasoning.",
    #         "To encourage the model to show its step-by-step reasoning before arriving at a final answer.",
    #         "To force the model to only use external knowledge sources.",
    #         "To train the model on a massive dataset of logical problems."
    #     ],
    #     "answer": "To encourage the model to show its step-by-step reasoning before arriving at a final answer."
    # },
    # {
    #     "question": "The **Self-Consistency** technique is most effective when used with which other prompting method?",
    #     "options": [
    #         "Basic zero-shot prompting.",
    #         "Few-shot prompting with very few examples.",
    #         "Chain-of-Thought (CoT) prompting.",
    #         "Direct instruction prompting."
    #     ],
    #     "answer": "Chain-of-Thought (CoT) prompting."
    # },
    # {
    #     "question": "Which prompt engineering technique is best suited for complex, multi-step arithmetic or logical reasoning problems?",
    #     "options": [
    #         "Zero-shot prompting.",
    #         "Few-shot prompting.",
    #         "Chain-of-Thought (CoT) prompting.",
    #         "Basic instruction-based prompting."
    #     ],
    #     "answer": "Chain-of-Thought (CoT) prompting."
    # },
    # {
    #     "question": "What is the key difference between **Zero-Shot CoT** and regular **Chain-of-Thought** prompting?",
    #     "options": [
    #         "Zero-Shot CoT requires a large number of examples, while regular CoT does not.",
    #         "Zero-Shot CoT uses a simple phrase like 'Let's think step by step' to elicit reasoning, while regular CoT relies on explicit step-by-step examples.",
    #         "Zero-Shot CoT is exclusively for creative writing, while regular CoT is for math problems.",
    #         "Zero-Shot CoT does not use an LLM, while regular CoT does."
    #     ],
    #     "answer": "Zero-Shot CoT uses a simple phrase like 'Let's think step by step' to elicit reasoning, while regular CoT relies on explicit step-by-step examples."
    # }
  # {
  #   "question": "Which of the following best describes the primary use case for LLMChain?",
  #   "options": [
  #     "Building complex, multi-step workflows with branching logic",
  #     "Creating simple, single-step prompt-and-response applications",
  #     "Enabling parallel execution of multiple model calls",
  #     "Debugging and tracing complex, multi-component applications"
  #   ],
  #   "answer": "Creating simple, single-step prompt-and-response applications"
  # },
  # {
  #   "question": "What is the key advantage of using LCEL's `|` (pipe) syntax?",
  #   "options": [
  #     "It requires explicit class instantiation for each component, increasing clarity",
  #     "It provides a declarative, functional approach that is more readable and concise",
  #     "It is the only way to integrate external tools and APIs in LangChain",
  #     "It allows for direct interaction with the LLM API without any abstractions"
  #   ],
  #   "answer": "It provides a declarative, functional approach that is more readable and concise"
  # },
  # {
  #   "question": "Which approach is generally recommended for building complex workflows that require branching and parallel processing?",
  #   "options": [
  #     "LLMChain",
  #     "LCEL",
  #     "Only `SimpleSequentialChain`",
  #     "Neither, as these are not core LangChain functionalities"
  #   ],
  #   "answer": "LCEL"
  # },
  # {
  #   "question": "A developer wants to create an application that streams the LLM's response token by token for a better user experience. Which method is natively supported by LCEL?",
  #   "options": [
  #     "The `invoke()` method with a special streaming flag",
  #     "The `stream()` and `astream()` methods",
  #     "The `run_and_wait()` method",
  #     "This is not a feature of either LCEL or LLMChain"
  #   ],
  #   "answer": "The `stream()` and `astream()` methods"
  # },
  # {
  #   "question": "What is the status of the `LLMChain` class in modern versions of the LangChain framework?",
  #   "options": [
  #     "It is the preferred method for all chain-building tasks",
  #     "It has been deprecated in favor of LCEL's `RunnableSequence` and pipe syntax",
  #     "It is a required component for all complex LCEL chains",
  #     "It is a legacy tool that is no longer maintained or supported"
  #   ],
  #   "answer": "It has been deprecated in favor of LCEL's `RunnableSequence` and pipe syntax"
  # },
  # {
  #   "question": "Which of the following is an LCEL primitive specifically designed for running multiple components simultaneously?",
  #   "options": [
  #     "RunnableSequence",
  #     "RunnablePassthrough",
  #     "RunnableParallel",
  #     "RunnableLambda"
  #   ],
  #   "answer": "RunnableParallel"
  # },
  # {
  #   "question": "When debugging a complex, multi-step chain, which approach provides better observability and automated logging with services like LangSmith?",
  #   "options": [
  #     "LLMChain",
  #     "LCEL",
  #     "Using the legacy `Agent` class",
  #     "Manually adding print statements at each step"
  #   ],
  #   "answer": "LCEL"
  # },
  # {
  #   "question": "LLMChain is best suited for scenarios where the chain involves a single LLM call and a single prompt template, making it ideal for:",
  #   "options": [
  #     "Complex agentic systems with tools",
  #     "Retrieval-Augmented Generation (RAG) pipelines",
  #     "Simple Q&A or summarization tasks",
  #     "Workflows with dynamic routing"
  #   ],
  #   "answer": "Simple Q&A or summarization tasks"
  # },
  # {
  #   "question": "Which approach is designed to be more modular and easily allow for swapping out components (e.g., changing the LLM or output parser) without rewriting the entire chain structure?",
  #   "options": [
  #     "LLMChain",
  #     "LCEL",
  #     "The `ConversationChain`",
  #     "The `VectorStoreRetriever`"
  #   ],
  #   "answer": "LCEL"
  # },
  # {
  #   "question": "Which of the following represents a declarative style for composing chains, allowing LangChain to optimize execution (e.g., parallelization) under the hood?",
  #   "options": [
  #     "Instantiating multiple LLMChain objects and calling their `run()` method sequentially",
  #     "The procedural-style code of a legacy `Agent`",
  #     "Using the LCEL pipe (`|`) syntax",
  #     "The `SequentialChain` class"
  #   ],
  #   "answer": "Using the LCEL pipe (`|`) syntax"
  # }
    # [
    # {"question": "What is the key mathematical difference between discriminative and generative models?",
    #  "options": ["Discriminative models estimate P(x, y)", "Generative models estimate P(y|x)",
    #              "Discriminative models estimate P(y|x)", "Generative models estimate P(x|y)"],
    #  "answer": "Discriminative models estimate P(y|x)"},
    # {"question": "Which model type is more suitable for semi-supervised learning tasks?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which AI model type is more likely to suffer from overfitting in high-dimensional data?",
    #  "options": ["Generative AI", "Discriminative AI", "Unsupervised AI", "Reinforcement AI"],
    #  "answer": "Generative AI"}, {
    #     "question": "Which of the following models is considered both generative and discriminative depending on its configuration?",
    #     "options": ["Naive Bayes", "Conditional Random Fields", "Variational Autoencoders",
    #                 "Hidden Markov Models"], "answer": "Hidden Markov Models"},
    # {"question": "Which AI model type is more robust to missing data?",
    #  "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in zero-shot learning scenarios?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type typically requires more computational resources during training?",
    #  "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in transfer learning applications?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more suitable for modeling complex dependencies between features?",
    #  "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in adversarial training setups?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in probabilistic graphical models?",
    #  "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in structured prediction tasks?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
    #  "answer": "Discriminative AI"},
    # {"question": "Which model type is more likely to be used in Bayesian inference?",
    #  "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in active learning scenarios?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
    #  "answer": "Discriminative AI"},
    # {"question": "Which model type is more likely to be used in unsupervised pretraining?",
    #  "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in multi-modal learning?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in few-shot learning?",
    #  "options": ["Discriminative AI", "Generative AI", "Predictive AI", "Reactive AI"],
    #  "answer": "Generative AI"},
    # {"question": "Which model type is more likely to be used in feature extraction tasks?",
    #  "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Cognitive AI"],
    #  "answer": "Discriminative AI"},
    # {"question": "Which model type is more likely to be used in reinforcement learning policy generation?",
    #  "options": ["Discriminative AI", "Generative AI", "Unsupervised AI", "Reactive AI"],
    #  "answer": "Generative AI"}, {
    #     "question": "Which model type is more likely to be used in synthetic data generation for privacy preservation?",
    #     "options": ["Discriminative AI", "Generative AI", "Symbolic AI", "Creative AI"],
    #     "answer": "Generative AI"}
# ]


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
