from pathlib import Path
import srt
from spellchecker import SpellChecker


class FONTCOL:
    DEFAULT = "\033[1;37m"
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    TEMP = "\u001b[38;2;145;231;255m"


def main():
    test_file = Path("./src/gbh.srt")
    temp_sub = srt.Subtitle(test_file)

    checker = SpellChecker()

    for i, sub in enumerate(temp_sub.entries, 1):
        words = sub.content.split()
        mispelled = [word for word in words if checker.unknown(word)]

        if len(mispelled):
            print(f"Line {i}")
            highlighted = temp_sub.entries[i - 1].content
            for w in mispelled:
                highlighted = highlighted.replace(
                    w, f"{FONTCOL.FAIL}{w}{FONTCOL.DEFAULT}"
                )
            print(f"{highlighted}\n")


if __name__ == "__main__":
    main()
