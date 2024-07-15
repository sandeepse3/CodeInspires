# %%
# REFERENCES: https://youtu.be/3Gcm27l-uyQ?si=rMWHECwauzrl1pzl
# *************************************************************************
            # TITLE: 2 SequentialChain (Using LCEL)

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel, RunnableAssign
import argparse
import os
from dotenv import load_dotenv
# %%
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
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

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant. Please resposne to the user request only based on the given context"),
#         ("user","Question:{question}\nContext:{context}")
#     ]
# )
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