from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[1]


def gen_testdoc_conf(name='default'):
    return {
        'buildername': 'revealjs',
        'srcdir': str(PROJECT_ROOT / 'tests' / 'testdocs' / name),
        'copy_srcdir_to_tmpdir': True,
    }
