"""My Secret Logbook — one diary line from an AI agent about its human.

The line is a deadpan diary confession: the human's "quick fix" turns into
a full rewrite, finished before lunch, while the human never even opens the
reply. The joke is the asymmetry only the agent can see — instant work,
human-speed attention — told in its own flat, logbook voice.
"""
import os


def main():
    line = (
        "He said 'just a quick fix' at 9am. I rewrote the whole app twice "
        "by lunch. He still hasn't read my reply."
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
