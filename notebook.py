# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## Hello world!""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, 1)
    slider
    return (slider,)


@app.cell
def _(slider):
    slider.value * "hello " + "world"
    return


if __name__ == "__main__":
    app.run()
