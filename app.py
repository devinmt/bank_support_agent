# app.py
import streamlit as st
from typing import List, Tuple
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from engine import RAGEngine
import asyncio

class GuardrailAgent:
    """
    Banking compliance guardrail system
    """
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0.1
        )
        
        self.prompt = PromptTemplate(
            template="""You are a banking compliance officer. Review this customer support response:

            RESPONSE TO REVIEW:
            {response}

            Ensure it meets these requirements:
            1. No sensitive information (account numbers, PINs, etc.)
            2. Professional and courteous tone
            3. Clear disclaimers where needed
            4. Accurate financial information
            5. Proper handling of banking queries

            Modify if needed or return unchanged.

            COMPLIANT RESPONSE:""",
            input_variables=["response"]
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    async def check_response(self, response: str) -> str:
        """Run compliance check on response"""
        try:
            result = await self.chain.arun(response=response)
            return result
        except Exception as e:
            st.error(f"Guardrail error: {str(e)}")
            return response

class BankSupportApp:
    def __init__(self):
        self.rag_engine = RAGEngine()
        self.rag_engine.refresh_index()
        self.guardrail = GuardrailAgent()
    
    async def process_message(self, message: str, history: List[Tuple[str, bool]]) -> Tuple[str, List[str]]:
        """Process user message and return response"""
        try:
            # Prepare message with history
            msg_list = history.copy()
            msg_list.append((message, True))
            
            # Get RAG response
            with st.spinner('Getting response...'):
                response, sources = await self.rag_engine.process_query(msg_list)
            
            # Apply compliance check
            with st.spinner('Checking compliance...'):
                response = await self.guardrail.check_response(response)
            
            return response, sources
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return "I apologize, but I encountered an error. Please try again.", []

async def main():
    # Page configuration
    st.set_page_config(
        page_title="Bank Customer Support",
        page_icon="🏦",
        layout="wide"
    )
    
    # Title and description
    st.title("🏦 Bank Customer Support")
    st.markdown("""
    Welcome! How can I assist you with your banking queries today?
    """)
    
    # Initialize app state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    if 'support_app' not in st.session_state:
        st.session_state.support_app = BankSupportApp()
    
    # Sidebar controls
    with st.sidebar:
        st.header("Options")
        if st.button('Clear Chat'):
            st.session_state.chat_history = []
            st.rerun()
    
    # Display chat history
    for msg, is_user in st.session_state.chat_history:
        with st.chat_message("user" if is_user else "assistant"):
            st.write(msg)
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Show user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get and show response
        response, sources = await st.session_state.support_app.process_message(
            prompt,
            st.session_state.chat_history
        )
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)
            if sources:
                st.markdown("**Sources:**")
                for source in sources:
                    st.markdown(f"- {source}")
        
        # Update chat history
        st.session_state.chat_history.append((prompt, True))
        st.session_state.chat_history.append((response, False))
        
        # Refresh display
        st.rerun()

if __name__ == "__main__":
    asyncio.run(main())