# 📝 Text Summariser

An AI-powered text summarisation application built using **Python, LangChain, OpenAI, and Streamlit**. It summarises long text documents into concise, meaningful summaries while preserving important information.

The application uses OpenAI's `gpt-3.5-turbo` model and an iterative summarisation pipeline to process long documents in manageable chunks.

## ✨ Features

- **AI-Powered Summarisation:** Generates concise summaries using OpenAI's language models.
- **Long Document Support:** Splits lengthy text into smaller, overlapping chunks for progressive processing.
- **Iterative Summary Refinement:** Updates the existing summary with important information from subsequent chunks.
- **Customisable Summary Length:** Specify the desired summary length between 10 and 300 words.
- **Interactive Web Interface:** A simple Streamlit UI for entering text and viewing generated summaries.
- **Side-by-Side Comparison:** Displays the original text and the generated summary in separate panels.
- **Input Validation:** Prevents summarisation when the input contains only whitespace.

## 🧠 AI Model

| Component | Technology |
|---|---|
| Language Model | OpenAI `gpt-3.5-turbo` |
| LLM Framework | LangChain |
| Text Chunking | `RecursiveCharacterTextSplitter` |
| Token Counting | `tiktoken` |
| Prompt Management | LangChain `PromptTemplate` |
| Output Parsing | `StrOutputParser` |
| Web Interface | Streamlit |
| Programming Language | Python |

The model is configured with a temperature of `0.1` to encourage consistent and focused summaries.

## ⚙️ How It Works

The summarisation engine is implemented in `text_summariser.py`. It uses a progressive summarisation strategy instead of processing the entire document in a single request.

### 1. Text Chunking

The input document is divided into smaller, overlapping chunks using LangChain's `RecursiveCharacterTextSplitter`.

- **Chunk size:** 2,500 tokens
- **Chunk overlap:** 200 tokens
- **Token counting:** Powered by `tiktoken`

Overlapping chunks help preserve context between consecutive sections of the document.

### 2. Initial Summary Generation

The first chunk is passed to the OpenAI language model through a LangChain pipeline. A custom prompt template guides the model in generating an initial summary.

This summary becomes the foundation for processing the remaining chunks.

### 3. Iterative Summary Refinement

Each subsequent chunk is processed alongside the summary generated so far.

A refinement prompt instructs the model to incorporate important information from the new chunk while retaining relevant information from the existing summary.

This process continues until the final chunk is reached.

### 4. Final Summary Generation

The last chunk is processed using a dedicated final refinement prompt.

The model receives the existing summary, the remaining text, and the requested word limit to generate the final refined summary.

### 5. LangChain Expression Language (LCEL)

The summarisation pipeline uses LangChain's Expression Language to connect prompts, the language model, and the output parser into reusable processing chains.

- `PromptTemplate` — Defines the instructions provided to the language model.
- `ChatOpenAI` — Generates and refines summaries.
- `StrOutputParser` — Converts model responses into plain text.

### 🔄 Summarisation Workflow

1. Accept the input text and desired summary length.
2. Divide the document into overlapping chunks.
3. Generate an initial summary from the first chunk.
4. Iteratively refine the summary using subsequent chunks.
5. Apply the final refinement prompt to the last chunk.
6. Return the final summary to the user through the Streamlit interface.

## 🖥️ Streamlit User Interface

The application's user interface is implemented in `app.py`.

### Interface Features

- **Text Input:** Paste the document into a dedicated text area.
- **Summary Length Slider:** Choose a target summary length from 10 to 300 words, with a default of 50 words.
- **Summarize Button:** Initiates the summarisation pipeline.
- **Clear Button:** Resets the input area.
- **Two-Column Layout:** Displays the original text and generated summary side by side.
- **Input Validation:** Displays an error message when the input is empty.
- **Interactive Feedback:** Provides an informational message before processing the text.

### UI Processing Flow

1. Streamlit initialises the page with a wide layout.
2. The input text is collected and maintained using `st.session_state`.
3. The user selects the desired summary length.
4. The application validates the input when the Summarize button is clicked.
5. The text is prepared for summarisation using `text_to_chunk_convert()`.
6. The `create_summary()` function generates the summary from the chunks.
7. The resulting summary is displayed in the output panel.

## 📁 Project Structure

```text
foss-text-summariser/
│
├── app.py                      # Streamlit user interface
├── model
  ├── text_summariser.py          # Text chunking and summarisation pipeline
  ├── prompt_template_strings.py  # Custom prompt templates
├── .env                        # OpenAI API key (not committed)
├── .gitignore                  # Files excluded from Git
└── README.md                   # Project documentation
```

*Note: The structure above is illustrative. Adjust the filenames and directories to match the actual repository.*

## 🚀 Getting Started

Follow these steps to run the application locally.

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- An OpenAI API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/rishavsarkardev/foss-text-summariser.git
```

Navigate to the project directory:

```bash
cd foss-text-summariser
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Your OpenAI API Key

Create a `.env` file in the project's root directory and add your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

**Important:** Never commit your `.env` file or expose your API key publicly. Add `.env` to your `.gitignore` file.

### 5. Run the Application

From the project's root directory, execute:

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal. Open that URL in your browser to use the summariser.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | API key used to authenticate requests to OpenAI |

## 🛠️ Technologies Used

- **Python:** Core application logic.
- **OpenAI API:** Generates and refines summaries.
- **LangChain:** Orchestrates the language model and summarisation pipeline.
- **LangChain Expression Language (LCEL):** Connects prompts, model calls, and output parsing.
- **tiktoken:** Supports token-based text splitting.
- **Streamlit:** Provides the interactive web interface.
- **python-dotenv:** Loads environment variables from the `.env` file.

## 🎯 Project Objective

The goal of this project is to explore the practical implementation of Large Language Models (LLMs) for natural language processing. It demonstrates how text chunking, prompt engineering, iterative refinement, and a web-based interface can be combined to build an application for summarising long-form text.

## 👨‍💻 Author

**Rishav Sarkar**

- GitHub: [@rishavsarkardev](https://github.com/rishavsarkardev)

---
