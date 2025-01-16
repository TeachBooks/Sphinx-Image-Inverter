import os

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset_file

try:
    from sphinx_image_inverter._version import version as __version__
except ImportError:
    __version__ = "1.0.0"

def copy_stylesheet(app: Sphinx, exc: None) -> None:
    # load template
    image_filter = os.path.join(os.path.dirname(__file__), 'static', 'image_dark_mode.css')
    with open(image_filter,'r') as css:
        image_filter_content = css.read()
    image_filter_content = image_filter_content.replace("<saturation>","1.5")
    if app.builder.format == 'html' and not exc:
        staticdir = os.path.join(app.builder.outdir, '_static')
        outfile = os.path.join(staticdir,'image_dark_mode.css')
        with open(outfile,'w') as css:
            css.write(image_filter_content)
        


def setup(app: Sphinx):
    app.add_css_file('image_dark_mode.css')
    app.connect('build-finished', copy_stylesheet)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
