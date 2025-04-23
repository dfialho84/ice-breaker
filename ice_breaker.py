from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

information = """
    With over 18 years of experience in software development, I am a full-stack engineer specializing in building scalable and robust applications. My expertise ranges from architecting microservices with Java and Spring Boot on the backend to developing dynamic and responsive interfaces with React and Vue.js on the frontend. I am passionate about best practices such as BDD and TDD, ensuring software quality and reliability.

    I have worked on strategic projects at the Federal University of Viçosa, where I developed customized management and learning systems and led multidisciplinary teams. I have significant experience in databases, infrastructure with Docker and CI/CD, and cloud computing, with an ongoing AWS certification. My career also includes managing IT support teams and governance, improving efficiency, and organizational processes.

    I am driven by the challenge of transforming complex problems into efficient and scalable solutions, always seeking innovation and continuous improvement. I am open to new opportunities where I can apply my expertise and contribute to technological growth.
"""

if __name__ == '__main__':
    load_dotenv()
    # print(os.environ.get("OPENAI_API_KEY"))
    print(os.environ.get("LANGCHAIN_TRACING_V2"))
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )
    # llm = ChatOpenAI(
    #     model_name="gpt-3.5-turbo",
    #     temperature=0,
    # )
    # llm = ChatOllama(model="llama3",)
    llm = ChatOllama(model="mistral",)
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})
    print(res)