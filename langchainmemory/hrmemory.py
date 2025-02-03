#from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory


# Create a memory object that stores, for instance, the last 3 messages.
memory = ConversationBufferWindowMemory(k=5, return_messages=True)

# Initialize the LLM model using LangChain’s ChatOpenAI.
# You can pass parameters similar to your OpenAI call (e.g., temperature, top_p, etc.)
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.5,
    max_tokens=2048
)

# Create the conversation chain with the LLM and memory.
conversation_chain = ConversationChain(llm=llm, memory=memory)


# Get Technical questions from a resume
def get_hr_questions(resume_text, job_description):
    # Construct a prompt that includes your instructions and the resume context.
    # This will be the new input for the chain.
    prompt = [
            {"role": "system", "content": f'''
                                            You are a human resources assistant expert for the company Klizo Solutions and
                                            You are an experienced HR professional at Klizo Solutions. 
                                            Based on the candidate's resume below, generate a list of **10 insightful HR interview questions** 
                                            that explore the candidate's fit for our company culture, work ethic, and soft skills and
                                            According to the job description - [{job_description}]. 
                                            '''},
            {"role":"assistant", "content": f"This is the Resume - [{resume_text}]."},
            {"role": "user", "content": "Provide me HR questions on this resume in relation with job description. Do not add Preamble. Provide me the questions in Proper Structure"},
        ]
    # Call the conversation chain.
    response = conversation_chain.predict(input=prompt)

    return response