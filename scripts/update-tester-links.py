#!/usr/bin/env python3
"""
update-tester-links.py — Atualiza links de TestFlight e Google Play em massa.

Sincroniza automaticamente _data/products.yml no portfolio e o site/index.html
de cada repositório em ~/Github.

Uso:
  python3 scripts/update-tester-links.py --list
  python3 scripts/update-tester-links.py --app quickread --testflight https://testflight.apple.com/join/NOVO_TOKEN
  python3 scripts/update-tester-links.py --app lira --google-play https://play.google.com/apps/testing/com.falcaosl.lira
"""

import argparse
import re
import sys
from pathlib import Path

PORTFOLIO_DIR = Path(__file__).resolve().parent.parent
PRODUCTS_YML = PORTFOLIO_DIR / "_data" / "products.yml"
GITHUB_DIR = PORTFOLIO_DIR.parent

APP_REPO_MAP = {
    "quickread": "Quickread",
    "swipeclean": "SwipeClean",
    "pocketrocket": "PocketRocket",
    "lira": "Lira",
    "meuposto": "MeuPosto",
    "pitaia": "pitaia",
    "matiz": "Matiz",
    "dictasy": "Dictasy",
    "spokennote": "SpokenNote",
    "spokenbook": "SpokenBook",
    "multidroid": "MultiDroid",
}


def list_links():
    if not PRODUCTS_YML.exists():
        print(f"Erro: {PRODUCTS_YML} não encontrado.")
        return

    content = PRODUCTS_YML.read_text(encoding="utf-8")
    print("\n=== Links de Testes Atuais no Portfolio (_data/products.yml) ===\n")
    
    current_key = None
    for line in content.splitlines():
        key_match = re.search(r"^\s*-\s*key:\s*([a-zA-Z0-9_-]+)", line)
        if key_match:
            current_key = key_match.group(1)
            print(f"[{current_key.upper()}] (Repo: {APP_REPO_MAP.get(current_key, 'N/A')})")
        tf_match = re.search(r"^\s*testflight:\s*(\S+)", line)
        if tf_match and current_key:
            print(f"   TestFlight:  {tf_match.group(1)}")
        gp_match = re.search(r"^\s*google_play:\s*(\S+)", line)
        if gp_match and current_key:
            print(f"  ▶ Google Play: {gp_match.group(1)}")
    print()


def update_link(app_key, tf_url=None, gp_url=None):
    if not PRODUCTS_YML.exists():
        print(f"Erro: {PRODUCTS_YML} não encontrado.")
        return

    app_key = app_key.lower()
    content = PRODUCTS_YML.read_text(encoding="utf-8")

    # Atualiza em _data/products.yml
    lines = content.splitlines()
    new_lines = []
    in_target_app = False

    for line in lines:
        key_match = re.search(r"^\s*-\s*key:\s*([a-zA-Z0-9_-]+)", line)
        if key_match:
            in_target_app = (key_match.group(1).lower() == app_key)

        if in_target_app:
            if tf_url and re.search(r"^\s*testflight:", line):
                new_lines.append(f"    testflight: {tf_url}")
                continue
            if gp_url and re.search(r"^\s*google_play:", line):
                new_lines.append(f"    google_play: {gp_url}")
                continue

        new_lines.append(line)

    PRODUCTS_YML.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"✓ Atualizado _data/products.yml para o app '{app_key}'.")

    # Atualiza no site individual se existir
    repo_name = APP_REPO_MAP.get(app_key)
    if repo_name:
        site_index = GITHUB_DIR / repo_name / "site" / "index.html"
        if site_index.exists():
            site_content = site_index.read_text(encoding="utf-8")
            changed = False
            if tf_url:
                site_content, count = re.subn(
                    r"https://testflight\.apple\.com/join/[a-zA-Z0-9_-]+",
                    tf_url,
                    site_content,
                )
                if count > 0:
                    changed = True
                    print(f"✓ Atualizado link de TestFlight em {site_index} ({count} ocorrências).")
            if gp_url:
                site_content, count = re.subn(
                    r"https://play\.google\.com/apps/testing/[a-zA-Z0-9_.-]+",
                    gp_url,
                    site_content,
                )
                if count > 0:
                    changed = True
                    print(f"✓ Atualizado link do Google Play em {site_index} ({count} ocorrências).")

            if changed:
                site_index.write_text(site_content, encoding="utf-8")
        else:
            print(f"- Site individual não encontrado em {site_index}.")


def main():
    parser = argparse.ArgumentParser(description="Atualiza links de TestFlight e Google Play.")
    parser.add_argument("--list", action="store_true", help="Lista todos os links configurados")
    parser.add_argument("--app", type=str, help="Chave do aplicativo (ex: quickread, lira, meuposto)")
    parser.add_argument("--testflight", type=str, help="Nova URL do TestFlight")
    parser.add_argument("--google-play", type=str, help="Nova URL do Google Play")

    args = parser.parse_args()

    if args.list or len(sys.argv) == 1:
        list_links()
        return

    if not args.app:
        print("Erro: especifique o aplicativo com --app <chave>.")
        sys.exit(1)

    update_link(args.app, args.testflight, args.google_play)


if __name__ == "__main__":
    main()
