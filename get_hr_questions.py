from openai import OpenAI

client = OpenAI()

# Get HR questions from a resume
def get_hr_questions(resume_text, job_description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f'''
                                            You are a human resources assistant expert for the company Klizo Solutions and
                                            You are an experienced HR professional at Klizo Solutions. 
                                            Based on the candidate's resume below, generate a list of **10 insightful HR interview questions** 
                                            that explore the candidate's fit for our company culture, work ethic, and soft skills and
                                            According to the job description - [{job_description}]. 
                                            '''},
            {"role":"assistant", "content": f"This is the Resume - [{resume_text}]."},
            {"role": "user", "content": "Provide me HR questions on this resume in relation with job description. Do not add Preamble. Provide me the questions in Proper Structure"},
        ],
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.2,
        presence_penalty=0.3,
        max_completion_tokens=2048
    )

    return response.choices[0].message.content