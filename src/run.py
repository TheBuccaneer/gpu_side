import argparse, csv, os, time
try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: pyyaml. Install with: pip install pyyaml")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    args = ap.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    out_csv = cfg["output"]["csv"]
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)

    runs = int(cfg["run"]["runs"])
    n = int(cfg["run"]["n"])
    seconds = float(cfg["run"]["seconds"])
    seed = int(cfg["meta"]["seed"])

    fieldnames = ["run_id", "seed", "n", "seconds", "ts_unix", "note"]

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        t0 = time.time()
        for r in range(runs):
            # Placeholder “work”: sleep a tiny bit so timestamps differ
            time.sleep(0.01)
            w.writerow({
                "run_id": r,
                "seed": seed,
                "n": n,
                "seconds": seconds,
                "ts_unix": time.time(),
                "note": "placeholder",
            })

    dt = time.time() - t0
    print(f"Wrote {runs} rows -> {out_csv} ({dt:.2f}s)")

if __name__ == "__main__":
    main()
