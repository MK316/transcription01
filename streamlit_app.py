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
    {"word": "multiply", "transcriptions": ["ˈmʌɫ.tə.pl̥aɪ", "ˈmʌɫ.tɪ.pl̥aɪ"]},
    {"word": "multiple", "transcriptions": ["ˈmʌɫ.tə.pəl", "ˈmʌɫ.tɪ.pəl", "ˈmʌɫ.tɪ.pl̩"]},
    {"word": "regulate", "transcriptions": ["ˈɹɛ.ɡjə.leɪt", "ˈɹɛ.ɡjʊ.leɪt"]},
    {"word": "regular", "transcriptions": ["ˈɹɛ.ɡjə.lɚ", "ˈɹɛ.ɡjʊ.lɚ"]},
    {"word": "copulate", "transcriptions": ["ˈkʰɑ.pjə.leɪt", "ˈkʰɑ.pjʊ.leɪt"]},
    {"word": "copula", "transcriptions": ["ˈkʰɑ.pjə.lə", "ˈkʰɑ.pjʊ.lə"]},
    {"word": "circulate", "transcriptions": ["ˈsɝ.kjə.leɪt", "ˈsɝ.kjʊ.leɪt"]},
    {"word": "circular", "transcriptions": ["ˈsɝ.kjə.lɚ", "ˈsɝ.kjʊ.lɚ"]},
    {"word": "criticize", "transcriptions": ["ˈkɹ̥ɪ.tɪ.saɪz", "ˈkɹ̥ɪ.tə.saɪz", "ˈkɹ̥ɪ.ɾɪ.saɪz", "ˈkɹ̥ɪ.ɾə.saɪz"]},
    {"word": "critical", "transcriptions": ["ˈkɹ̥ɪ.tɪ.kəl", "ˈkɹ̥ɪ.tə.kəl", "ˈkɹ̥ɪ.ɾə.kəl", "ˈkɹ̥ɪ.ɾə.kəl"]},
    {"word": "minimize", "transcriptions": ["ˈmɪ.nɪ.maɪz", "ˈmɪ.nə.maɪz"]},
    {"word": "minimal", "transcriptions": ["ˈmɪ.nɪ.məɫ", "ˈmɪ.nə.məɫ"]},
    {"word": "explain", "transcriptions": ["ɪk.spleɪn", "ɛk.spleɪn"]},
    {"word": "explanation", "transcriptions": ["ɪk.splə.ˈneɪ.ʃən", "ɛk.splə.ˈneɪ.ʃən"]},
    {"word": "exploit", "transcriptions": ["ɪk.ˈsplɔɪt", "ɪk.ˈsplɔɪt"]},
    {"word": "exploitation", "transcriptions": ["ɪk.splɔɪ.ˈtʰeɪ.ʃən", "ɛk.splɔɪ.ˈtʰeɪ.ʃən"]},
    {"word": "photograph", "transcriptions": ["ˈfoʊ.tə.ɡɹæf", "ˈfoʊ.ɾə.ɡɹæf"]},
    {"word": "photography", "transcriptions": ["fə.ˈtʰɑ.ɡɹə.fi"]},
    {"word": "photographic", "transcriptions": ["foʊ.tə.ˈɡɹæ.fɪk", "foʊ.ɾə.ˈɡɹæ.fɪk"]}
]

# Initialize session state
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = word_transcriptions.copy()
    random.shuffle(st.session_state.remaining_words)
    st.session_state.current_word = None
    st.session_state.feedback = ""

# Button to show a random word
if st.button("Show me a word"):
    st.markdown("""
    ### Notes:
    1. Use an **approximant 'r'**.
    2. Use **'r-colored vowels'**.
    3. Check **diacritics** such as:
       - Aspiration (e.g., /pʰ/, /tʰ/, /kʰ/)
       - Devoicing (e.g., [z̥], [d̥])
       - Velarized 'l' (e.g., /ɫ/)
       - Primary stress (e.g., ˈ)
    """)

    if st.session_state.remaining_words:
        st.session_state.current_word = st.session_state.remaining_words.pop()
        st.session_state.feedback = ""  # Reset feedback
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
            st.session_state.feedback = "Correct!"
        else:
            st.error(f"Incorrect. Acceptable answers: {', '.join(correct_transcriptions)}")
            st.session_state.feedback = f"Incorrect. Acceptable answers: {', '.join(correct_transcriptions)}"

    # Display feedback after submission
    if st.session_state.feedback:
        st.write(st.session_state.feedback)
