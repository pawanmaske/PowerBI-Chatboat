import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxx"}  # your token

def query_hf(prompt):
    payload = {"inputs": prompt}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        # If response is not JSON
        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code}"}
        
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timeout. Try again."}
    
    except Exception as e:
        return {"error": str(e)}

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    prompt = f"You are a Power BI expert. Answer clearly:\n{query}"

    result = query_hf(prompt)

    # Handle all cases
    if isinstance(result, list) and "generated_text" in result[0]:
        answer = result[0]["generated_text"]
    elif isinstance(result, dict) and "error" in result:
        answer = result["error"]
    else:
        answer = "Model loading... please try again in few seconds"

    st.write("Answer:", answer)
