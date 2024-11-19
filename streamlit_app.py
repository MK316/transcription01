import streamlit as st
import random

# Dataset of words and transcriptions
word_transcriptions = [
    {"word": "diplomat", "transcription": "ˈdɪ.plə.mæt"},
    {"word": "diplomacy", "transcription": "dɪ.ˈploʊ.mə.si"},
    {"word": "diplomatic", "transcription": "ˌdɪ.plə.ˈmæ.tɪk"},
    {"word": "monotone", "transcription": "ˈmɑ.nə.toʊn"},
    {"word": "monotony", "transcription": "mə.ˈnɑ.tə.ni"},
    {"word": "monotonic", "transcription": "mɑ.nə.ˈtɑ.nɪk"},
    {"word": "multiply", "transcription": "ˈmʌl.tə.plaɪ"},
    {"word": "multiple", "transcription": "ˈmʌl.tə.pəl"},
    {"word": "regulate", "transcription": "ˈrɛ.ɡjə.leɪt"},
    {"word": "regular", "transcription": "ˈrɛ.ɡjə.lər"},
    {"word": "copulate", "transcription": "ˈkɑ.pjə.leɪt"},
    {"word": "copula", "transcription": "ˈkɑ.pjə.lə"},
    {"word": "circulate", "transcription": "ˈsɜr.kjə.leɪt"},
    {"word": "circular", "transcription": "ˈsɜr.kjə.lər"},
    {"word": "criticize", "transcription": "ˈkrɪ.tɪ.saɪz"},
    {"word": "critical", "transcription": "ˈkrɪ.tɪ.kəl"},
    {"word": "minimize", "transcription": "ˈmɪ.nɪ.maɪz"},
    {"word": "minimal", "transcription": "ˈmɪ.nɪ.məl"},
    {"word": "explain", "transcription": "ɪk.spleɪn"},
    {"word": "explanation", "transcription": "ɛk.splə.ˈneɪ.ʃən"},
    {"word": "exploit", "transcription": "ɪk.ˈsplɔɪt"},
    {"word": "exploitation", "transcription": "ɛk.splɔɪ.ˈteɪ.ʃən"},
    {"word": "photograph", "transcription": "ˈfoʊ.tə.ɡræf"},
    {"word": "photography", "transcription": "fə.ˈtɑ.ɡrə.fi"},
    {"word": "photographic", "transcription": "foʊ.tə.ˈɡræ.fɪk"}
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
        correct_transcription = f"[{st.session_state.current_word['transcription']}]"
        if user_input.strip() == correct_transcription:
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = f"❌ Incorrect! Check this: {correct_transcription}"

    # Display feedback
    if st.session_state.feedback:
        st.write(st.session_state.feedback)

# Reset button for users who want to restart
if st.button("Restart"):
    st.session_state.remaining_words = word_transcriptions.copy()
    st.session_state.current_word = None
    st.session_state.feedback = ""
    st.experimental_rerun()
