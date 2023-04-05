import glob
import re
import copy
import sys
import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# chatbot
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain, ConversationChain
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferMemory
from langchain.utilities import PythonREPL
import openai


def query_database(db_path, query):
    
    try:
        with sqlite3.connect(path_to_db) as connection:

            cursor = connection.cursor()
            cursor.execute(query)

            rows = cursor.fetchall()[:20]   # limit response to 20 rows max
            columns = tuple([x[0] for x in cursor.description])
            
            return pd.DataFrame(rows, columns=columns)
    
    except:
        return '<query_failed>'


def get_schema(db_path):
    
    command = "PRAGMA table_info('salaries')"
    
    with sqlite3.connect(path_to_db) as connection:
        
        cursor = connection.cursor()
        cursor.execute(command)
        
        rows = [row[1:3] for row in cursor.fetchall()]
        # columns = ['column_name', 'data_type']
        
    return rows

generate_query_prompt = PromptTemplate(
    input_variables=['question'],
    template='''    
Context:
Your job is to write a sql query that answers the following question:
{question}

Below is a list of columns and their datatypes. Your query should only use the data contained in the table. The table name is `salaries`. Do not use columns that aren't in the table.
Columns:
[('fiscal_year', 'INTEGER'), ('payroll_number', 'REAL'), ('agency_name', 'TEXT'), ('last_name', 'TEXT'), ('first_name', 'TEXT'), ('mid_init', 'TEXT'), ('agency_start_date', 'TEXT'), ('work_location_borough', 'TEXT'), ('title_description', 'TEXT'), ('leave_status_as_of_june_30', 'TEXT'), ('base_salary', 'REAL'), ('pay_basis', 'TEXT'), ('regular_hours', 'REAL'), ('regular_gross_paid', 'REAL'), ('ot_hours', 'REAL'), ('total_ot_paid', 'REAL'), ('total_other_pay', 'REAL')]

If the question is not a question or is answerable, respond to the best of your ability.

Query:
'''
)

present_data_prompt = PromptTemplate(
    input_variables=['question', 'data'],
    template='''    
Context:
Your job is to present the following question and answer data in plain English as a summary. If the answer is <query_failed>, respond that you could not find the answer.
Use up to 5 sentences.

#########
EXAMPLES:
Question:
Who are the top 5 highest paid employees without duplicates??

Data: 
first_name    last_name  base_salary
0    GREGORY         RUSS   414707.000
1    RICHARD     CARRANZA   363346.000
2     MEISHA  ROSS PORTER   363346.000
3      DAVID        BANKS   363346.000
4    RICHARD     CARRANZA   352763.000
##########

Question:
{question}

data:
{data}

Summary:
'''
)

llm = ChatOpenAI(
    model_name='gpt-3.5-turbo', 
    temperature=0.,
    max_tokens=2048
)

generate_query = LLMChain(
    llm=llm, 
    prompt=generate_query_prompt,
    # memory=memory
)

present_data = LLMChain(
    llm=llm,
    prompt=present_data_prompt
)

path_to_db = Path.cwd() / 'data' / 'test.db'
schema = get_schema(path_to_db)

def answer_question(question, verbose=False):

    query = generate_query.run(question)
    query = query.split(';', 1)[0] + ';'   # only 1 query. Sometimes the model generates more than one.
    if verbose:
        print(query, '\n')

    data = query_database(path_to_db, query)
    if verbose:
        print(data, '\n')

    answer = present_data.run({'question': question, 'data': data})
    if verbose:
        print(answer, '\n')
        
    return answer

def language_model(prompt):
    return answer_question(prompt)