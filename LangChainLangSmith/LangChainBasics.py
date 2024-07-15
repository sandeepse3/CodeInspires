# %%
# 1. LLMChain
# 2. SequentialChain
# 3.  ChatOpenAI 
# 4. ConversationBufferMemory 
# 4. FileChatMessageHistory
# 4. FileChatMessageHistoryVerbose
# 5. ConversationSummaryMemory
# 6. TextLoader
# 7. CharacterTextSplitter
# 8. OpenAIEmbeddings
# 9. Chroma
# 10. RetrievalQA Chain
# 11. CustomFilters (RedundantFilterRetriever.py)
# 12. RetrieverQARedundantFilter (This will import RedundantFilterRetriever class from RedundantFilterRetriever.py in CustomFilters)
# 13. Conversational Retrieval Chain (Pending) https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/learn/lecture/40261414#notes
# 14. Streaming and Different Calling Methods(__call__, invoke (almost same but one differnce), )
# 15. Streaming callback handler (https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/learn/lecture/40261464#notes)
# 16. Ollama basics
# *************************************************************************
# %%
            # TITLE: 1. LLMChain
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import argparse
from dotenv import load_dotenv
load_dotenv()
# Note: This will cause an error (if you run it in Jupyter notebook or VSCode Interactive Notebook without these command-line arguments) because argparse expects these arguments to be passed in from the command line.
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# %%
# Language Model
model = OpenAI()

# Input
code_prompt = PromptTemplate(
    input_variables=["task","language"],
    template="Write a very short {language} function that will {task}."
)

# Chain
code_chain = code_prompt | model

# Chain Object that takes inputs 
result = code_chain.invoke({
    "task": args.task,
    "language": args.language
})

print(result)
# *************************************************************************
            # TITLE: 2 SequentialChain (Using LCEL)
# %%
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableAssign
import argparse
from dotenv import load_dotenv
# %%
load_dotenv()

# Note: This will cause an error (if you run it in Jupyter notebook or VSCode Interactive Notebook without these command-line arguments) because argparse expects these arguments to be passed in from the command line.
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# %%
# Chain A: Code Chain
# OpenAI Function that does http request on the OpenAI server
model = OpenAI()

# Input
code_prompt = PromptTemplate(
    input_variables=["task","language"],
    template="Write a very short {language} function that will {task}."
)

# Chain A
# Define a lambda to combine the outputs into the desired format
def combine_results(input):
    print(f">>>>> GENERATED CODE  <<<<<<{input}\n")
    return {"code": input, "language": args.language}

code_chain = code_prompt | model | RunnableLambda(combine_results)

# Chain B: Test Chain
test_prompt = PromptTemplate(
    input_variables=["language","code"],
    template="Write a test for the following code:\n{code} in {language}"
)
test_chain = test_prompt | model

# Chaining Chain A and Chain B in a Sequential manner
seqChain = code_chain | test_chain
result = seqChain.invoke({
    "task": args.task,
    "language": args.language
})

# Chaining Chain A and Chain B in a Sequential manner
# from langchain.chains import LLMChain,SequentialChain
# chain = SequentialChain(
#     chains = [code_chain,test_chain],
#     input_variables = ["task","language"],
#     output_variables = ["code","test"]
# )

print(f">>>>> GENERATED TEST  <<<<<<{result}\n")
# *************************************************************************
            # TITLE: 2 SequentialChain (Using LCEL 2nd Method)
# %%
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableAssign
import argparse
from dotenv import load_dotenv
# %%
load_dotenv()

# Note: This will cause an error (if you run it in Jupyter notebook or VSCode Interactive Notebook without these command-line arguments) because argparse expects these arguments to be passed in from the command line.
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# %%
# Chain A: Code Chain
# OpenAI Function that does http request on the OpenAI server
model = OpenAI()

# Input
code_prompt = PromptTemplate(
    input_variables=["task","language"],
    template="Write a very short {language} function that will {task}."
)

