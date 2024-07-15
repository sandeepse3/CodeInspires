# TITLE: 4 ConversationBufferMemory (Using LCEL)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI()

# Input
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        # specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), 
        # so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Memory
memory = ConversationBufferMemory(memory_key="messages", return_messages=True)

# Output parser
output_parser = StrOutputParser() # Output without extras

# It's not working
# chain = (
#     RunnablePassthrough.assign(
#         messages=RunnableLambda(memory.load_memory_variables)
#     )
#     | prompt
#     | chatmodel
# )

# Type break or Ctrl + C to interrupt the loop
while True:
    content = input('>>> User Message: ')
    if content == 'break':
        break
    else:
        # Retrieve messages from memory
        messages = memory.load_memory_variables({}).get("messages", [])

        # Run the chain with current input and memory
        input_data = {
            "content": content,
            "messages": messages
        }
        chain = prompt | chatmodel | output_parser
        ai_response = chain.invoke(input_data)


        # Update memory with new interaction
        memory.save_context(input_data, {"response": ai_response})

        print(f">>> AI Message: {ai_response}")
