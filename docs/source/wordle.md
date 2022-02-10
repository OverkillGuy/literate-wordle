# Literate programming wordle

Rendering the `wordle.org` file and showing it raw, without any processing.

Unfortunately, the sphinx documentation generator doesn't understand org-mode
files, so I can't render this directly. The following is exported from org-mode
to HTML, then included as raw (static) HTML inside sphinx, so as to keep the
sidebar etc.

```{eval-rst}
.. raw:: html
   :file: _collections/_static/wordle.html
```

## Raw file

Below is the raw org-mode file that was rendered above

```{literalinclude} ../../wordle.org
```
