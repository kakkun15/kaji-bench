# 鍛冶ナビ 性能テスト

鍛冶ナビ(kakkun15/kaji-navi)の打ち方を、同じ局でふつう・最強・最強(GPU)と打ち比べるページ。2026-11-07 に分けた。

- `index.html`: 組み立て済み(そのまま開ける)。
- `bench.html`: 元のページ。計算の部品(core.js・game.js・value.js・pool.js・gpumax.js・重み)は鍛冶ナビの物を使う。
- 組み立て直す: 鍛冶ナビを隣に置いて `python3 build.py ../kaji-navi`。鍛冶ナビの計算を直した時はこれで作り直す。