# The reason you can't directly write "language": args.language in this context is because the RunnableParallel expects a callable or Runnable object for each key-value pair in the dictionary. When you provide "language": args.language, you are directly assigning the value of args.language to the key "language", which is a string. This is not a callable or Runnable object, which causes the error.
# code_chain = code_prompt | model | RunnableParallel({
#     "code": RunnablePassthrough(),
#     "language": args.language
# })

code_chain = code_prompt | model | RunnableParallel({
    "code": RunnablePassthrough(),
    "language": lambda language=args.language: language
})


# Chain B: Test Chain
test_prompt = PromptTemplate(
    input_variables=["language","code"],
    template="Write a test for the following code:\n{code} in {language}"
)
test_chain = test_prompt | model

# Chaining Chain A and Chain B in a Sequential manner
seqChain = code_chain | test_chain
result = seqChain.invoke({
    "task": args.task,
    "language": args.language
})

print(f">>>>> GENERATED TEST  <<<<<<{result}\n")
# *************************************************************************
            # TITLE: 2 SequentialChain (Using LCEL 3rd Method)
# %%
load_dotenv()

# Note: This will cause an error (if you run it in Jupyter notebook or VSCode Interactive Notebook without these command-line arguments) because argparse expects these arguments to be passed in from the command line.
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# %%
# Chain A: Code Chain
# OpenAI Function that does http request on the OpenAI server
model = OpenAI()

# Input
code_prompt = PromptTemplate(
    input_variables=["task","language"],
    template="Write a very short {language} function that will {task}."
)

# Chain A
# Define a lambda to combine the outputs into the desired format
def combine_results(input):
    return {"code": input, "language": args.language}

# Chain A
code_chain = code_prompt | model | RunnableLambda(combine_results)

# Chain B: Test Chain
test_prompt = PromptTemplate(
    input_variables=["language","code"],
    template="Write a test for the following code:\n{code} in {language}"
)

# test_chain = test_prompt | model | RunnableParallel({"test": RunnablePassthrough()})
test_chain = test_prompt | model

# Chaining Chain A and Chain B in a Sequential manner
result = code_chain.invoke({
    "task": args.task,
    "language": args.language
})
print(f">>>>> GENERATED CODE  <<<<<<{result['code']}\n")
# tresult = test_chain.invoke(result)
# print(f">>>>> GENERATED TEST  <<<<<<\n{tresult['test']}")
print(f">>>>> GENERATED TEST  <<<<<<{test_chain.invoke(result)}\n")
# *************************************************************************
            # TITLE: 3 ChatOpenAI 
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableAssign
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# %%
load_dotenv()

# Chain A: Code Chain
# OpenAI Function that does http request on the OpenAI server
chatmodel = ChatOpenAI()
# ChatOpenAI(model_name="gpt-3.5-turbo") # Default it uses gpt-3.5-turbo
# chatllm = ChatOpenAI(model_name="gpt-4") # Works only when paid 

# Input
prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages = [
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

output_parser = StrOutputParser() # Output without extras

# Chain
chain = prompt | chatmodel | output_parser

while True:
    content = input('>>> User Message: ')
    if content == 'break':
        break
    else:
        result = chain.invoke(
            {
            "content": content
        }
    )
    print(f">>> AI Message: {result}")
# *************************************************************************
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

# *************************************************************************
            # TITLE: 4 ConversationBufferMemory (Using LLMChain)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI()

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), 
        # so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# ConversationBufferMemory can store a history but it can't store history in a 'file', so if you exit the
# program everything that is stored in RAM is lost, but FileChatMessageHistory stores in a json file.
memory = ConversationBufferMemory(memory_key="messages",return_messages=True)

# Chain takes Input and LLM
chain = LLMChain(
    llm=chatmodel,
    prompt=prompt,
    memory=memory
)

