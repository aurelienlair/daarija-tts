import argparse
import asyncio
import subprocess
import sys

import edge_tts

VOICES = ["ar-MA-JamalNeural", "ar-MA-MounaNeural"]


async def synthesize(text: str, voice: str, output: str) -> None:
    await edge_tts.Communicate(text, voice).save(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Text-to-speech for Moroccan Darija (Arabic script)"
    )
    parser.add_argument("text", nargs="?", help="Text to synthesize")
    parser.add_argument("-f", "--file", help="Input text file")
    parser.add_argument("-o", "--output", default="output.mp3", help="Output mp3 path")
    parser.add_argument("-v", "--voice", default=VOICES[0], choices=VOICES)
    parser.add_argument("--play", action="store_true", help="Play audio after generating")
    return parser.parse_args()


def read_text(args: argparse.Namespace) -> str:
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            return f.read()
    if args.text:
        return args.text
    if not sys.stdin.isatty():
        return sys.stdin.read()
    print("Error: provide text as argument, --file, or via stdin.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    args = parse_args()
    text = read_text(args)
    asyncio.run(synthesize(text, args.voice, args.output))
    print(f"Saved to {args.output}")
    if args.play:
        subprocess.run(["afplay", args.output], check=True)


if __name__ == "__main__":
    main()
