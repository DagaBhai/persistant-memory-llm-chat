# all the helper function of gemini will be here

def get_gemini_response(prompt, system_instructions):
    """
    use google.genai to send the prompt and system instructions to get the response from gemini
    args:
        prompt: The prompt to send to gemini.
        system_instructions: The system instructions to send to gemini.
    returns:
        The response from gemini.(In json format)
    """
    return 1

def create_session_name(session_chat):
    """
    use gemini to create a session name for the given session chat
    args:
        session_chat: The chat history of the session to create a session name for.
    """
    return 1

def create_embeddings(chunk, dimentions):
    """
    use gemini embeddings model to create embeddings for the given chunk of text and return the embeddings
    use 768 dimensions
    """
    return 1

