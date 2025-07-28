Understood. I will provide a README.md file that emphasizes GPT-2 as the primary generation model and mentions Gemini LLM only for "final touches or polishing." The output will be a copy-paste ready file only, with no additional conversational text.

````markdown
# 📚 StoryGen: AI Story Creator

![Streamlit App - StoryGen](https://user-images.githubusercontent.com/mohsinnyz/storygenerator/assets/your_screenshot_name.png) ## Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Live Demo](#live-demo)
* [Technologies Used](#technologies-used)
* [Getting Started Locally](#getting-started-locally)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the Application](#running-the-application)
* [Deployment on Streamlit Community Cloud](#deployment-on-streamlit-community-cloud)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)

---

## About the Project

**StoryGen** is an interactive AI-powered web application built with Streamlit that helps users craft creative short stories from a basic idea. At its core, it leverages a **fine-tuned GPT-2 model (`mohsinnyz/storygen-gpt2medium-finetuned`)** for the primary generation of narrative drafts. To ensure the final output is coherent and aligns with specific creative parameters, the Google Gemini 1.5 Flash API is used for final touches and polishing.

The goal of StoryGen is to provide an intuitive interface for anyone to experiment with AI-driven creative writing, from hobbyists to writers looking for inspiration.

## Features

* **GPT-2 Powered Draft Generation:** Generates initial story drafts based on user prompts and selected creative parameters using a powerful fine-tuned GPT-2 model.
* **Customizable Story Details:**
    * Select from various **genres** (Fantasy, Sci-Fi, Mystery, Horror, Adventure, Romance, or "Any").
    * Choose a desired **tone** (Serious, Funny, Dramatic, Poetic, or "Any").
    * Define a **main character's name**.
    * Specify a central **theme or moral**.
    * Pick a **preferred ending type** (Happy, Tragic, Open-ended, Twist, or "Any").
* **Advanced Generation Settings (for GPT-2):**
    * Control **story length** (50 to 300 words).
    * Adjust **creativity level (temperature)** for more imaginative or predictable outputs.
    * Set **word pool size (top_k)** and **word pool confidence (top_p)** for fine-grained control over word selection.
    * Generate **multiple story versions** (1 to 3).
* **Gemini LLM for Polishing:** Employs the Google Gemini 1.5 Flash model to provide final refinements, enhancing coherence, narrative flow, and ensuring the story meets specified genre, tone, and ending requirements.
* **User-Friendly Interface:** Built with Streamlit for a clean and interactive web experience.

## Live Demo

Experience StoryGen live on Streamlit Community Cloud:

[**https://mohsinnyz-storygen.streamlit.app/**](https://mohsinnyz-storygen.streamlit.app/)
*(Note: Please update this link with your actual custom URL once set in Streamlit Cloud, if `mohsinnyz-storygen` was unavailable.)*

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **Hugging Face Transformers:**
    * `GPT2LMHeadModel`: The primary model for initial text generation (specifically `mohsinnyz/storygen-gpt2medium-finetuned`).
    * `GPT2Tokenizer`: For handling text encoding and decoding for the GPT-2 model.
* **Google Gemini API (`google-generativeai`):** Utilized for the final polishing and refinement of generated stories.
* **python-dotenv:** For securely loading API keys during local development.

## Getting Started Locally

To run this project on your local machine, follow these steps:

### Prerequisites

* Python 3.8+ (recommended 3.10)
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mohsinnyz/storygenerator.git](https://github.com/mohsinnyz/storygenerator.git)
    cd storygenerator
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your Gemini API Key:**
    * Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Create a file named `.env` in the root directory of your project (the same directory as `app.py`).
    * Add your API key to this file in the following format:
        ```
        GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
        ```
        **Important:** Do not commit this `.env` file to your Git repository. It's already included in `.gitignore` for this reason.

### Running the Application

Once the setup is complete, run the Streamlit application:

```bash
streamlit run app.py
````

This will open the application in your default web browser.

## Deployment on Streamlit Community Cloud

This application is deployed on Streamlit Community Cloud. If you wish to deploy your own version:

1.  Ensure your code is pushed to a GitHub repository (like this one).
2.  Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Connect your GitHub repository and select the `app.py` file as your main script.
4.  **Crucially, set your `GEMINI_API_KEY` in the Streamlit Cloud "Secrets" section** of your app's settings.
      * Click the three dots next to your app -\> Settings -\> Secrets.
      * Add the secret in TOML format:
        ```toml
        GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
        ```
      * Save the changes, and the app will redeploy.

## Acknowledgements

  * **Streamlit:** For providing an amazing platform for rapid app development.
  * **Hugging Face Transformers:** For the powerful GPT-2 model and tokenizer, central to the story generation.
  * **Google Gemini API:** For enabling the final text polishing capabilities.
  * The broader AI and open-source communities for their invaluable contributions.

## Contact

Feel free to connect with me:

  * **GitHub:** [mohsinnyz](https://www.google.com/search?q=https://github.com/mohsinnyz)
  * **LinkedIn:** [Mohsin Nyz](https://www.google.com/search?q=https://linkedin.com/in/mohsinnyz)

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```
```