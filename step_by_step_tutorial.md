# Part 1 Main Page

## Step 1: Import Required Libraries
```python
import streamlit as st
from streamlit_ace import st_ace
import subprocess
import tempfile
```
This step imports the necessary libraries for the Streamlit web app. `streamlit` is the main library used for building web applications, `streamlit_ace` provides an interactive code editor, `subprocess` allows running external commands, and `tempfile` helps in creating temporary files.

## Step 2: Set Up Page Configuration
```python
st.set_page_config(page_title="Code Editor", page_icon=":books:", layout="wide")
```
This step configures the web page settings, setting the title to "Code Editor", the page icon to a book emoji, and the layout to "wide".

## Step 3: Title and Instructions
```python
st.title("Python Code Editor")
st.write("Write your Python code below and press 'Run' to see the output.")
```
This step adds a title to the page and provides instructions for the user on how to use the code editor.

## Step 4: Sidebar for Settings
```python
with st.sidebar:
    theme = st.selectbox("Editor Theme", ["dracula"])
    font_size = st.selectbox("Font Size", [20])
    show_gutter = st.checkbox("Show Line Numbers", value=True)
    language = st.selectbox("Language", ["python"])
```
This step creates a sidebar where the user can select the editor theme, font size, whether to show line numbers, and the programming language for the code editor.

## Step 5: Initialize Session State for Saved Code
```python
if "saved_code" not in st.session_state:
    st.session_state["saved_code"] = ""  # Initialize with an empty string
```
This step initializes the session state to store the saved code in the user's session.

## Step 6: Code Editor Function
```python
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
```
This function creates an interactive code editor using `st_ace` and returns the editor instance.

## Step 7: Display the Code Editor with Session State Content
```python
code = code_editor(code_content=st.session_state["saved_code"])
```
This step displays the code editor with the content from the session state.

## Step 8: Save User Input Back to Session State
```python
st.session_state["saved_code"] = code
```
This step saves the code entered by the user back into the session state.

## Step 9: Create a Temporary File to Save the Code
```python
with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as temp_file:
    temp_file.write(code)
    temp_file_path = temp_file.name
```
This step creates a temporary file and writes the code from the editor into it, then saves the path to the temporary file.

## Step 10: Run Button
```python
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
```
This step adds a "Run" button that, when clicked, executes the Python code in the temporary file and displays the output in the web app.

# Part 2 Second Page

Please note that the code for the second page is quite extensive and detailed explanations are provided only up to the `<if option == 'Print':>` code block. To replicate the project, you should place the code for the second page into a folder named 'pages'.

## Step 1: Import Required Libraries
```python
import os
import streamlit as st
from streamlit_option_menu import option_menu
```
This step imports the necessary libraries for the Streamlit web app, including `os` for file operations and `streamlit_option_menu` for creating a menu.

## Step 2: Set Up Page Configuration
```python
st.set_page_config(page_title="Python For Beginners", page_icon=":books:", layout="wide")
```
This step configures the web page settings, setting the title to "Python For Beginners", the page icon to a book emoji, and the layout to "wide".

## Step 3: Load Image Function
```python
@st.cache_data
def load_image(image_path):
    return image_path
```
This function is used to cache and load images for display on the web page.

## Step 4: Key Concepts List
```python
key_concept = ['Print', 'Variable', 'Math', 'Comment', 'Data Type', 'Interactive Mode', 'Input', 'Condition',
               'Logical Operators', 'List', 'Dictionary', 'For Loop', 'While Loop', 'String Formatting', 'Function',
               'Importing Module', 'Object-Oriented Programming', 'Class', 'Inheritance', 'File Path', 'Read File', 'Write File',
               'Higher-order function & Lambda']
```
This step defines a list of key concepts that will be used to create a menu for the user to select different topics.

## Step 5: Initialize Session State for Current Option
```python
if 'current_option' not in st.session_state:
    st.session_state['current_option'] = key_concept[0]
```
This step initializes the session state to store the current selected option from the menu.

## Step 6: Menu Options
```python
option = option_menu(
    menu_title=None,
    options=key_concept,
    icons=['filetype-py']*len(key_concept),
    orientation='horizontal',
    default_index=key_concept.index(st.session_state['current_option']),
    key='menu'
)
```
This step creates a menu for the user to select different topics from the list of key concepts.

## Step 7: Update Session State with Selected Option
```python
st.session_state['current_option'] = option
```
This step updates the session state with the selected option from the menu.

## Step 8: Print Topic Page
```python
if option == 'Print':
    st.write('### print | 打印')
    
    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=6&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="print | 让程序给你打印“爸爸”", icon=":material/smart_display:")
    py_1 = '''
        print("Dad!")
        print("妈！！")
        '''
    st.code(py_1,language='python')
    
    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=7&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="更多 print | 让程序给你打印一首诗", icon=":material/smart_display:")
    py_2 = '''
        print("你好" + " 这是一句代码" + " 哈哈")
        '''
    py_3 = '''
        print("""君不见，黄河之水天上来，奔流到海不复回。
        君不见，高堂明镜悲白发，朝如青丝暮成雪。
        人生得意须尽欢，莫使金樽空对月。
        天生我材必有用，千金散尽还复来。
        烹羊宰牛且为乐，会须一饮三百杯。
        岑夫子，丹丘生，将进酒，君莫停。
        与君歌一曲，请君为我倾耳听。
        钟鼓馔玉不足贵，但愿长醉不复醒。
        古来圣贤皆寂寞，惟有饮者留其名。
        陈王昔时宴平乐，斗酒十千恣欢谑。
        主人何为言少钱，径须沽取对君酌。
        五花马，千金裘，呼儿将出换美酒，
        与尔同销万古愁。""")
        '''
    st.code(py_2,language='python')
    st.code(py_3,language='python')
```
This step provides an explanation and examples of the `print` function in Python, including how to print simple text and formatted strings.

