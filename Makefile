
local_sdist:
	@if [ -z "${ANACONDA_DEVEL_DATA}" ]; then \
		echo "Error: ANACONDA_DEVEL_DATA is not set"; \
		exit 1; \
	fi
	python -m build --sdist --outdir "${ANACONDA_DEVEL_DATA}"


