=========================
Customizing design simply
=========================

When using bundled theme, you can customize design by adding custom CSS.

Example: Disable transform style in header text
===============================================

Some of reveal.js bundled themes (ex: ``black`` ) set uppercase in ``text-transform`` of heading texts.
You can add extra custom CSS to use other settings.

Source
------

.. code-block:: python
   :caption: conf.py
   :name: conf-py

   revealjs_css_files = [
       "revealjs/plugin/highlight/zenburn.css",
       "custom.css",
   ]

.. code-block:: css
   :caption: custom.css
   :name: custom-css

   .reveal h1, .reveal h2, .reveal h3, .reveal h4, .reveal h5, .reveal h6 {
      text-transform: none;
   }
