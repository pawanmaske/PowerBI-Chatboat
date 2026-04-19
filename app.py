def ask_ai(prompt):
    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a Power BI expert."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    # Debug (optional)
    # st.write(data)

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    elif "error" in data:
        return f"Error: {data['error']}"
    else:
        return "Unexpected response, try again"
