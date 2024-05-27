from crewai import  Crew, Process
from agents import blog_researcher, blog_writer
# from tools import yt_tool
from tasks import research_task, writer_task
import streamlit as st


crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, writer_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

results = crew.kickoff(
    st.text_input(input = {'topic':'AI VS ML VS DL vs Data Science'}))
print(st.write(results))