while True:
    content = input(">> ")
    if content=='break':
        break
    else:
        result = chain({"content":content})
        # Output
        print(result['text'])
# *************************************************************************
            # TITLE: 4 FileChatMessageHistory (Using LCEL)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI()

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # It will specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# FileChatMessageHistory is a Class
# ConversationBufferMemory can't store history in a file but FileChatMessageHistory does. Even if you exit the program all the history will be restored
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True)

# Output parser
output_parser = StrOutputParser() # Output without extras

# Type break or Ctrl + C to interrupt the loop
while True:
    content = input(">> ")
    if content=='break':
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
# *************************************************************************
            # TITLE: 4 FileChatMessageHistory (Using LLMChain)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI()

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # It will specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# FileChatMessageHistory is a Class
# ConversationBufferMemory can't store history in a file but FileChatMessageHistory does. Even if you exit the program all the history will be restored
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True)

# Chain takes Input and LLM
chain = LLMChain(
    llm=chatmodel,
    prompt=prompt,
    memory=memory
)

# Type break or Ctrl + C to interrupt the loop
while True:
    content = input(">> ")
    if content=='break':
        break
    else:
        result = chain({"content":content})
        # Output
        print(result['text'])
# *************************************************************************
            # TITLE: 4 FileChatMessageHistoryVerbose (Using LLMChain)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI(verbose=True)

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # It will specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# FileChatMessageHistory is a Class
# ConversationBufferMemory can't store history in a file but FileChatMessageHistory does. Even if you exit the program all the history will be restored
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True)

