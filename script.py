import pathlib
import whisper
from langchain_ollama.llms import OllamaLLM
import textwrap

# Caminho do arquivo de áudio
file_path = pathlib.Path(__file__).parent.joinpath("theOffice.mp3").as_posix()

# Carrega o modelo Whisper
whisper_model = whisper.load_model("tiny")

# Transcreve o áudio
whisper_result = whisper_model.transcribe(file_path)
transcription = whisper_result["text"]

# Prompt para o modelo Ollama
prompt = f"Transcription: {transcription}"

# Carrega o modelo de linguagem Ollama
llm_model = OllamaLLM(model="llama3.2:3b")

# Invoca o modelo com o prompt
response = llm_model.invoke(prompt)

# Exibe a resposta formatada
print('\n')
print("=== Resultados da Análise ===\n")
wrapped_response = textwrap.fill(response.strip(), width=80)  # Formata o texto para largura ajustada
print(wrapped_response)
print("\n=== Fim da Análise ===")
print('\n')
