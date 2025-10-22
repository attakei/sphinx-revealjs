=========================================
Including Highlight.js Language Packages
=========================================

Some languages listed with a "package" in the `Highlight.js supported languages table <https://highlightjs.readthedocs.io/en/latest/supported-languages.html>`_ are **not** included by default in Highlight.js or the RevealHighlight plugin. To use these languages, follow these steps:

1. Prepare the Language Definition
----------------------------------
Download or copy the language definition file. Remove the ``hljs.registerLanguage`` function call, so it only defines the language, e.g.::

    window.hljsDefineIecst = (() => {
        "use strict";
        return e => ({
            // ...language definition...
        });
    })();

1. Include the Language Definition
----------------------------------
Add the language definition file to your Sphinx config using the ``revealjs_script_files`` option::

    revealjs_script_files = [
        "revealjs/plugin/highlight/iecst.min.js",
    ]

1. Register the Language After Highlight.js Loads
-------------------------------------------------
Create a second JavaScript file (e.g. ``register-iecst.js``) to register the language after Highlight.js and RevealHighlight have loaded::

    if (typeof revealjsConfig === 'undefined') { var revealjsConfig = new Object(); }
    revealjsConfig.highlight = {
        beforeHighlight: function (hljs) {
            hljs.registerLanguage('iecst', window.hljsDefineIecst);
        }
    };

1. Include the Registration Script
----------------------------------
Add this registration script using the ``revealjs_script_appended_files`` option::

    revealjs_script_appended_files = [
        "revealjs/plugin/highlight/register-iecst.js",
    ]

.. note::
   - Replace ``iecst`` with the language you want to add.
   - This process is required for any language marked as "package" in the Highlight.js table, as they are not bundled by default.
   - The first script loads the language definition, and the second script registers it with Highlight.js after the plugin is ready.
