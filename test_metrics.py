import subprocess
import time

ollama_path = r"C:\Users\sreet\AppData\Local\Programs\Ollama\ollama.exe"

def ask_ollama(prompt_text, model="llama2"):
    start = time.time()
    result = subprocess.run(
        [ollama_path, "run", model, prompt_text],
        capture_output=True,
        text=True,
        encoding="utf-8"  # <-- force UTF-8
    )
    end = time.time()
    
    latency = end - start
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}", latency
    return result.stdout.strip(), latency

answer, latency = ask_ollama("Explain gravity in one sentence.")
print(f"Answer: {answer}\nLatency: {latency:.2f}s")
