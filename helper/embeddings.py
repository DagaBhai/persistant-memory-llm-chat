#Contains helper functions to create and manage embeddings for the documents and chat sessions.
#
#

def get_context(query, top_k):
    """
    Search `query` in the vector database and return the top `top_k` most relevant documents as context for the chat session.
    args:
        query: The query to search in the vector database.
        top_k: The number of most relevant documents to return as context.
    returns:
        A list of the top `top_k` most relevant documents as context for the chat session.

    example:
        context = get_context("What is the capital of France?", 5)
        print(context)
        >>> ["The capital of France is Paris.", "Paris is the capital city of France.", 
        "France's capital is Paris.", "The city of Paris is the capital of France.", 
        "Paris, the capital of France, is known for its art and culture."]
    """
    return 1

