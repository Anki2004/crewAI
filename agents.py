from crewai import Agent
from tools import yt_tool


import os
os.environ["OPEN_API_KEY"] = os.getenv("OPEN_AI_KEY")
# pass your api key below 
os.environ["OPENAI_MODEL_NAME"] = " "

blog_researcher = Agent(
    role = 'Blog researcher from youtube videos',
    goal = 'get the relevant video content for the topic{topic} from the YT channel',
    verbose = True,
    memory = True,
    backstory = (
        "expertisse in understanding videos in AI Data Science, Machine Learning and Gen AI"
    ),
    tools = [yt_tool],
    allow_delegations = True,

)

## creating a senior blog writer
blog_writer = Agent(
    role = 'writer',
    goal = 'Narate compilling tech stories about the video {topic}',
    verbose = True,
    memory = True,
    backstory = (
        "expertisse in writing tech stories about AI Data Science, Machine Learning and Gen AI"
    ),
    tools = [yt_tool],
    allow_delegation = False
)
