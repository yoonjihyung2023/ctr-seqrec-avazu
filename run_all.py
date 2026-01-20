import argparse
import subprocess
from pathlib import Path

def run(cmd):
    print(">>", " ".join(cmd))
    subprocess.run(cmd, check=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config_dir", default="configs")
    p.add_argument("--pattern", default="*.yaml")
    args = p.parse_args()

    root = Path(__file__).resolve().parent
    config_dir = root / args.config_dir
    configs = sorted(config_dir.glob(args.pattern))

    if not configs:
        raise SystemExit(f"설정파일이 없어요: {config_dir}/{args.pattern}")

    for cfg in configs:
        run(["python", "-m", "src.run", "--config", str(cfg)])

    print("DONE ✅  (reports/metrics.json 확인하세요)")

if __name__ == "__main__":
    main()
