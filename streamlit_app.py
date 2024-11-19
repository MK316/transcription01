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
    random.shuffle(st.session_state.remaining_words)
    st.session_state.current_word = None

# Button to show a random word
if st.button("Show me a word"):
    if st.session_state.remaining_words:
        st.session_state.current_word = st.session_state.remaining_words.pop()
    else:
        st.success("You've completed all words!")
        st.stop()

# Display word and input box if a word is available
if st.session_state.current_word:
    st.write(f"Word: **{st.session_state.current_word['word']}**")
    user_input = st.text_input("Provide the phonetic transcription (e.g., [ˈdɪ.plə.mæt]):")

    if st.button("Submit"):
        correct_transcriptions = st.session_state.current_word["transcriptions"]
        if user_input.strip("[]") in correct_transcriptions:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Acceptable answers: {', '.join(correct_transcriptions)}")
