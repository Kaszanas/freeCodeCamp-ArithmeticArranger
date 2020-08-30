# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

# Run unit tests automatically
main(module='test_module', exit=False)