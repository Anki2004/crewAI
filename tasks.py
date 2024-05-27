from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task= Task(
    description = (
        "Identify the video {topic}."
        "get detailed info about the video from the channel."
    ),
    expected_ouput = 'A comprehensive 2 para long report based on the {topic} of the video',
    tools = [yt_tool],
    agent = blog_researcher,

)
write_task = Task(
    description = (
        "Write a blog post about the video {topic}."
    ),
    expected_ouput = 'A blog post about the {topic} of the video',
    tools = [yt_tool],
    agent = blog_writer,
    async_excution = False,
    output_file = 'new-blog-post.md'
)