#!/usr/bin/env python3
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CAPTURE = ROOT / 'scripts' / 'capture_runtime.py'


def infer_kind(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ['改一下', '不对', '错了', '以后', '别再', '纠正', 'should have', 'wrong', 'next time']):
        return 'correction'
    if any(k in t for k in ['成功', 'worked', '有效', '这次不错', 'good pattern', 'reuse']):
        return 'win'
    return 'incident'


def infer_gap(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ['漏', 'missing', '没校验', 'validation']):
        return 'validation_gap'
    if any(k in t for k in ['语气', 'tone', '太官方', 'formal']):
        return 'behavior_gap'
    if any(k in t for k in ['工具', 'tool', '执行', 'execution']):
        return 'workflow_gap'
    return 'unknown'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('text')
    p.add_argument('--source', default='chat')
    p.add_argument('--context', default='chat correction')
    p.add_argument('--recurrence', default='1')
    args = p.parse_args()

    kind = infer_kind(args.text)
    gap = infer_gap(args.text)
    subprocess.run([
        sys.executable, str(CAPTURE), kind, args.text,
        '--source', args.source,
        '--context', args.context,
        '--gap', gap,
        '--recurrence', str(args.recurrence),
    ], check=True)


if __name__ == '__main__':
    main()
