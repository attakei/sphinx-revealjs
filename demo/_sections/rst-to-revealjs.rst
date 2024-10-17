Convert reStructuredText to Reveal.js
=====================================

reST structure to Reveal.js sections
------------------------------------

.. container:: flex-container

   .. container:: half

      From:

      .. code-block:: rst

          Title
          =====

          First section
          -------------

          Content 1
          ^^^^^^^^^

          Content 2
          ^^^^^^^^^

   .. container:: half

      To:

      .. code-block:: html

          <section>
              <section>
                  <h1>Title</h1>
              </section>
          </section>
          <section>
              <section>
                  <h2>First section</h2>
              </section>
              <section>
                  <h3>Content 1</h3>
              </section>
              <section>
                  <h3>Content 2</h3>
              </section>
          </section>

Using built-in directives
-------------------------

.. container:: flex-container

   .. container:: half

      From:

      .. code-block:: rst

         Sub section
         -----------

         Content
         ^^^^^^^

         .. image:: ./your-image.png

   .. container:: half

      To:

      .. code-block:: html

         <section>
           <section>
              <h2>First section</h2>
           </section>
           <section>
              <h3>Content 1</h3>
              <img src="_images/your-image.png">
           </section>
         </section>

Using custom directives of Sphinx extensions
--------------------------------------------

.. container:: flex-container

   .. container:: half

      From:

      .. code-block:: rst

         .. oembed:: \
         https://twitter.com/attakei/status/1517152841550376961

      ``oembed`` is custom directive from :pypi:`oEmbedPy`.

   .. container:: half

      To:

      .. oembed:: https://twitter.com/attakei/status/1517152841550376961

Comments of reST
----------------

.. This comment in reST are not out into html

.. container:: flex-container

   .. container:: half

      From:

      .. code-block:: rst

         Title
         =====

         First section
         -------------

         .. This is comment

   .. container:: half

      To:

      .. code-block:: html

         <section>
           <h1>Title</h1>
         </section>
         <section>
           <section>
             <h2>First section</h2>
           </section>
         </section>

Comments of reST are not written into output files by default settings.
