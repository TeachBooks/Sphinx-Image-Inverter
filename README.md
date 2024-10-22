# Sphinx Image Inverter

```{admonition} User types
:class: tip
This page is useful for user type 3, 4 and 5.
```

## Introduction

When toggling dark mode in JupyterBook, images and figures are inverted by default. However, this inversion might not always be desired, as certain images may not look correct when their colors are flipped. The **Sphinx-Image-Inverter** extension provides a solution by allowing selective inversion control using the `dark-light` class.

## How does it work?
Sphinx extension that inverts the colors of images and iframes in dark mode but keeps the colours recognizable. This is particularly useful for graphs in which a certain colour is mentioned in accompanying text. Item are not converted if they are marked with the `dark-light` class (recommended for photos).

In more detail, the colors of the element are inverted, then the hue of the colors is shifted by 180 degrees, so the inverted colors change to their complementary hues. This flips the brightness and contrast, while keeping the hue somewhat recognizable (so a blue line will be a blue line in both ligth and dark mode). Black and white stay inverted (so white becomes black, and black becomes white), because they don’t have a hue. After this, the element blends with the background, making similar colors appear dark and very different colors appear bright. The overall effect creates high contrast between the element and the background, depending on their colors.

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




