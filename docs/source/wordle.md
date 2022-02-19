# Literate programming wordle

Rendering the `wordle.org` file as webpage and showing it raw, without any
post-processing.

Unfortunately, the sphinx documentation generator doesn't understand org-mode
files, so I can't render this directly. The following is exported from org-mode
to HTML, then included as raw (static) HTML inside sphinx, so as to keep the
sidebar etc.


```{note}
You can see the raw file for context in [Source of Literate Wordle](wordle_sources.md)
```

```{eval-rst}
.. raw:: html
   :file: _collections/_static/wordle.html
```
