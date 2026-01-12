from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.chatbot_with_tool import ChatbotWithToolNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphagenticai.nodes.chatbot_with_tool import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.This method createschatbot graph which includes chatbot node and tool node.sets up conditional edges between nodes and this function set as a entry point.
        """
        #define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        #define the LLM
        llm = self.llm

        #define chatbot node

        obj_chatbot_with_node = ChatbotWithToolNode(llm)

        chatbot_node = obj_chatbot_with_node.create_chatbot_with_tools(tools)


        #Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        #Add edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")

    def ai_news_builder_graph(self):
        """
        AI News Summarizer Graph Builder
        """
        ai_news_node = AINewsNode(self.llm)


        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_results)

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)



    def setup_graph(self,usecase:str):
        """
        sets up the graph for the selected use case.
        """
        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()

        if usecase == "AI News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()



        