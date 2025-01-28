# O que este script faz?

Este script realiza a **transcrição de um arquivo de áudio** utilizando o modelo **Whisper**, e em seguida, utiliza o modelo **Ollama LLM** para processar a transcrição e gerar uma análise formatada do conteúdo.

# Passos para rodar o script

## 1. Garantir que o Python e o PIP estejam instalados

Verifique se o Python e o PIP estão instalados no seu sistema:

```sh
python --version
pip --version
```

## 2. Instalar as bibliotecas necessárias

Instale as bibliotecas **`openai-whisper`**, **`langchain_ollama`** e **`textwrap`** usando o seguinte comando:

```sh
pip install openai-whisper langchain_ollama
```

## 3. Garantir que o [FFmpeg](https://ffmpeg.org/) esteja instalado

O Whisper utiliza o **FFmpeg** para processar os arquivos de áudio. Certifique-se de que o FFmpeg está instalado e configurado no PATH do sistema. Para verificar:

```sh
ffmpeg -version
```

Se não estiver instalado, siga [estas instruções](https://ffmpeg.org/download.html).

## 4. Garantir que o [Ollama](https://ollama.com/) esteja instalado

Instale o Ollama e verifique se está funcionando corretamente:

```sh
ollama -v
```

## 5. Instalar o modelo LLM `llama3.2:3b`

Baixe o modelo necessário para o Ollama:

```sh
ollama pull llama3.2:3b
```

## 6. Executar o script

Após todas as dependências estarem configuradas, execute o script:

```sh
python script.py
```

---

# Exemplos de uso

## Entrada:

**Áudio**: *theOffice.mp3* (Trecho curto de uma conversa).

## Saída:

**Análise formatada do conteúdo**:

```
=== Resultados da Análise ===

This conversation seems to be a dialogue between two people, possibly friends
or family members. The speaker is expressing frustration and confusion about an
event or situation where something didn't go as planned.

The person being addressed, "Ryan", might have been involved in the event or
made a mistake that led to the negative outcome. The speaker's tone suggests
they're trying to understand what went wrong, but are coming up empty.

The line "Not everything's a lesson, Ryan" implies that sometimes things just
don't work out as expected, and it's not always about learning from mistakes.
This line might be suggesting that Ryan made a mistake, but the outcome wasn't
necessarily meant to teach a valuable lesson.

The final phrase "Sometimes you just fail" is a blunt admission that sometimes
things don't go as planned, and that's okay. It's a recognition that failure is
a natural part of life, and it doesn't always have to be tied to learning
something new.

=== Fim da Análise ===
```

---

# Considerações Finais

Este script demonstra como combinar o poder do **Whisper** para transcrição de áudio e o **Ollama LLM** para análise de texto, permitindo uma aplicação prática de modelos de linguagem e processamento de áudio. Se tiver dúvidas ou problemas, confira as instruções acima ou entre em contato. 🚀
