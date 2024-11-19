import streamlit as st
import random

# Dataset with multiple transcriptions for some words
word_transcriptions = [
    {"word": "diplomat", "transcriptions": ["ˈdɪ.plə.mæt"]},
    {"word": "diplomacy", "transcriptions": ["dɪ.ˈpl̥oʊ.mə.si"]},
    {"word": "diplomatic", "transcriptions": ["ˌdɪ.plə.ˈmæ.tɪk", "ˌdɪ.plə.ˈmæ.ɾɪk"]},
    {"word": "monotone", "transcriptions": ["ˈmɑ.nə.tʰoʊn"]},
    {"word": "monotony", "transcriptions": ["mə.ˈnɑ.tə.ni"]},
    {"word": "monotonic", "transcriptions": ["mɑ.nə.ˈtʰɑ.nɪk"]},
    {"word": "multiply", "transcriptions": ["ˈmʌl.tə.pl̥aɪ", "ˈmʌl.tɪ.pl̥aɪ"]},
    {"word": "multiple", "transcriptions": ["ˈmʌl.tə.pəl", "ˈmʌl.tɪ.pəl", "ˈmʌl.tɪ.pl̩"]},
    {"word": "regulate", "transcriptions": ["ˈrɛ.ɡjə.leɪt", "ˈrɛ.ɡjʊ.leɪt"]},
    {"word": "regular", "transcriptions": ["ˈrɛ.ɡjə.lər", "ˈrɛ.ɡjʊ.lər"]},
    {"word": "copulate", "transcriptions": ["ˈkʰɑ.pjə.leɪt", "ˈkʰɑ.pjʊ.leɪt"]},
    {"word": "copula", "transcriptions": ["ˈkʰɑ.pjə.lə", "ˈkʰɑ.pjʊ.lə"]},
    {"word": "circulate", "transcriptions": ["ˈsɜr.kjə.leɪt", "ˈsɜr.kjʊ.leɪt"]},
    {"word": "circular", "transcriptions": ["ˈsɜr.kjə.lər", "ˈsɜr.kjʊ.lər"]},
    {"word": "criticize", "transcriptions": ["ˈkɹ̥ɪ.tɪ.saɪz", "ˈkɹ̥ɪ.tə.saɪz", "ˈkɹ̥ɪ.ɾɪ.saɪz", "ˈkɹ̥ɪ.ɾə.saɪz"]},
    {"word": "critical", "transcriptions": ["ˈkɹ̥ɪ.tɪ.kəl", "ˈkɹ̥ɪ.tə.kəl", "ˈkɹ̥ɪ.ɾə.kəl", "ˈkɹ̥ɪ.ɾə.kəl"]},
    {"word": "minimize", "transcriptions": ["ˈmɪ.nɪ.maɪz", "ˈmɪ.nə.maɪz"]},
    {"word": "minimal", "transcriptions": ["ˈmɪ.nɪ.məl", "ˈmɪ.nə.məl"]},
    {"word": "explain", "transcriptions": ["ɪk.spleɪn", "ɛk.spleɪn"]},
    {"word": "explanation", "transcriptions": ["ɪk.splə.ˈneɪ.ʃən", "ɛk.splə.ˈneɪ.ʃən"]},
    {"word": "exploit", "transcriptions": ["ɪk.ˈsplɔɪt", "ɪk.ˈsplɔɪt"]},
    {"word": "exploitation", "transcriptions": ["ɪk.splɔɪ.ˈtʰeɪ.ʃən", "ɛk.splɔɪ.ˈtʰeɪ.ʃən"]},
    {"word": "photograph", "transcriptions": ["ˈfoʊ.tə.ɡræf", "ˈfoʊ.ɾə.ɡræf"]},
    {"word": "photography", "transcriptions": ["fə.ˈtʰɑ.ɡrə.fi"]},
    {"word": "photographic", "transcriptions": ["foʊ.tə.ˈɡræ.fɪk", "foʊ.ɾə.ˈɡræ.fɪk"]}
]


# Initialize session state
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = word_transcriptions.copy()
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Title
st.title("Phonetic Transcription Practice")

# Show a word button
if st.button("Show me a word"):
    if st.session_state.remaining_words:
        # Select a random word
        st.session_state.current_word = random.choice(st.session_state.remaining_words)
        st.session_state.remaining_words.remove(st.session_state.current_word)
        st.session_state.feedback = ""  # Reset feedback
    else:
        st.warning("No more words left to practice!")

# Display the current word
if st.session_state.current_word:
    st.subheader(f"Word: {st.session_state.current_word['word']}")
    user_input = st.text_input("Provide the phonetic transcription of this word (use [ ] brackets):")

    # Check answer
    if st.button("Submit"):
        # Normalize user input (remove brackets and whitespace)
        normalized_input = user_input.strip().strip("[]")
        correct_transcriptions = st.session_state.current_word["transcriptions"]

        if normalized_input in correct_transcriptions:
            st.session_state.feedback = "✅ Correct!"
        else:
            correct_transcriptions_str = ", ".join([f"[{trans}]" for trans in correct_transcriptions])
            st.session_state.feedback = f"❌ Incorrect! Check this: {correct_transcriptions_str}"

    # Display feedback
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

# Reset button for users who want to restart
if st.button("Restart"):
    st.session_state.remaining_words = word_transcriptions.copy()
    st.session_state.current_word = None
    st.session_state.feedback = ""
    st.experimental_rerun()
