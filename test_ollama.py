import subprocess

result = subprocess.run(
    ["ollama", "run", "mistral-7b", "--prompt", "Hello"],
    capture_output=True,
    text=True
)
print(result.stdout)
