from openai import OpenAI

client = OpenAI()

# Get Technical questions from a resume
def get_technical_questions(resume_text, job_description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''
                                                You are a technical lead at Klizo Solutions. 
                                                Based on the candidate's resume below, create a list of **10 challenging technical interview questions** 
                                                that assess the candidate's expertise in their field. Focus on areas of strength and any specialized skills mentioned.
                                                According to the job description - [{job_description}].
                                                '''},
            {"role":"assistant", "content": f"This is the Resume - [{resume_text}]."},
            {"role": "user", "content": "Provide me Technical questions on this resume in relation with job description. Do not add Preamble. Provide me the questions in Proper Structure"},
        ],
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        max_completion_tokens=2048
    )

    return response.choices[0].message.content