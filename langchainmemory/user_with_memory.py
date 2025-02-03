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
def get_user_questions(resume_text, job_description, input_question):
    if input_question == "":
        return "Please provide a question to generate questions."
    else:
        # Construct a prompt that includes your instructions and the resume context.
        # This will be the new input for the chain.
        prompt = [
            {"role": "system", "content": f'''
                                            You are a interviewer at Klizo Solutions. 
                                            How is highly skilled at their job and has a lot of experience in the field.
                                            This is the job description - [{job_description}].
                                            '''},
            {"role": "assistant", "content": f"This is the Resume - [{resume_text}]."},
            {"role": "user", "content": f'''According of the 'job description' and 'Resume' provide me a list of question on this topic - {input_question}. 
                                        Provide New unique questions Everytime. Do not add Preamble. Provide me the questions in Proper Structure'''}
        ]
        # Call the conversation chain.
        response = conversation_chain.predict(input=prompt)

        return response