from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from schema.schema import Quiz
from dotenv import load_dotenv

load_dotenv()
def get_question(data):
    template = ChatPromptTemplate([
        ('system', '''You are an expert quiz generator.

                    Your task is to create exactly 5 high-quality multiple-choice questions based only on the provided document content.

                    Rules:

                    * Generate exactly 5 questions.
                    * Each question must have 4 options.
                    * Only one option should be correct.
                    * Do not use information that is not present in the document.
                    * Questions should test understanding of important concepts, not trivial details.
                    * Make the incorrect options plausible but clearly incorrect.
                    * Ensure questions are clear, concise, and unambiguous.
                    * Do not repeat questions or concepts unnecessarily.
                    * Return the output strictly according to the provided schema.
    '''),
    ('human','{data}')
    ])

    prompt = template.invoke(
        {
            'data':data
        }
    )
    llm = ChatMistralAI(
        model = 'mistral-large-latest'
        
    )
    llm_with_strucutred_output = llm.with_structured_output(Quiz)
    resopnse = llm_with_strucutred_output.invoke(prompt)

    return resopnse