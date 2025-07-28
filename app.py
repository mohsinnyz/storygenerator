import os
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Page configuration
st.set_page_config(page_title="StoryGen - Mohsin Nyz", page_icon="🧑‍💻", layout="wide")

# Title and description
st.markdown("<h1 style='text-align: center;'>📚 StoryGen: AI Story Creator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Craft creative stories from your ideas using a fine-tuned AI storyteller!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Load model and tokenizer (cached)
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("mohsinnyz/storygen-gpt2medium-finetuned")
    model = GPT2LMHeadModel.from_pretrained("mohsinnyz/storygen-gpt2medium-finetuned")
    return tokenizer, model

tokenizer, model = load_model()

# Function to polish story using Gemini
def polish_with_gemini(story_text, character_name, genre, tone, theme, ending_type, max_length):
    if not GEMINI_API_KEY:
        return "[Gemini API key missing. Please set it in .env]"

    prompt = f"""
    You are an AI storyteller.

    Take this quirky, somewhat random raw AI-generated draft and improve it to be:
    - Coherent and {tone.lower()}
    - Belonging to the {genre.lower()} genre with a {ending_type.lower()} ending
    - Involve a character named {character_name or 'Zara'}
    - Keep the planet, plant, garden, and laughing cat scene
    - Match the theme: {theme or 'curiosity'}
    - Add a clear beginning, buildup, climax, and twist ending

    Raw Draft:
    {story_text}  # <--- Changed this line! Removed extra triple quotes.

    Polish this into a fun short story of around {max_length} words.
    """
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Gemini Error] {e}"

# Prompt input
prompt = st.text_area("Write Basic Story Direction", height=150, placeholder="e.g. A robot discovers an ancient library on Mars...")
st.markdown("---")

# Input columns
inputs_col, advanced_settings_col = st.columns([0.45, 0.55])

with inputs_col:
    st.subheader("Story Details")

    col1, col2 = st.columns(2)
    with col1:
        genre = st.selectbox("📚 Genre", ["Any", "Fantasy", "Sci-Fi", "Mystery", "Horror", "Adventure", "Romance"])
    with col2:
        tone = st.selectbox("🎝 Tone", ["Any", "Serious", "Funny", "Dramatic", "Poetic"])

    col3, col4 = st.columns(2)
    with col3:
        character_name = st.text_input("🧙 Main Character's Name", placeholder="e.g. Zara, Max, Captain Orion")
    with col4:
        theme = st.text_input("💡 Theme or Moral", placeholder="e.g. friendship, courage, redemption")

    ending_type = st.selectbox("🔚 Preferred Ending", ["Any", "Happy", "Tragic", "Open-ended", "Twist"])

with advanced_settings_col:
    st.subheader("Advanced Generation Settings")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        max_length = st.slider(
            "📏 Story Length",
            50, 300, 120,
            help="Controls how long the story will be. Higher = more content."
        )
    with col_s2:
        temperature = st.slider(
            "🔥 Creativity Level",
            0.5, 1.5, 1.0, 0.1,
            help="Higher = more imaginative and unexpected words. Lower = more focused and predictable."
        )

    col_s3, col_s4 = st.columns(2)
    with col_s3:
        top_k = st.slider(
            "📚 Word Pool Size",
            10, 100, 50,
            help="Determines how many likely words the AI considers at each step. Higher = more variety."
        )
    with col_s4:
        top_p = st.slider(
            "🎯 Word Pool Confidence",
            0.5, 1.0, 0.95,
            help="Controls how confidently the AI chooses the next word. Lower = focused, Higher = diverse."
        )

    num_return_sequences = st.slider(
        "🔁 Number of Stories",
        1, 3, 1,
        help="How many story versions do you want generated?"
    )

st.markdown("---")

# Generate story
if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a basic story prompt.")
    else:
        st.info("AI is cooking your story...")

        full_prompt = prompt.strip()
        if character_name:
            full_prompt += f" The main character is named {character_name}."
        if genre != "Any":
            full_prompt += f" The story belongs to the {genre.lower()} genre."
        if tone != "Any":
            full_prompt += f" It should have a {tone.lower()} tone."
        if theme:
            full_prompt += f" The theme of the story is about {theme}."
        if ending_type != "Any":
            full_prompt += f" The story should end in a {ending_type.lower()} way."

        inputs = tokenizer(full_prompt, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            num_return_sequences=num_return_sequences
        )

        # Display polished stories
        for i, output in enumerate(outputs):
            raw_story = tokenizer.decode(output, skip_special_tokens=True)

            polished_story = polish_with_gemini(
                raw_story,
                character_name,
                genre,
                tone,
                theme,
                ending_type,
                max_length
            )

            st.markdown(f"### ✨ Story Generated #{i + 1}")
            st.write(polished_story)
            st.markdown("---")

# Footer
st.markdown("<br><hr><center> Made with <3 by <a href='https://linkedin.com/in/mohsinnyz' target='_blank'>Mohsin Nyz</a></center>", unsafe_allow_html=True)
