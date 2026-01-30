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

# y_true: 정답(0/1), y_pred: 예측확률(0~1) 이라고 가정

pos = int((y_true == 1).sum())
neg = int((y_true == 0).sum())

if pos == 0 or neg == 0:
    raise SystemExit(
        f"[STOP] test split이 이상함: pos={pos}, neg={neg}. "
        "AUC/LogLoss 저장하지 마세요."
    )

if __name__ == "__main__":
    main()
