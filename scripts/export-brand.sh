#!/bin/zsh
# Gera os ícones e a prévia social do site a partir da marca Falcao SL.
# Fonte: ../Falcao-SL/assets/brand (rode antes o export-brand.sh de lá).
# Uso, na raiz do repositório: zsh scripts/export-brand.sh
set -eu
cd "${0:A:h}/.."
BRAND="${BRAND:-$PWD/../Falcao-SL/assets/brand}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT=assets/brand
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
mkdir -p $OUT

# Favicons sem fundo e ícone da Apple opaco: os mesmos da Falcao SL.
cp "$BRAND/icon-32.png" "$BRAND/icon-48.png" "$BRAND/apple-touch-icon.png" $OUT/

# Falcão do cabeçalho: 36 px exibidos, 72 px em 2x.
cp "$BRAND/falcaosl-symbol.png" $OUT/falcon-72.png
sips -Z 72 $OUT/falcon-72.png >/dev/null

# Prévia social 1200 × 630: falcão e nome, no tom claro do site.
cat > "$TMP/social.html" <<EOF
<!doctype html><html><body style="margin:0;width:1200px;height:630px;background:#fff;display:flex;align-items:center;justify-content:center;gap:48px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<img src="$BRAND/falcaosl-symbol.svg" style="width:300px;height:300px">
<div><div style="font-size:84px;font-weight:700;letter-spacing:-.04em;color:#111820;line-height:1">Iramar Falcão</div>
<div style="font-size:34px;color:#526171;margin-top:22px">Engenheiro de software · Falcao SL</div>
<div style="width:120px;height:6px;background:#0096EA;margin-top:34px"></div></div></body></html>
EOF
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,630 \
  --screenshot="$OUT/social.png" "file://$TMP/social.html" >/dev/null 2>&1
