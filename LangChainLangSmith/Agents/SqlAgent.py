# main.py
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.agents import OpenAIFunctionsAgent,AgentExecutor
from tools.sql import run_query_tool, tables_str, describe_tables_tool
from tools.report import write_report_tool
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from dotenv import load_dotenv
# import langchain

# langchain.debug = True
load_dotenv()
chat = ChatOpenAI()
tables = tables_str()
# memory_key is chat_history. And remember, we also need to add in that other keyword argument of return_messages true. And we're putting that in to make sure that the memory is going to return a list of memory objects. So when it says return_messages=True, it means return or give us back the list of messages as message objects as opposed to a bunch of strings. We would use that list of strings if we were using a completion-based language model (say if we set return_messages=False). And we aren't, we are using ChatGPT here, which is message/chat-based.  
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content="You are an AI that has access to a SQLite database.\n"
            f"The database has tables of: {tables}\n"
            "Do not make any assumptions about what tables exist "
            "or what columns exist. Instead, use the 'describe_tables' function"), # It's a Static Message so no need to use System Message Prompt Template
        # We need to add in a MessagesPlaceholder for the chat_history as well. So this is going to be the thing that tries to find the stored list of messages (with variable_name=chat_history) and it's gonna kind of explode and convert into all the previous messages that were exchanged. So we'll put in another MessagesPlaceholder with a variable name of chat_history.
        # And I'm putting it right here specifically because I want to add it before any brand new human message that we add in.
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") # Remember, the goal of MessagesPlaceholder is to kind of take in an input variable and then explode or expand into a new list of messages. Agent Scratch Pad is exactly same as MessagesPlaceholder(variable_name="messages") in ConversationSummaryMemory (LangChainBasics.py).
    ]
    )

tools = [run_query_tool, describe_tables_tool, write_report_tool]
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools = tools
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    # To use the ConversationBufferMemory as this Memory object that we just created, we're going to add it into our agent executor because that is the thing that needs to remember this list of messages. 
    memory=memory
)

if __name__ == "__main__":
    agent_executor(
        "How many users are there?"
        # "How many orders are there? Write the result to an html report."
    )

# # This is going to use ConversationBufferMemory and repeat the process.
# agent_executor(
#     "Repeat the exact same process for users."
# )
