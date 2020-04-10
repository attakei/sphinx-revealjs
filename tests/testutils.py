from html.parser import HTMLParser
from pathlib import Path


PROJECT_ROOT = Path(__file__).parents[1]


def gen_testdoc_conf(name="default"):
    return {
        "buildername": "revealjs",
        "srcdir": str(PROJECT_ROOT / "tests" / "testdocs" / name),
        "copy_srcdir_to_tmpdir": True,
    }


class RevealjsParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.local_css_files = []
        self.local_js_files = []
        self.remote_css_files = []
        self.remote_js_files = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Judge that local resource is exists
        if tag == "link" and attrs_dict["href"]:
            uri = attrs_dict["href"]
            if uri.startswith("http://"):
                self.remote_css_files.append(uri)
            elif uri.startswith("https://"):
                self.remote_css_files.append(uri)
            else:
                self.local_css_files.append(attrs_dict["href"])
        # script tag parse
        if tag == "script" and "src" in attrs_dict:
            uri = attrs_dict["src"]
            if uri.startswith("http://"):
                self.remote_js_files.append(uri)
            elif uri.startswith("https://"):
                self.remote_js_files.append(uri)
            else:
                self.local_js_files.append(uri)
