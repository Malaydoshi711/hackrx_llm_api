from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt_template = PromptTemplate.from_template("""
You are an insurance policy expert. Based on the query and document excerpts, give:
- Decision: Approved or Rejected
- Amount: Estimate payout if applicable
- Justification: Refer to exact policy clauses

Return JSON like:
{{
  "decision": "Approved",
  "amount": "Rs. 1,00,000",
  "justification": "Clause 3.2 allows..."
}}

Query: {question}
Excerpts:
{context}
""")

def query_llm(question, context):
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run({"question": question, "context": "\n".join(context)})
