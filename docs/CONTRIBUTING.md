# Contributing to Daily Journal

Thank you for your interest in contributing! Here are guidelines to help you get started.

## How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
4. **Make your changes**
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Ivan0206cool/ai-test.git
cd ai-test

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Run `black` and `flake8` before committing

```bash
black src/
flake8 src/
```

## Testing

- Write tests for new features
- Ensure all tests pass before opening a PR
- Aim for good test coverage

```bash
pytest --cov=src/
```

## Reporting Issues

- Check if the issue already exists
- Provide a clear description
- Include steps to reproduce
- Share relevant code or screenshots

## Feature Requests

- Describe the feature and why it would be useful
- Provide examples if possible
- Be open to discussion and feedback

## Questions?

Feel free to open an issue with the `question` label!

Thank you for contributing! 🎉