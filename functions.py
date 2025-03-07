from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
import os
import yaml

with open('setting.yaml') as f:
    setting = yaml.load(f,Loader=yaml.FullLoader)

os.environ['HUGGINGFACEHUB_API_TOKEN'] = setting['huggingface_api_key']

llm = HuggingFaceEndpoint(
    repo_id=setting['repo_id'],
    task="text-generation",
    max_new_tokens=512,
    huggingfacehub_api_token = os.environ['HUGGINGFACEHUB_API_TOKEN']
)

template = """Question: {question}

Answer: """

prompt = PromptTemplate.from_template(template)

llm_chain = prompt | llm

def get_answer(user_input):
    return llm_chain.invoke({"question": user_input})
