{{ '{{' }} fullname {{ '}}' }}
{{ '{{' }} underline {{ '}}' }}

.. automodule:: {{ '{{' }} fullname {{ '}}' }}
   :members:
   :undoc-members:
   :show-inheritance:

{{ '{%' }} if modules {{ '%}' }}
.. autosummary::
   :toctree: {{ '{{' }} toctree {{ '}}' }}
   :recursive:

{{ '{%' }} for item in modules {{ '%}' }}
   {{ '{{' }} item {{ '}}' }}
{{ '{%' }} endfor {{ '%}' }}
{{ '{%' }} endif {{ '%}' }}
