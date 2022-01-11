import streamlit as st
from streamlit.logger import get_logger

from duplicazer.core import remove_duplicate, find_duplicate
from duplicazer.constant import APP_PARAMS

st_logger = get_logger(__name__)

st.set_page_config(
    layout=APP_PARAMS["layout"],
    page_title=APP_PARAMS["title"],
    page_icon=APP_PARAMS["icon"],
)

def remove():
    remove_ret = remove_duplicate(input_text)
    st.session_state[APP_PARAMS["right"]["key"]] = remove_ret


def find():
    find_ret = find_duplicate(input_text)
    st.session_state[APP_PARAMS["right"]["key"]] = find_ret


def clear():
    st.session_state[APP_PARAMS["left"]["key"]] = ""
    st.session_state[APP_PARAMS["right"]["key"]] = ""


if __name__ == "__main__":
    st.title(APP_PARAMS["title"])
    st.markdown(f'{APP_PARAMS["markdown"]["repository"]} {APP_PARAMS["markdown"]["visitor"]}')
    st.markdown(APP_PARAMS["markdown"]["description"])

    input_column, output_column = st.columns(2)
    remove_button, find_button, _,_,clear_button = st.columns([0.15,0.1,0.35,0.4,0.1])

    with input_column:
        input_text = st.text_area(
            label=APP_PARAMS["left"]["label"],
            height=APP_PARAMS["left"]["height"],
            key=APP_PARAMS["left"]["key"],
        )
    with output_column:
        output_text = st.text_area(
            label=APP_PARAMS["right"]["label"],
            height=APP_PARAMS["right"]["height"],
            key=APP_PARAMS["right"]["key"],
        )

    with remove_button:
        st.button(label=APP_PARAMS["button"]["remove"]["label"], on_click=remove)
    with find_button:
        st.button(label=APP_PARAMS["button"]["find"]["label"], on_click=find)
    with clear_button:
        st.button(label=APP_PARAMS["button"]["clear"]["label"], on_click=clear)
