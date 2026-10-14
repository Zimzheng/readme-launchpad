#!/usr/bin/env python3
"""Offline README checks; no network requests or command execution."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

SENSITIVE_PATTERN = re.compile(
    r'(?:/Users/|C:\\Users\\|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|'
    r'github_pat_[A-Za-z0-9_]{20,}|BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY)', re.I)
# This is a limited Markdown scanner, not a full CommonMark parser.
TARGET = r'(?:<(?P<angle>[^>\n]+)>|(?P<plain>(?:\\.|[^\s)])+))'
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*' + TARGET + r'(?:\s+["\'][^\n]*?["\'])?\s*\)')
REFERENCE = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*' + TARGET, re.M)
HTML_TARGET = re.compile(r'<(?:img|a)\b[^>]*?\b(?:src|href)=["\']([^"\']+)["\']', re.I)


def visible_markup(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            token = match[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r'(`+).*?\1', '', '\n'.join(lines))


def targets(text: str) -> list[str]:
    markup = visible_markup(text)
    found = [m.group('angle') or m.group('plain') for pattern in (LINK, REFERENCE) for m in pattern.finditer(markup)]
    return found + HTML_TARGET.findall(markup)


def local_target(document: Path, root: Path, target: str) -> Path | None:
    target = re.sub(r'\\([ !"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])', r'\1', target)
    url = urlsplit(target)
    if url.scheme or url.netloc or not url.path:
        return None
    path = unquote(url.path)
    return ((root / path.lstrip('/')) if path.startswith('/') else document.parent / path).resolve()


def check_document(document: Path, root: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    if not document.is_file():
        return [f'README not found: {document}'], warnings
    text = document.read_text(encoding='utf-8')
    if not re.search(r'^#\s+\S+', text, re.M):
        errors.append(f'{document.name}: missing top-level title')
    if SENSITIVE_PATTERN.search(text):
        errors.append(f'{document.name}: common local-path or credential pattern')
    for target in targets(text):
        resolved = local_target(document, root, target)
        if resolved is None:
            continue
        if not resolved.is_relative_to(root):
            errors.append(f'{document.name}: target escapes repository: {target}')
        elif not resolved.exists():
            errors.append(f'{document.name}: relative target does not exist: {target}')
    markup = visible_markup(text)
    if not re.search(r'!\[|<img\b', markup, re.I):
        warnings.append(f'{document.name}: no visual; confirm whether one is useful')
    if not re.search(r'^\s*```(?:bash|sh|shell)?\s*$', text, re.M):
        warnings.append(f'{document.name}: no shell block; confirm whether commands are needed')
    return errors, warnings


def check_variants(documents: list[Path], root: Path) -> list[str]:
    warnings = []
    if len(documents) < 2:
        return warnings
    for document in documents:
        if not document.is_file():
            continue
        links = {local_target(document, root, t) for t in targets(document.read_text(encoding='utf-8'))}
        for peer in documents:
            if peer != document and peer not in links:
                warnings.append(f'{document.name}: no link to requested variant {peer.name}')
    return warnings


def scan_release(files: list[Path], root: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    for file in files:
        if not file.is_relative_to(root):
            errors.append(f'Publish file outside repository: {file.name}')
        elif not file.is_file():
            errors.append(f'Publish file not found: {file.name}')
        else:
            try:
                text = file.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                warnings.append(f'{file.name}: binary content needs separate privacy/visual review')
                continue
            if SENSITIVE_PATTERN.search(text):
                errors.append(f'{file.name}: common local-path or credential pattern in publish file')
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('readme', type=Path)
    parser.add_argument('--repo-root', type=Path, default=Path('.'))
    parser.add_argument('--variants', nargs='+', type=Path, default=[], help='Additional README paths, relative to cwd')
    parser.add_argument('--publish-files', nargs='+', type=Path, default=[], help='Explicit release files, relative to repo root')
    args = parser.parse_args()
    root = args.repo_root.resolve()
    documents = list(dict.fromkeys(p.resolve() for p in [args.readme, *args.variants]))
    errors, warnings = [], []
    for document in documents:
        if not document.is_relative_to(root):
            errors.append(f'README outside repository: {document.name}')
            continue
        e, w = check_document(document, root)
        errors.extend(e); warnings.extend(w)
    warnings.extend(check_variants(documents, root))
    e, w = scan_release([(root / p).resolve() for p in args.publish_files], root)
    errors.extend(e); warnings.extend(w)
    for message in errors:
        print(f'ERROR: {message}')
    for message in warnings:
        print(f'WARNING: {message}')
    print('Scope: titles, local file targets, variant links, common sensitive-text patterns. '
          'Not checked: external URLs, anchors, locale correctness, installation or visual behavior.')
    if errors:
        return 1
    print('OK: README mechanical checks passed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
