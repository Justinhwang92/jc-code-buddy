from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
  Elon Musk is the CEO of electric-vehicle maker Tesla, whose board he joined in 2004. During his nearly two decades there, the company has grown to be the global leader in EVs and world’s most valuable car company. Musk is also CEO and founder of SpaceX, and in 2022, he purchased Twitter for $44 billion. The entrepreneur, one of the world’s wealthiest people, has also launched other ventures including Neuralink, a brain-computer startup and Boring Co., a tunneling company. More recently he has incorporated a company called X.AI as part of efforts to steer development of artificial intelligence.
"""

if __name__ == "__main__":
    print("Hello, LangChain!")

    summary_template = """
      Given the information {information} about a person from I want you to create:
      1. a short summary
      2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
