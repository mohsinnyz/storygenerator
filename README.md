
---

````markdown
 ### 📚 StoryGen: AI Story Creator

---

## 🧠 About the Project

**StoryGen** is an interactive AI-powered web application built with Streamlit that helps users craft creative short stories from a basic idea. At its core, it leverages a **fine-tuned GPT-2 model (`mohsinnyz/storygen-gpt2medium-finetuned`)** for the primary generation of narrative drafts. To ensure the final output is coherent and aligns with specific creative parameters, the Google Gemini 1.5 Flash API is used for final touches and polishing.

The goal of StoryGen is to provide an intuitive interface for anyone to experiment with AI-driven creative writing, from hobbyists to writers looking for inspiration.

---

## ✨ Features

- **GPT-2 Powered Draft Generation:** Generates initial story drafts based on user prompts and selected creative parameters using a powerful fine-tuned GPT-2 model.
- **Customizable Story Details:**
  - Select from various **genres** (Fantasy, Sci-Fi, Mystery, Horror, Adventure, Romance, or "Any").
  - Choose a desired **tone** (Serious, Funny, Dramatic, Poetic, or "Any").
  - Define a **main character's name**.
  - Specify a central **theme or moral**.
  - Pick a **preferred ending type** (Happy, Tragic, Open-ended, Twist, or "Any").
- **Advanced Generation Settings (for GPT-2):**
  - Control **story length** (50 to 300 words).
  - Adjust **creativity level (temperature)**.
  - Set **top_k** and **top_p** values for fine-grained control.
  - Generate **multiple story versions** (1 to 3).
- **Gemini LLM for Polishing:** Final polishing and rewriting using Google Gemini 1.5 Flash to improve coherence, flow, and creative alignment.
- **User-Friendly Interface:** Built with Streamlit for simplicity and interactivity.

---

## 🚀 Live Demo

Try the live version here:  
👉 [https://mohsinnyz-storygen.streamlit.app](https://mohsinnyz-storygen.streamlit.app)

---##

## 🛠 Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Interactive frontend.
- **Hugging Face Transformers**
  - `GPT2LMHeadModel`, `GPT2Tokenizer` – For text generation.
- **Google Gemini API** – For story enhancement.
- **python-dotenv** – Securely manage API keys locally.

---

## 🖥️ Getting Started Locally

To run this project on your machine:

### ✅ Prerequisites

- Python 3.8+
- `pip`

### 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mohsinnyz/storygenerator.git
   cd storygenerator
````

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it:

   * **Windows:**

     ```bash
     .\venv\Scripts\activate
     ```
   * **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file:

   ```ini
   GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
   ```

---

### ▶️ Running the Application

Start the app:

```bash
streamlit run app.py
```

---

## ☁️ Deployment on Streamlit Community Cloud

To deploy:

1. Push your code to a GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Click **"New app"** → select the GitHub repo.
4. Set the Python file to `app.py`.
5. Add a **secret** (API key) in the **"Secrets"** section:

   ```
   GEMINI_API_KEY = "your_actual_api_key"
   ```
6. Click **Deploy**.

---

## 🙏 Acknowledgements

* Hugging Face 🤗 for the transformers library.
* Google for Gemini API.
* Streamlit for the UI framework.

---

## 📬 Contact

**Developer:** Mohsin Niaz
**GitHub:** [@mohsinnyz](https://github.com/mohsinnyz)
**Email:** [mohsinnyz@gmail.com](mailto:mohsinnyz@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```

---

Let me know if you want:
- The license file auto-generated (`MIT`).
- A new logo/banner.
- GitHub tags/badges (e.g., stars, forks, Streamlit deployed status).
- A `setup.sh` for one-click deployment.

You’re almost there!
```
