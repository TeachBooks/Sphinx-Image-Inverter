import os

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file

def copy_stylesheet(app: Sphinx, exc: None) -> None:
    image_filter = os.path.join(os.path.dirname(__file__), 'static', 'image_dark_mode.css')
    if app.builder.format == 'html' and not exc:
        staticdir = os.path.join(app.builder.outdir, '_static')
        copy_asset_file(image_filter, staticdir)


def setup(app: Sphinx) -> dict[str, str]:
    app.add_css_file('image_dark_mode.css')
    app.connect('build-finished', copy_stylesheet)
    return dict(parallel_read_safe=True, parallel_write_safe=True)
