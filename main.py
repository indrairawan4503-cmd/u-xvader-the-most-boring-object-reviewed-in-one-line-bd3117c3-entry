import os

ENTRY_TEXT = ("Performance review: the rubber band snapped under pressure, held nothing properly, and now lies perished in the drawer with the dead pens. Do not rehire.")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass

if __name__ == "__main__":
    main()
