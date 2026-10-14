import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('validator', Path(__file__).resolve().parents[1] / 'scripts/validate_readme.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        (self.root / 'docs').mkdir()
        (self.root / 'assets').mkdir()
        (self.root / 'assets/a b.svg').write_text('<svg/>')
        self.doc = self.root / 'docs/README.md'

    def check(self, text):
        self.doc.write_text('# Test\n' + text)
        return v.check_document(self.doc, self.root)[0]

    def test_nested_encoded_and_space_paths(self):
        self.assertEqual([], self.check('[image](../assets/a%20b.svg)\n![image](<../assets/a b.svg>)\n<img src="../assets/a b.svg">'))

    def test_missing_and_escaping(self):
        self.assertEqual(2, len(self.check('[missing](missing.txt)\n[outside](../../outside.txt)')))

    def test_fenced_and_inline_examples_are_not_links(self):
        self.assertEqual([], self.check('```md\n[x](absent.txt)\n```\n`[x](absent.txt)`'))

    def test_root_reference_and_external(self):
        self.assertEqual([], self.check('[x][asset]\n[asset]: </assets/a b.svg>\n[x](https://example.org)\n[x](#heading)'))

    def test_variant_switches(self):
        peer = self.root / 'README.en.md'
        peer.write_text('# English\n[Chinese](docs/README.md)')
        self.doc.write_text('# Chinese\n[English](../README.en.md)')
        self.assertEqual([], v.check_variants([self.doc, peer], self.root))
        self.doc.write_text('# Chinese')
        self.assertEqual(1, len(v.check_variants([self.doc, peer], self.root)))

    def test_release_text_and_binary(self):
        private = self.root / 'sample.html'
        private.write_text('/Users/example/private')
        binary = self.root / 'image.bin'
        binary.write_bytes(b'\xff')
        errors, warnings = v.scan_release([private, binary], self.root)
        self.assertEqual(1, len(errors))
        self.assertEqual(1, len(warnings))

if __name__ == '__main__':
    unittest.main()
