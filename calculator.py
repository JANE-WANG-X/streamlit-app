import streamlit as st

def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "ERROR"

# Set up the Streamlit interface
st.title("Streamlit Calculator")

st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 60px);  /* 4 columns, each 60px wide */
        grid-gap: 5px;  /* Smaller gap between buttons */
        justify-content: center;
    }
    .grid-container button {
        font-size: 24px;
        padding: 10px;
        background-color: #f0f0f5;
        color: black;
        border: 2px solid #000;
        border-radius: 8px;
        width: 60px;
        height: 60px;
    }

    </style>
""", unsafe_allow_html=True)


# Initialize session state for storing the current expression and result
if 'expression' not in st.session_state:
    st.session_state.expression = ""

if 'result' not in st.session_state:
    st.session_state.result = ""

symbol_to_operator = {
    '&times;': '*',
    '&divide;': '/',
    '&minus;': '-',
    '&plus;': '+'
}

# Layout the buttons using columns (with HTML entities)
buttons = [
    ['7', '8', '9', '&divide;'],
    ['4', '5', '6', '&times;'],
    ['1', '2', '3', '&minus;'],
    ['0', '.', '=', '&plus;'],
    ['C']
]

# Button click handling logic
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if cols[i].button(button): 
            if button == 'C':
                st.session_state.expression = ""
                st.session_state.result = ""
            elif button == '=':
                st.session_state.result = evaluate_expression(st.session_state.expression)
            else:
                button_label = button.replace('&times;', '*').replace('&divide;', '/').replace('&minus;', '-').replace('&plus;', '+')
                st.session_state.expression += button_label

# Display the current expression and result after button handling
st.text_input("Expression", value=st.session_state.expression, key="display", disabled=True)
st.text_input("Result", value=st.session_state.result, key="result_display", disabled=True)

