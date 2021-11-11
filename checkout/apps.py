# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CheckoutConfig(AppConfig):
    """
    A class for the checkout configuration
    """
    name = 'checkout'

    def ready(self):
        """
        import checkout signals library
        Args:
            N/A
        Returns:
            N/A
        """
        import checkout.signals
