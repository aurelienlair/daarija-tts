import re

_FI_WORDS = {
    "فواحد": "في واحد",
    "فهاد": "في هاد",
    "فكل": "في كل",
    "فجناب": "في جناب",
    "فبلاص": "في بلاص",
    "فبلاد": "في بلاد",
    "فدار": "في دار",
    "فوقت": "في وقت",
    "فحياة": "في حياة",
}


def normalize(text: str) -> str:
    # فال → في ال  (fi l- : most common Darija contraction)
    text = re.sub(r"فال", "في ال", text)
    # individual known contractions
    for contracted, expanded in _FI_WORDS.items():
        text = text.replace(contracted, expanded)
    return text
