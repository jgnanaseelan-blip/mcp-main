FROM registry.access.redhat.com/ubi9-minimal:9.5-1741850109
LABEL maintainer="Li Duan" \
      name="hubbell_mcp" \
      description="Hubbell MCP Server"

ARG PYTHON_VERSION=3.11

# Install Python and build dependencies
RUN microdnf update -y && \
    microdnf install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-devel gcc git && \
    microdnf clean all

# Set default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 1

WORKDIR /app

# Copy source code
COPY . /app

# Create venv, install pip, pdm, uv, and project deps
RUN python3 -m venv /app/.venv && \
    /app/.venv/bin/python3 -m pip install --upgrade pip setuptools pdm uv && \
    /app/.venv/bin/python3 -m uv pip install .

## Change ownership
RUN mkdir -p /.local /.cache /.chuk_mcp_artifacts \
    && chown -R 1001:0 /app /.local /.cache /.chuk_mcp_artifacts \
    && chmod -R g=u /app /.local /.cache /.chuk_mcp_artifacts \
    && chmod -R 777 /app /.local /.cache /.chuk_mcp_artifacts

EXPOSE 8000

USER 1001
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

CMD ["sh", "-c", "chuk-mcp-server --config config.yaml"]