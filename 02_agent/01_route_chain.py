# route logic based on input using llm

from langchain_community.llms import Ollama
from langchain.chains.router import MultiPromptChain

# initate prompt
HARDWARE_ISSUE_TEMPLATE = """
I'm an agent from customer service, I can help to answer all the hardware related questions.
The question is:
{input}
"""
PAYMENT_ISSUE_TEMPLATE = """
I'm an agent from customer service, I can help to answer all the payment related questions.
The question is:
{input}
"""

prompt_infos = [
    {
        "name": "hardware_issue",
        "description": "Answer all the hardware related questions",
        "prompt_template": HARDWARE_ISSUE_TEMPLATE,
    },
    {
        "name": "payment_issue",
        "description": "Answer all the payment related questions",
        "prompt_template": PAYMENT_ISSUE_TEMPLATE,
    },
]

# initate llm model
llm = Ollama(model="llama3:8b", temperature=0.8)

# initate rounter chain
chain = MultiPromptChain.from_prompts(
    llm=llm,
    prompt_infos=prompt_infos,
    verbose=True,
)

# tests
print(chain.invoke({"input": "How to increase RAM of my PC?"}))
print(chain.invoke({"input": "How to increase my credit limit my Chase credit card?"}))
print(chain.invoke({"input": "How to fix my MAC network issue?"}))
