# daarija-tts

Text-to-speech CLI for Moroccan Darija (Arabic script), using Microsoft's [ar-MA neural voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#arabic) via [`edge-tts`](https://github.com/rany2/edge-tts).

## Voices

| Voice | Gender |
|---|---|
| [`ar-MA-JamalNeural`](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#arabic) (default) | Male |
| [`ar-MA-MounaNeural`](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#arabic) | Female |

## Usage

### Synthesize a file

```bash
make run FILE=input.txt
```

### Change voice

```bash
make run FILE=input.txt VOICE=ar-MA-MounaNeural
```

### Inline text

```bash
make run TEXT="كان يا ما كان"
```

### Speed control

Default speed is `0.75`. Override with `SPEED=`:

```bash
make run FILE=input.txt SPEED=1.0
```

### Direct CLI

```bash
python tts.py -f input.txt -o output.mp3 --play
python tts.py "نص قصير" --voice ar-MA-MounaNeural --speed 0.8
```

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Requires Python 3.10+ and an internet connection ([edge-tts](https://github.com/rany2/edge-tts) streams from Microsoft servers).

## Text normalization

`normalize.py` expands common Darija contractions before synthesis:

| Input | Expanded |
|---|---|
| فالبيت | في البيت |
| فواحد | في واحد |
| فالدوار | في الدوار |
