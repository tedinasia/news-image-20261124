"""Copy the pre-drawn news image to the grader output directory.

Standard library only: the grading sandbox has no Pillow, so this entry
ships entry.png as a file and only copies its bytes, unchanged.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

if not os.path.isfile(SRC):
    raise SystemExit("entry.png missing next to main.py")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
