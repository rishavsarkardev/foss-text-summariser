import os
import warnings
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from .prompt_template_strings import prompt_template_string, refined_prompt_template_string, final_refined_prompt_template_string

warnings.filterwarnings("ignore")


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
env_path = os.path.join(parent_dir, ".env")
load_dotenv(dotenv_path=env_path)


summary_gen_pipeline = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
parser = StrOutputParser()

PROMPT = PromptTemplate(template=prompt_template_string, input_variables=['text'])
initial_chain = PROMPT | summary_gen_pipeline | parser

REFINED_PROMPT = PromptTemplate(template=refined_prompt_template_string, input_variables=['text', 'word_limit', 'existing_summary'])
refined_chain = REFINED_PROMPT | summary_gen_pipeline | parser

FINAL_REFINED_PROMPT = PromptTemplate(template=final_refined_prompt_template_string, input_variables=['text', 'word_limit', 'existing_summary'])
final_refined_chain = FINAL_REFINED_PROMPT | summary_gen_pipeline | parser



def text_to_chunk_convert(text):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-4o-mini",
        chunk_size=2500,
        chunk_overlap=200
    )

    return text_splitter.split_text(text)


def create_summary(text_chunks, word_limit):
    final_summary = ""

    for i, chunk in enumerate(text_chunks):
        if i == 0:
            final_summary = initial_chain.invoke({'text': chunk})
        elif i < len(text_chunks)-1:
            final_summary = refined_chain.invoke({'text': chunk, 'existing_summary': final_summary})
        elif i == len(text_chunks)-1:
            final_summary = final_refined_chain.invoke({'text': chunk, 'existing_summary': final_summary, 'word_limit': word_limit})

    
    return final_summary
