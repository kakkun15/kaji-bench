# 鍛冶ナビ(隣のフォルダ)の build.py を借りて bench.html を組み立て、index.html に書く。
# python3 build.py ../kaji-navi
import sys, shutil, subprocess, pathlib
here = pathlib.Path(__file__).resolve().parent
navi = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here.parent / 'kaji-navi').resolve()
tmp = navi / 'src' / 'bench.html'
shutil.copy(here / 'bench.html', tmp)
try:
    subprocess.run([sys.executable, 'build.py'], cwd=navi, check=True)
    shutil.copy(navi / 'dist' / 'bench.html', here / 'index.html')
finally:
    tmp.unlink(missing_ok=True); (navi / 'dist' / 'bench.html').unlink(missing_ok=True)
print('built', here / 'index.html')
