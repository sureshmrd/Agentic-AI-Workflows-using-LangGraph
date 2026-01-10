from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    def __init__(self,model):
        self.llm = model

    def create_chatbot_with_tools(self,tools):
        """
        returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """
            Actual Chatbot Logic Node takes state input and returns llm response
            """
            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
