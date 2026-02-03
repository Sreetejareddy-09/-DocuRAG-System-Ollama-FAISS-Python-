import subprocess

ollama_path = r"C:\Users\sreet\AppData\Local\Programs\Ollama\ollama.exe"

def ask_ollama(prompt_text):
    result = subprocess.run(
        [ollama_path, "run", "llama2", prompt_text],
        capture_output=True,
        text=True
    )
    return result.stdout

# Example usage with top chunks from your PDF
top_chunks_text = "Insert your top PDF chunks here."
answer = ask_ollama(top_chunks_text)
print("AI Answer:\n", answer)
