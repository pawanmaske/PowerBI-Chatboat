from transformers import pipeline

def load_model():
    return pipeline("text-generation", model="gpt2")

chatbot = load_model()

query = st.text_input("Ask your question:")

if query:
    response = chatbot(query, max_length=100)
    st.write("Answer:", response[0]['generated_text'])
