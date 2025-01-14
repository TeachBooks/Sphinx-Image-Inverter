# Sphinx extension: Image Inverter

## Introduction

When toggling dark mode in JupyterBook, images and figures are not inverted by default, but a white background is inserted. However, this white background might not always be desired in dark mode.

The **Sphinx-Image-Inverter** extension provides a solution by applying an automatic filter to images and iframes. If this filter is not desired for certain items, the **Sphinx-Image-Inverter** extension provides a solution by allowing selective disabling using the `dark-light` class.

## How does it work?
This Sphinx extension applies a filter such that dark and light colors are switched, however keeps the colours recognizable. This is particularly useful for graphs in which a certain colour is mentioned in accompanying text. Items are not converted if they are marked with the `dark-light` class (recommended for example for photos).

In more detail, first the colors of the element are inverted, then the hue of the colors is shifted by 180 degrees, so the inverted colors change to their complementary hues. This flips the brightness and contrast, while keeping the hue somewhat recognizable (so a blue line will be a blue line in both ligth and dark mode). Black and white stay inverted (so white becomes black, and black becomes white), because they don’t have a hue. Next, the colors are slightly saturated to enforce a better contrast. After this, the element blends with the background, making similar colors appear dark and very different colors appear bright. The overall effect creates high contrast between the element and the background, depending on their colors.

## Installation
To install the Sphinx-Image-Inverter, follow these steps:

**Step 1: Install the Package**

Install the `sphinx-image-inverter` package using `pip`:
```
pip install sphinx-image-inverter
```

**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
sphinx-image-inverter
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions:
```
sphinx: 
    extra_extensions:
        - sphinx_image_inverter
```

## Usage
### Disable Image/Figure Inversion

By default, when dark-mode is toggled in JupyterBook, all images and figures are inverted. To prevent certain images from being inverted, apply the `dark-light` class. The steps for both Markdown and HTML formats are given below.

**For Markdown Format**

1. Locate the markdown file that contains the image or figure you want to exclude from inversion.
2. Add the `:class: dark-light` attribute to the figure directive.

    Example:
    ```
    ```{figure} example_folder/example_image.jpg
    :class: dark-light
    :width: 400```
    ```

**For HTML Format**

If your image or figure is defined using HTML, apply the `dark-light` class directly to the tag.

```
<iframe 
    src="some_figure.html" 
    width="600" 
    height="300" 
    class="dark-light">
</iframe>
```

Done! Now your image will not be inverted when dark mode is toggled.

### Display Text According to Theme

You may want to display different text depending on whether the dark mode or light mode is enabled. To do that, you can use the following classes:

- **Light Mode only:**
```
<span class="only-light">Text only visible in Light Mode.</span>
```
- **Dark Mode only:**
```
<span class="only-dark">Text only visible in Dark Mode.</span>
```
These classes make sure that your text is only visible in the specified modes.

### Compatible LaTeX colours
If you'd like to use LaTeX colours which invert similarly, use the approach Sphinx extension [Sphinx-Named-Colors](https://github.com/TeachBooks/Sphinx-Named-Colors).

## Contribute
This tool's repository is stored on [GitHub](https://github.com/TeachBooks/Sphinx-Image-Inverter). The `README.md` of the branch `Manual` is also part of the [TeachBooks manual](https://teachbooks.io/manual/external/Sphinx-Image-Inverter/README.html) as a submodule. If you'd like to contribute, you can create a fork and open a pull request on the [GitHub repository](https://github.com/TeachBooks/Sphinx-Image-Inverter). To update the `README.md` shown in the TeachBooks manual, create a fork and open a merge request for the [GitHub repository of the manual](https://github.com/TeachBooks/manual). If you intent to clone the manual including its submodules, clone using: `git clone --recurse-submodulesgit@github.com:TeachBooks/manual.git`.
