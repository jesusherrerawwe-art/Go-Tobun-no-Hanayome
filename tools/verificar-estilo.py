#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar-estilo.py — el detector de estilo del Volumen 1.

Nació de un problema real: el celular de Chuy NO dibuja el renglón largo (—).
Cuando la raya queda entre dos palabras, el teléfono la borra y las palabras
se pegan ("casapor la sala"). Desde el 16-oct-2026 la regla del tomo es:

    EL RENGLÓN LARGO (—) ES EXCLUSIVO DE LOS DIÁLOGOS.

Uso:
    python3 tools/verificar-estilo.py            # revisa todo volumen-1/
    python3 tools/verificar-estilo.py archivo.md # revisa uno solo

Sale con código 1 si encuentra algo. Pensado para correrlo después de
escribir cada capítulo, antes de darlo por bueno.
"""

import glob
import re
import sys
import unicodedata

LETRAS = '0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ'

# 1. Raya en una línea de NARRACIÓN (la línea no empieza con —).
NARRACION = re.compile(r'(?<!^)—')

# 2. Raya pegada a palabra por los dos lados: al desaparecer fusiona palabras.
FUSION = re.compile(rf'[{LETRAS}]—[{LETRAS}]')

# 3. Caracteres invisibles que algunos visores se comen.
INVISIBLES = {
    '\u00A0': 'espacio duro',
    '\u2007': 'espacio de cifra',
    '\u202F': 'espacio fino sin quiebre',
    '\u2009': 'espacio fino',
    '\u200A': 'espacio capilar',
    '\u200B': 'espacio de ancho cero',
    '\u200C': 'ZWNJ',
    '\u200D': 'ZWJ',
    '\uFEFF': 'BOM',
    '\u00AD': 'guion suave',
    '\u2060': 'word joiner',
    '\u2011': 'guion sin quiebre',
    '\t': 'tabulador',
}

# 4. Otros guiones tipográficos que no deben usarse como raya de diálogo.
OTROS_GUIONES = {'\u2013': 'guion medio (–)', '\u2015': 'barra horizontal (―)', '\u2212': 'signo menos (−)'}


def revisar(path):
    with open(path, encoding='utf-8') as fh:
        texto = fh.read()
    lineas = texto.split('\n')
    problemas = []

    for n, linea in enumerate(lineas, 1):
        desnuda = linea.lstrip()

        # Regla 1: nada de rayas en la narración.
        if not desnuda.startswith('—') and not desnuda.startswith('>') and '—' in linea:
            problemas.append((n, 'RAYA EN NARRACIÓN', linea.strip()[:110]))

        # Regla 2: nunca una raya entre dos letras/números.
        for m in FUSION.finditer(linea):
            problemas.append((n, 'RAYA QUE FUSIONA PALABRAS', linea[max(0, m.start() - 40):m.end() + 40]))

        # Regla 3: caracteres invisibles.
        for car, nombre in INVISIBLES.items():
            if car in linea:
                problemas.append((n, f'CARÁCTER INVISIBLE: {nombre}', linea.strip()[:110]))

        # Regla 4: otros guiones.
        for car, nombre in OTROS_GUIONES.items():
            if car in linea:
                problemas.append((n, f'GUION PROHIBIDO: {nombre}', linea.strip()[:110]))

    return problemas


def main():
    objetivos = sys.argv[1:] or sorted(glob.glob('volumen-1/capitulo-*.md'))
    if not objetivos:
        print('No encontré capítulos que revisar.')
        return 0

    total = 0
    for path in objetivos:
        problemas = revisar(path)
        nombre = path.split('/')[-1]
        if problemas:
            total += len(problemas)
            print(f'\n✗ {nombre} — {len(problemas)} problema(s)')
            for n, tipo, muestra in problemas:
                print(f'   línea {n:4d} · {tipo}\n              {muestra}')
        else:
            print(f'✓ {nombre}')

    print()
    if total:
        print(f'RESULTADO: {total} problema(s). El capítulo no está listo.')
        return 1
    print('RESULTADO: limpio. Renglón largo solo en diálogos, sin fusiones, sin invisibles.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
