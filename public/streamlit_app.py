"""
VitexBrain App
"""
from dotenv import load_dotenv
import uuid
import html

import streamlit as st

from lib.codegen_streamlit_lib import StreamlitLib
from lib.codegen_utilities import get_app_config
from lib.codegen_utilities import log_debug

DEBUG = True

app_config = get_app_config()
cgsl = StreamlitLib(app_config)


# UI elements


def add_title():
    """
    Add the title section to the page
    """

    # Emoji shortcodes
    # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

    with st.container():
        st.image("./assets/real-tor-logo-500.png", width=200)
        st.title(cgsl.get_title())


def add_assistant_html():
    """
    Add the WatsonX assistant HTML embedded code
    """
    # Reference:
    # Injecting JS?
    # https://discuss.streamlit.io/t/injecting-js/22651/5?u=carlos9
    # The following snippet could help you solve your cross-origin issue:
    div_id = uuid.uuid4()
    source = cgsl.get_par_value("ASSISTANT_JS")
    log_debug(f"Assistant HTML source: {source}", debug=DEBUG)
    st.markdown(f"""
<div style="display:none" id="{div_id}">
    <iframe src="javascript: \
        var script = document.createElement('script'); \
        script.type = 'text/javascript'; \
        script.text = {html.escape(repr(source))}; \
        var div = window.parent.document.getElementById('{div_id}'); \
        div.appendChild(script); \
        div.parentElement.parentElement.parentElement.style.display = 'none'; \
    "/>
</div>
    """, unsafe_allow_html=True)


def get_app_description():
    """
    Add the sidebar to the page
    """
    app_desc = cgsl.get_par_value("APP_DESCRIPTION")
    app_desc = app_desc.replace(
        "{app_name}",
        f"**{st.session_state.app_name}**")
    log_debug(f"App description: {app_desc}", debug=DEBUG)
    return app_desc


def add_sidebar():
    """
    Add the sidebar to the page
    """
    with st.sidebar:
        app_desc = get_app_description()
        st.sidebar.write(app_desc)
        # Data management
        cgsl.data_management_components()
        data_management_container = st.empty()
        # Show the conversations in the side bar
        cgsl.show_conversations()
    return data_management_container


def add_main_content():
    cols = st.columns(2)
    with st.container():
        app_desc = get_app_description()
        with cols[0]:
            st.write(app_desc)
    with st.container():
        with cols[0]:
            app_features = cgsl.get_par_value("APP_FEATURES")
            st.write(app_features)
    with st.container():
        with cols[0]:
            app_instructions = cgsl.get_par_value("APP_INSTRUCTIONS")
            st.write(app_instructions)


def add_check_buttons_pushed(
        containers: dict,
        question: str):
    """
    Check buttons pushed
    """
    pass


def add_footer():
    """
    Add the footer to the page
    """
    st.caption(f"© 2024 {st.session_state.maker_name}. All rights reserved.")


# Pages


def page_1():
    # Main content

    # Title
    add_title()

    # Sidebar
    # data_management_container = add_sidebar()
    # add_sidebar()

    # Main content
    add_main_content()

    # Assistant HTML
    add_assistant_html()

    # Check buttons pushed
    # add_check_buttons_pushed(
    #     {
    #         "result_container": result_container,
    #         "additional_result_container": additional_result_container,
    #         "data_management_container": data_management_container,
    #         "parameters_container": parameters_container,
    #     },
    #     question,
    # )

    # Footer
    with st.container():
        add_footer()


# Main


# Main function to render pages
def main():
    load_dotenv()

    st.session_state.app_name = cgsl.get_par_or_env("APP_NAME")
    st.session_state.app_version = cgsl.get_par_or_env("APP_VERSION")
    st.session_state.app_name_version = \
        f"{st.session_state.app_name} v{st.session_state.app_version}"
    st.session_state.maker_name = cgsl.get_par_or_env("MAKER_MAME")
    st.session_state.app_icon = cgsl.get_par_or_env("APP_ICON", ":sparkles:")

    # if "question" not in st.session_state:
    #     st.session_state.question = ""
    # if "prompt_enhancement_flag" not in st.session_state:
    #     st.session_state.prompt_enhancement_flag = False
    # if "use_response_as_prompt_flag" not in st.session_state:
    #     st.session_state.use_response_as_prompt_flag = False
    # if "conversations" not in st.session_state:
    #     cgsl.update_conversations()
    # if "question_label" not in st.session_state:
    #     get_question_label()
    # if "forms_config" not in st.session_state:
    #     st.session_state.forms_config = {}

    # Streamlit app code
    st.set_page_config(
        page_title=st.session_state.app_name_version,
        page_icon=st.session_state.app_icon,
        layout="wide",
        initial_sidebar_state="auto",
    )

    # Query params to handle navigation
    page = st.query_params.get("page", cgsl.get_par_value("DEFAULT_PAGE"))
    # Page navigation logic
    if not page or page == "home":
        page_1()


if __name__ == "__main__":
    main()
