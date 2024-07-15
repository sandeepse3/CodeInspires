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
    
    def get_relevant_documents(self, query: str):
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
    async def aget_relevant_documents(self, query: str):
        return []