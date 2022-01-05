import streamlit as st
from streamlit.logger import get_logger

from duplicazer.core import remove_duplicate, find_duplicate
from duplicazer.constant import APP_PARAMS

st_logger = get_logger(__name__)


def clear():
    st.session_state["input_text"] = ""
    st.session_state["output_text"] = ""


if __name__ == "__main__":
    st.title(APP_PARAMS["title"])
    st.markdown(APP_PARAMS["description"])

    # Column initiailzation
    left, right = st.columns(2)
    remove_button, find_button, clear_button = st.columns([0.4, 1.1, 0.17])

    with left:
        input_text = st.text_area(
            label=APP_PARAMS["left_label"],
            height=APP_PARAMS["left_height"],
            key="input_text",
        )
    with right:
        output_text = st.text_area(
            label=APP_PARAMS["right_label"],
            height=APP_PARAMS["right_height"],
            key="output_text",
        )

    with remove_button:
        st.button(label=APP_PARAMS["remove_button_label"])
    with find_button:
        st.button(label=APP_PARAMS["find_button_label"])
    with clear_button:
        st.button(label=APP_PARAMS["clear_button_label"], on_click=clear)

    # Button trigger!
    if remove_button:
        print(remove_duplicate(input_text))

    if find_button:
        print(find_duplicate(input_text))
