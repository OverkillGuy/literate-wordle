# Literate programming wordle

Including the entire `wordle.org` file raw, without any processing.

Unfortunately, the sphinx documentation generator doesn't understand org-mode
files, so I can't render this directly. The following is exported from org-mode
to HTML, then included as raw (static) HTML inside sphinx, so as to keep the
sidebar etc.

```{eval-rst}
.. raw:: html
   :file: _static/wordle.html
```

## Raw file

Below is the raw org-mode file that rendered as above

```{literalinclude} ../../wordle.org
```
