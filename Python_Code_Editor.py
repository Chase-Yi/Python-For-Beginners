import streamlit as st
from streamlit_ace import st_ace
import subprocess
import tempfile

# Set up page configuration
st.set_page_config(page_title="Code Editor", page_icon=":books:", layout="wide")

# Title and Instructions
st.title("Python Code Editor")
st.write("Write your Python code below and press 'Run' to see the output.")

# Sidebar for settings
with st.sidebar:
    theme = st.selectbox("Editor Theme",["dracula"])
    font_size = st.selectbox("Font Size",[20])
    show_gutter = st.checkbox("Show Line Numbers",value=True)
    language = st.selectbox("Language",["python"])

# Initialize session state for saved code
if "saved_code" not in st.session_state:
    st.session_state["saved_code"] = ""  # Initialize with an empty string

# Code editor function
def code_editor(code_content):
    code = st_ace(
        value=code_content,
        language=language,
        theme=theme,
        font_size=font_size,
        show_gutter=show_gutter,
        auto_update=True,
        key="python_editor",
        keybinding="vscode",
        max_lines=None)
    return code

# Display the code editor with session state content
code = code_editor(code_content=st.session_state["saved_code"])

# Save user input back to session state
st.session_state["saved_code"] = code

# Create a temporary file to save the code
with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as temp_file:
    temp_file.write(code)
    temp_file_path = temp_file.name

# Run button
if st.button("Run"):
    try:
        # Run the code and capture the output
        result = subprocess.run(
            ["python", temp_file_path],
            capture_output=True,
            text=True
        )

        # Display the output
        st.subheader("Output:")
        st.text(result.stdout)
        if result.stderr:
            st.error(result.stderr)
    except Exception as e:
        st.error(f"Error: {e}")

# streamlit run Python_Code_Editor.py
