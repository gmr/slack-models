# CLAUDE.md - slack-models Repository Guide

## Project Overview

**slack-models** is a Python library providing comprehensive Pydantic models for working with the Slack API. The library offers type-safe data structures for Slack events, webhooks, users, channels, files, and other API objects.

### Key Information
- **Purpose**: Pydantic Models for Slack API integration
- **License**: BSD-3-clause
- **Python Requirements**: 3.12+
- **Main Dependency**: pydantic>=2.11.3,<3
- **Author**: Gavin M. Roy <gavinr@aweber.com>
- **Repository**: https://github.com/gmr/slack-models
- **Documentation**: https://gmr.github.io/slack-models/

## Project Architecture

### Package Structure
```
slack-models/
├── src/slack_models/           # Main package (src-layout)
│   ├── __init__.py            # Package metadata and version
│   ├── models.py              # All Pydantic models
│   └── py.typed               # Type annotations marker
├── tests/                     # Test directory (currently empty)
├── pyproject.toml             # Project configuration
├── mkdocs.yml                 # Documentation configuration
├── .pre-commit-config.yaml    # Pre-commit hooks
├── .github/workflows/         # GitHub Actions CI/CD
└── README.md                  # Basic project information
```

### Core Models Architecture

The library is organized around several model categories:

1. **Core Slack Objects**:
   - `User`: Comprehensive user representation with profile and enterprise data
   - `Channel`: Workspace channel information following official Slack API
   - `File` & `FileContent`: File sharing and content handling
   - `UserProfile` & `EnterpriseUser`: Extended user information

2. **Event Models**:
   - `MessageEvent`: Channel message events
   - `AppMentionEvent`: App mention notifications
   - `ReactionAddedEvent` & `ReactionRemovedEvent`: Reaction events
   - `TeamJoinEvent`: New member notifications
   - `FileCreatedEvent` & `FileDeletedEvent`: File events
   - `ChannelCreatedEvent`, `ChannelDeletedEvent`, `ChannelRenameEvent`: Channel events

3. **Webhook Models**:
   - `SlackEventCallback`: Standard event callback envelope
   - `SlackUrlVerification`: URL verification challenge
   - `SlackAppRateLimited`: Rate limiting notifications

4. **Supporting Models**:
   - `Reaction`, `MessageItem`, `MessageEdited`, `Authorization`
   - `ChatMessage`: Bot conversation history and context

5. **Union Types**:
   - `SlackEvent`: All possible event types
   - `SlackWebhookPayload`: All webhook payload types
   - `EVENT_MAP`: Dictionary mapping event types to model classes

## Development Workflow

### Build System
- **Build Backend**: hatchling (modern Python packaging)
- **Layout**: src-layout packaging for clean organization
- **Version Management**: Direct version string in pyproject.toml (currently "1.0.0")

### Development Commands

```bash
# Setup development environment
python -m pip install --upgrade pip
pip install -e '.[dev]'

# Install pre-commit hooks
pre-commit install

# Run linting
ruff check .
ruff format .

# Run type checking
mypy src/slack_models

# Run tests (when implemented)
pytest --cov --cov-report=xml

# Build documentation
mkdocs build

# Build package
python -m build --wheel
```

### Code Quality Standards

**Linting Configuration (ruff)**:
- Line length: 79 characters
- Target: Python 3.12
- Single quotes preferred
- Comprehensive rules: ANN, ASYNC, B, E/W, F, S
- Type annotations required (ANN rules)

**Testing**:
- Framework: pytest with coverage
- Minimum coverage: 90% (configured in pyproject.toml)
- Current status: Tests directory exists but is empty

**Type Checking**:
- Tool: mypy for static type analysis
- py.typed file indicates full type annotation support

## Key Files and Relationships

### /src/slack_models/models.py
- **Purpose**: Contains all Pydantic model definitions
- **Key Features**:
  - Python 3.10+ union syntax (| operator)
  - Comprehensive docstrings with Slack API references
  - Type-safe event handling with EVENT_MAP dictionary
  - Strict adherence to official Slack API specifications

### /src/slack_models/__init__.py
- **Purpose**: Package metadata and version management
- **Key Features**:
  - Dynamic version detection via importlib.metadata
  - Fallback to '0.0.0-dev' for development
  - Export configuration via __all__

### /pyproject.toml
- **Purpose**: Central project configuration
- **Key Sections**:
  - Build system: hatchling configuration
  - Dependencies: pydantic core, dev tools, docs tools
  - Tool configurations: ruff, pytest, coverage, mypy

## Dependencies and Requirements

### Core Dependencies
- **pydantic**: >=2.11.3,<3 (core data modeling)

### Development Dependencies
- **build**: Package building
- **coverage**: Test coverage reporting
- **mypy**: Static type checking
- **pre-commit**: Git hooks
- **pytest** & **pytest-cov**: Testing framework
- **ruff**: Linting and formatting

### Documentation Dependencies
- **mkdocs** & **mkdocs-material**: Documentation generation
- **mkdocstrings**: API documentation from docstrings
- **black**: Code formatting for signatures
- **griffe-pydantic**: Pydantic model documentation

## Testing Approach

### Current Status
- Tests directory exists but contains no test files
- pytest configuration in pyproject.toml ready for implementation
- Coverage reporting configured (90% minimum)

### Testing Strategy (Recommended)
- Unit tests for each Pydantic model
- Validation tests for edge cases and error conditions
- Integration tests for EVENT_MAP functionality
- Documentation tests for code examples

## CI/CD Pipeline

### GitHub Actions
- **test.yml**: Main CI pipeline
- **Matrix Testing**: Python 3.12 and 3.13
- **Steps**:
  1. Checkout code
  2. Install Hatch
  3. Setup Python environment
  4. Install dependencies
  5. Lint with ruff
  6. Type check with mypy
  7. Test with pytest (coverage)
  8. Upload coverage to Codecov

### Pre-commit Hooks
- File validation (shebang, TOML, YAML)
- Debug statement detection
- File ending and whitespace fixes
- ruff format and check

## Special Conventions and Patterns

### API Compliance
The library strictly follows the official Slack API specifications:
- All models match official Slack API object structures
- No custom fields beyond what Slack provides
- `ChatMessage`: Bot conversation history and context management
- Comprehensive type safety with Pydantic validation

### Code Style
- Python 3.10+ type hints with union operator (|)
- Single quotes for strings
- Comprehensive docstrings with Slack API references
- Type annotations required for all functions and methods
- 79-character line length limit

### Model Design Patterns
- Union types for polymorphic data structures
- Literal types for event type discrimination
- Optional fields with proper defaults
- Extra configuration handling where needed
- Comprehensive field documentation

## Development Notes

### Missing Components
- No actual test implementations (tests/ directory empty)
- No VERSION file (version managed in pyproject.toml)
- No bootstrap script (uses GitHub Actions exclusively)
- No CI scripts directory (modern GitHub Actions approach)

### Documentation
- MkDocs with Material theme
- Automatic API documentation via mkdocstrings
- GitHub Pages deployment configured
- Single-page documentation structure

### Future Considerations
- Implement comprehensive test suite
- Add examples and usage documentation
- Consider adding utility functions for common operations
- Evaluate need for additional Slack API models