# Chain takes Input and LLM
chain = LLMChain(
    llm=chatmodel,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# Ctrl + C to interrupt the loop
while True:
    content = input(">> ")
    if content=='break':
        break
    else:
        result = chain({"content":content})
        # Output
        print(result['text'])
# *************************************************************************
            # TITLE: 5 ConversationSummaryMemory (Using LCEL)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI() # verbose=True (optional)

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # It will specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# 'System' key is automatically added and passes the Summary prompt of 'FileChatMessageHistory' to the LLM defined in ConversationSummaryMemory Class 
memory = ConversationSummaryMemory(
    llm=chatmodel, # You can pass any summarization LLM, need not necessarily same LLM that you are using for final response
    memory_key="messages",
    return_messages=True)

# Output parser
output_parser = StrOutputParser() # Output without extras

# Ctrl + C to interrupt the loop
while True:
    content = input(">> ")
    if content=='break':
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

# *************************************************************************
            # TITLE: 5 ConversationSummaryMemory (Using LLMChain)
# %%
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv
# %%
load_dotenv()

# LLM / Interface
chatmodel = ChatOpenAI(verbose=True) # verbose=True (optional)

# Input
prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages= [
        # It will specifically look for 'messages' key in the modified input (i.e., with added 'messages' key), so that memory placeholder can expand the messages key value in such a way that LLM can easily understand
        MessagesPlaceholder(variable_name="messages"), # Can be any key name, need not necessarily be messages
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# New key called 'messages' will be inserted with every input
# 'System' key is automatically added and passes the Summary prompt of 'FileChatMessageHistory' to the LLM defined in ConversationSummaryMemory Class 
memory = ConversationSummaryMemory(
    llm=chatmodel, # You can pass any summarization LLM, need not necessarily same LLM that you are using for final response
    memory_key="messages",
    return_messages=True)

# Chain takes Input and LLM
chain = LLMChain(
    llm=chatmodel,
    prompt=prompt,
    memory=memory,
    verbose=True # verbose=True optional
)

# Ctrl + C to interrupt the loop
while True:
    content = input(">> ")
    if content=='break':
        break
    else:
        result = chain({"content":content})
        # Output
        print(result['text'])
    
# *************************************************************************
            # TITLE: 6 TextLoader
# %%
from langchain.document_loaders import TextLoader
from dotenv import load_dotenv
# %%
load_dotenv()

loader = TextLoader("facts.txt")
docs = loader.load()
# docs = TextLoader("facts.txt").load()
print(docs)
# %%

# *************************************************************************
            # TITLE: 7. CharacterTextSplitter
# %%
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
# %%
load_dotenv()

# Loader and Splitter
loader = TextLoader("facts.txt")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

docs = loader.load_and_split(
    text_splitter=text_splitter
)

for doc in docs:
    print(doc.page_content)
    print()
# *************************************************************************
            # TITLE: 8. OpenAIEmbeddings
# %%
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
# %%
load_dotenv()

#  Embeddings. Embed the chunks using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
embeds = embeddings.embed_query("Hi There")
print(embeds)
# ****************************************************************************
            # TITLE: 9. RetrievalQA Chain (1st Part - Storing Data to Chroma)
# %%
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma 
from dotenv import load_dotenv
# %%
load_dotenv()

#  Embeddings. Embed the chunks using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Loader and Splitter
loader = TextLoader("facts.txt")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

docs = loader.load_and_split(
    text_splitter=text_splitter
)
 
# Creating an instance of Chromadb
# All chunks will be converted to embeddings in a single request and stored in a vector store
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)
#  similarity_search_with_score it gives scores
results = db.similarity_search_with_score("What is an interesting fact about the English language?",
                                          k=5) # k = Return Top N results
for result in results:
    print()
    print(f'Similarity Search Score: {result[1]}') # Less Score means less Distance means More Similarity
    print(result[0].page_content)
# *************************************************************************
            # TITLE: 10. RetrievalQA Chain (2nd Part - Retrieval)
# %%
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
# %%
load_dotenv()
#  Embeddings. Embed the chunks using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Location of the Vector Store and Embedding that it needs to use for Retrevial
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

# Retriever
# A Retriever is an object that can take in a string and return some relevant documents.
# To be a "Retriever", the object must have a method called "get_relevant_documents" that takes a string and returns a list of documents.
# Look up (it'not just passive look up it's finding a similarity) Query against the Vector Store for Similar results. We call it as Retriever or RetrieverQA to be specific
# It's Modular. You can you any retriever that might have slightly different functions to find documents
retriever = db.as_retriever()

# which LLM to use by Chain
chatmodel = ChatOpenAI()

# RetrievalQA Chain: LangChain has a tool that basically wraps up this entire flow. It's going to take in our vector store. It's going to encode or generate some embeddings for an incoming user question or a query. Find some relevant documents, inject / 'stuff' them into a system message prompt template, take the user's question and put it into human message prompt template, and then feed the entire thing into an LLM Chain for us. This construct is called a retrieval chain, or in the source code it's called really just a retrieval.
chain = RetrievalQA.from_chain_type(
    llm=chatmodel,
    retriever=retriever,
    chain_type="stuff"
)

# We will pass the input to the retriever here in the chain because always chain takes the input and re-routes the input to the retriever.
result = chain.invoke("What is an interesting fact about the English language?")
print(result['result'])

# The main problem with above code is it doesn't remove any duplicate records.
# *************************************************************************
            # TITLE: 11. CustomFilters (RedundantFilterRetriever.py)
# %%
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import BaseRetriever
# %%
# Because EmbeddingsRedundantFilter has some disadvantages (It doesn't have a slot to connect to db and use already claculated embeddings for duplicate removal), so we are using customFilterRetriever to do those two tasks.

# Custom Filter Retriever does two things 1. To get relevant documents 2. To remove any duplicate records
# class CustomFilterRetriever:
#     def get_relevant_documents(self, query: str):
#         # Code to use Chroma to get the relevant documents
#         # and remove any duplicate records

# RedundantFilterRetriever class is going to extend a base class of base retriever (BaseRetriever). This base class has some basic functionality inside of it that kind of defines what a retriever is and how it behaves.
# Our custom retriever must do two things.
# 1. Our function in our class must define that get relevant documents method (after input Query gets embeded). It must take in a string and then return a list of (relevant) documents.
# 2. Custom retriever must define an asynchronous function (even if doesn't do anything)

class RedundantFilterRetriever(BaseRetriever):
    # So now whenever someone tries to create an instance of this class, they must provide an two objects (embeddings of type 'Embeddings' and chroma of type 'Chroma') that can be used to calculate embeddings.
    # Defining Objects
    embeddings:OpenAIEmbeddings
    db:Chroma
    
    def get_relevant_documents(self, query):
        # calculate embeddings for the 'query' string
        # Convert query to embeddings
        emb = self.embeddings.embed_query(query)
       
        # take embeddings and feed them into that max_marginal_relevance_search_by_vector
        # Code to use Chroma to get the relevant documents and remove any duplicate records
        return self.db.max_marginal_relevance_search_by_vector(
            embedding = emb,
            lambda_mult=0.8 # 0 to 1. Higher values allow for similar docs
        )
    
    # Even if I remove below async code, everything is working fine but need more verfication (I checked only at high level)
    # The other requirement of a custom retriever is, it must define an asynchronous function called aget_relevant_documents, and this is if you are using async Python, which we are not currently doing. Regardless, we are using it or not still we are required to define it. Our implementation of this function is just going to be empty, because we're only going to worry about the synchronous case.
    async def aget_relevant_documents(self):
        return []
# *************************************************************************
            # TITLE: 12. RetrieverQARedundantFilter
# %%
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from CustomFilters.RedundantFilterRetriever import RedundantFilterRetriever
# from Folder.File import Class
from dotenv import load_dotenv
# import langchain
# 
# langchain.debug = True # to Turn ON Debugging Mode
# %%
load_dotenv()

#  Embeddings. Embed the chunks using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Location of the Vector Store and Embedding that it needs to use for Retrevial
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

# Retriever
# A Retriever is an object that can take in a string and return some relevant documents.
# To be a "Retriever", the object must have a method called "get_relevant_documents" that takes a string and returns a list of documents.
# Look up (it'not just passive look up it's finding a similarity) Query against the Vector Store for Similar results. We call it as Retriever or RetrieverQA to be specific
# It's Modular. You can you any retriever that might have slightly different functions to find documents
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
    )

