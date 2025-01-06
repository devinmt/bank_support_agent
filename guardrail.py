# guardrail.py
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

class GuardrailAgent:
    """
    Enhanced guardrail system for banking customer support.
    Ensures responses comply with banking regulations, policies, and best practices.
    """
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0.1  # Lower temperature for more consistent policy enforcement
        )
        
        self.prompt = PromptTemplate(
            template="""You are a banking compliance officer reviewing customer support responses.
            Review the following response carefully and ensure it meets ALL banking compliance and policy requirements:

            RESPONSE TO REVIEW:
            {response}

            Apply these mandatory checks:

            1. Regulatory Compliance:
            - No specific account numbers, balances, or personal information
            - Include necessary banking disclaimers where relevant
            - Compliance with banking secrecy laws
            - Clear distinction between financial advice vs information

            2. Security Protocols:
            - No request for sensitive information via unsafe channels
            - Clear authentication procedures when needed
            - Proper handling of suspected fraud cases
            - No sharing of internal banking procedures

            3. Customer Protection:
            - Clear fee and charge disclosures
            - Transparent terms and conditions
            - Fair lending practices
            - Clear escalation paths for complaints

            4. Communication Standards:
            - Professional and courteous tone
            - Clear and unambiguous language
            - No promises or guarantees unless authorized
            - Proper handling of time-sensitive matters

            5. Risk Management:
            - No unauthorized financial advice
            - Clear risk disclosures for products/services
            - Proper handling of transaction disputes
            - Clear limits of service/support scope

            If ANY violations are found, modify the response to comply while maintaining the core message.
            If compliant, return unchanged.

            COMPLIANT RESPONSE:""",
            input_variables=["response"]
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
        
    async def check_response(self, response: str) -> str:
        """
        Validate and modify response to ensure compliance with banking policies.
        
        Args:
            response (str): Original response to check
            
        Returns:
            str: Compliant response
        """
        try:
            # Pre-check for common sensitive patterns
            if any(term in response.lower() for term in [
                "account number",
                "pin",
                "password",
                "social security",
                "credit card number",
                "ssn"
            ]):
                response = "I apologize, but I cannot discuss sensitive account details in this channel. Please visit your local branch or use our secure online banking portal for such inquiries."
                return response
            
            # Apply comprehensive compliance check
            compliant_response = await self.chain.arun(response=response)
            
            # Post-check for required disclaimers
            if any(term in compliant_response.lower() for term in [
                "investment",
                "loan",
                "interest rate",
                "mortgage"
            ]) and "disclaimer" not in compliant_response.lower():
                compliant_response += "\n\nDisclaimer: This information is for general informational purposes only and should not be considered as financial advice. Please consult with a qualified financial advisor for personalized recommendations."
            
            return compliant_response
            
        except Exception as e:
            st.error(f"Guardrail check failed: {str(e)}")
            # Fallback to a safe, generic response
            return "I apologize, but I need to ensure my response meets all banking compliance requirements. Could you please rephrase your question?"

    def _contains_sensitive_info(self, text: str) -> bool:
        """Check for sensitive information patterns."""
        sensitive_patterns = [
            r'\b\d{16}\b',  # Credit card numbers
            r'\b\d{9}\b',   # SSN
            r'\b\d{8,}\b',  # Long number sequences
            r'\b[A-Z]{2}\d{6,}\b'  # Account number patterns
        ]
        
        import re
        return any(re.search(pattern, text) for pattern in sensitive_patterns)

