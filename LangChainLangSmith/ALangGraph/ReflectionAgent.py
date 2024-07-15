from typing import List, Sequence

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph # MessageGraph is a type of graph that its state is simply a sequence of messages. And that is the new state.And in this graph, every node will receive as an input a list of messages. And the output for every node is going to be one message or maybe a couple of messages.

from chains import generate_chain, reflect_chain # Chains which are going to run in each node in our langGraph graph.

# Keys for LangGraph Nodes that we are going to create
REFLECT = "reflect"
GENERATE = "generate"


# It receives input the "State". State is simply the sequence of Messages
def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})


def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)] # There is a subtle difference which is super important here. The response we get back from the LLM, which usually would be with the role of the AI, then we now change it to be a human message. So we simply take the content of that message and we frame it with the role of a human, and then we need to return it. Because we want to trick the LLM to think that a human is sending this message. So that way we're going to have a conversation with the LLM back and forth, critique, generate, critique, generate.


builder = MessageGraph() # To store the state of the graph

# Nodes in the Graph
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)

# Drawing a Graph
builder.set_entry_point(GENERATE) # Sending the entry point Key to MessageGraph

# It's going to receive a state and it's going to return us the key of the node to execute.
def should_continue(state: List[BaseMessage]):
    # Now in this example we're not going to be leveraging an LLM to decide whether or not to finish or to go to another step
    if len(state) > 6:
        return END
    return REFLECT


builder.add_conditional_edges(GENERATE, should_continue) # Conditional Edge from GENERATE NODE -> REFLECT NODE
builder.add_edge(REFLECT, GENERATE) # REFLECT NODE -> GENERATE NODE

# We've built all the nodes and edges that we need for the graph, and now it's time to compile it, which will give us the final graph object that we can use and we can invoke.
graph = builder.compile()
print(graph.get_graph().draw_mermaid())
graph.get_graph().print_ascii()

if __name__ == "__main__":
    print("Hello LangGraph")
    inputs = HumanMessage(content="""Make this tweet better:"
                                    @LangChainAI
            — newly Tool Calling feature is seriously underrated.

            After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.

            Made a video covering their newest blog post

                                  """)
    response = graph.invoke(inputs)
    print(response)