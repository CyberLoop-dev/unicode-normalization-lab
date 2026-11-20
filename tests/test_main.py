import unittest
from main import analyze

class Tests(unittest.TestCase):
    def test_canonical_composition(self):
        result = analyze("e\u0301")
        self.assertEqual(result["NFC"]["normalized"], "é")
        self.assertEqual(result["NFD"]["length"], 2)
    def test_compatibility_form(self):
        self.assertEqual(analyze("ﬃ")["NFKC"]["normalized"], "ffi")
    def test_ascii_is_stable(self):
        result = analyze("hello")
        self.assertFalse(any(item["changed"] for item in result.values()))
    def test_codepoint_names(self):
        self.assertEqual(analyze("A")["NFC"]["codepoints"][0]["codepoint"], "U+0041")

if __name__ == "__main__":
    unittest.main()
