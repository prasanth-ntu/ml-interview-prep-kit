# ML Interview Prep Kit — Build System

# Generate mind map data from fundamentals.md metadata
.PHONY: kb-sync
kb-sync:
	@python scripts/kb-sync.py

# Open interactive D3.js mind map locally
.PHONY: mindmap
mindmap:
	@echo "Opening interactive mind map..."
	open index.html

# Check for broken internal markdown links
.PHONY: check-links
check-links:
	@python scripts/check-links.py

# Scan for PII/confidential terms (requires scripts/.pii-terms.json)
.PHONY: pii-scan
pii-scan:
	@python scripts/pii-scan.py

# Build docs site (MkDocs Material)
.PHONY: docs-build
docs-build:
	@bash scripts/build-docs.sh

# Serve docs locally with hot reload (http://localhost:8000)
.PHONY: docs-serve
docs-serve:
	@bash scripts/build-docs.sh serve

# Serve full site locally (mirrors production layout)
# Mind map at http://localhost:9000/, docs at http://localhost:9000/docs/
.PHONY: serve
serve: docs-build
	@echo "Assembling site..."
	@rm -rf _serve
	@mkdir -p _serve/docs
	@cp index.html ml-knowledge-map-data.js _serve/
	@cp -r _site/* _serve/docs/
	@cp -r overview-prototypes _serve/overview-prototypes
	@echo "Serving at http://localhost:9000 (Ctrl+C to stop)"
	@cd _serve && python -m http.server 9000 --bind 127.0.0.1

# Full validation: sync + links + PII scan
.PHONY: validate
validate: kb-sync check-links pii-scan
