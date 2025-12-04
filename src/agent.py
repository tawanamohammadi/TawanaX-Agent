from planner import plan

def run():
    steps = plan()
    for s in steps:
        print(f"[TawanaX-Agent] {s}")

if __name__ == "__main__":
    run()

