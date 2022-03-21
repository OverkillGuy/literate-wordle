# Literate programming wordle

Rendering the `wordle.org` file as webpage and including in the docs as-is,
because the Sphinx documentation generator doesn't understand org-mode files, so
we couldn't render this page directly from Sphinx the usual way.


```{note}
You can see the raw file for context in [Source of Literate Wordle](wordle_sources.md)
```

```{eval-rst}
.. raw:: html
   :file: _collections/_static/wordle.html
```
