PYTHON := python
PYTEST := pytest

TEST_FILES := \
    tests/test_purchase_place.py \
    tests/test_booking_page.py \
    tests/test_show_summary.py

test:
	$(PYTEST) $(TEST_FILES)

help:
	@echo "  test        Exécute les tests Pytest"
	@echo "  help        Affiche cette aide"

.PHONY: test install run clean help
