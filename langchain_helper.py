from langchain.llms import OpenAI

def explain_area_formula(shape):
    llm = OpenAI(temperature=0, model="text-davinci-003")
    return llm(f"Explain how to calculate area of a {shape} in simple words.")
