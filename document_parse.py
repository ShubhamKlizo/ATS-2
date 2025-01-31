from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

# Get file details
def get_file_details(file, file_name):

    llama_doc = LlamaParse(result_type="markdown").load_data(
                                                                [file],  
                                                                extra_info={"file_name": file_name}  # llama_parse needs a file name
                                                            )


    pasrsed_document = " ".join([f"Resume Name - [{file_name}]\n Resume ID - [{doc.id_}]\n Resume Text - [{doc.text}] \n" for doc in llama_doc])

    return pasrsed_document

'''
pasrsed_document = get_file_details("sample_resume\PRASAD-ADHIKARY-CV.pdf", "sample_resume.pdf")
with open("sample_resume_text.txt", "w", encoding="utf-8") as f:
        f.write(pasrsed_document)
'''