# Which LLM to use by Chain
chatmodel = ChatOpenAI()

# RetrievalQA Chain: LangChain has a tool that basically wraps up this entire flow. It's going to take in our vector store. It's going to encode or generate some embeddings for an incoming user question or a query. Find some relevant documents, inject / 'stuff' them into a system message prompt template, take the user's question and put it into human message prompt template, and then feed the entire thing into an LLM Chain for us. This construct is called a retrieval chain, or in the source code it's called really just a retrieval.
chain = RetrievalQA.from_chain_type(
    llm=chatmodel,
    retriever=retriever,
    chain_type="stuff"
)

# We will pass the input to the retriever here in the chain because always chain takes the input and re-routes the input to the retriever.
result = chain.run("What is an interesting fact about the English language?") # chain.run gives string in 'result' key as output
# result = chain("What is an interesting fact about the English language?")  # chain gives dictionary as output
print(result)
# *************************************************************************
            # TITLE: 16. Ollama basics
from langchain_community.llms import Ollama

# Initialize Ollama with the model "llama3"
llm = Ollama(model="llama3",temperature=0.9)

# response = llm.invoke("what is stop=['<|eot_id|>'] in langchain?")
# print(response)

# Define your query
query = "what is stop=['<|eot_id|>'] in langchain?"

# print(llm.invoke(query, stop=['<|eot_id|>'], max_tokens=160))

# Stream the answer
for chunks in llm.stream(query, stop=['<|eot_id|>'], max_tokens=160):
    print(chunks, end="")