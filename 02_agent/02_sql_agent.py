from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType


llm = Ollama(model="llama3:8b", temperature=0.8)
db = SQLDatabase.from_uri("sqlite:///SupportCenter.db")

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

response = agent_executor.invoke("Which agent is working on the ticket?")
print(response)
