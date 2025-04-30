import sys

import dotenv
import streamlit as st

from camel.tasks import Task
from camel_ai_coding_workforce.agents import AGENT_CONFIGURATIONS
from camel_ai_coding_workforce.output import generate_task_tree, StreamlitStdout
from camel_ai_coding_workforce.workforce import (
    create_workforce,
    WORKFORCE_DESCRIPTION,
    DEFAULT_TASK,
)

dotenv.load_dotenv()

st.set_page_config(page_title="CAMEL-AI Coding Workforce", layout="wide")
st.title("🤖🤖 CAMEL-AI Coding Workforce")

task_prompt = st.text_area("Enter your TASK:", DEFAULT_TASK)
task = Task(content=task_prompt, id="0")

workforce = create_workforce(
    description=WORKFORCE_DESCRIPTION,
    agent_configurations=AGENT_CONFIGURATIONS,
)

if st.button("Run", icon="🚀"):

    st.info("Starting task processing...", icon="🔄")

    log_placeholder = st.empty()
    original_stdout = sys.stdout
    log_stream = StreamlitStdout("📜 Live Workforce Log", log_placeholder)
    sys.stdout = log_stream

    with st.spinner("🤖🤖 Running Workforce…"):
        task = workforce.process_task(task)

    sys.stdout = original_stdout
    log_placeholder.empty()

    st.success("Task processing completed", icon="🔥")

    st.subheader("🌳 Task Structure")

    st.markdown(generate_task_tree(task))

    st.subheader("✅ Final Task Result")
    st.markdown(task.result)

    st.subheader("📜 Full Workforce Log")
    st.code(log_stream.full_log, language="")
