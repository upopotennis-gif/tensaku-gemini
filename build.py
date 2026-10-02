"""build/template.html に添削室の見た目（base.css）と観点（types.js）を入れて index.html を作る。

  python3 build.py
観点を変えたいときは ~/shutsugan-tensaku/tensaku.html の TYPES を直してから
  python3 build.py --sync   （base.css・types.js・ap.json を添削室から取り直す）
"""
import os, sys, shutil
H = os.path.dirname(os.path.abspath(__file__))
if "--sync" in sys.argv:
    src = open(os.path.expanduser("~/shutsugan-tensaku/tensaku.html"), encoding="utf-8").read()
    open(f"{H}/build/base.css", "w").write(src[src.index("<style>") + 7:src.index("</style>")])
    open(f"{H}/build/types.js", "w").write(src[src.index("const TYPES = {"):src.index("const SAMPLE")])
    shutil.copy(os.path.expanduser("~/shutsugan-tensaku/ap.json"), f"{H}/ap.json")
t = open(f"{H}/build/template.html", encoding="utf-8").read()
t = t.replace("%%CSS%%", open(f"{H}/build/base.css", encoding="utf-8").read())
t = t.replace("%%TYPES%%", open(f"{H}/build/types.js", encoding="utf-8").read())
open(f"{H}/index.html", "w", encoding="utf-8").write(t)
print("index.html", len(t))
