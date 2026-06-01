---
name: 'Python Tool Scripts'
description: 'Coding standards for tools/ directory Python scripts'
applyTo: 'tools/**/*.py'
---

# Python Tool Script Standards

## Structure
- Every tool script must be self-contained (runnable from its directory)
- Use `argparse` for CLI argument parsing
- Output must be **valid JSON** to stdout
- Errors must output JSON with `"success": false` and `"error"` field
- Load `.env` using python-dotenv (graceful fallback if not installed)

## Error Handling
```python
try:
    result = do_something()
    print(json.dumps({"success": True, "data": result}))
except Exception as e:
    print(json.dumps({"success": False, "error": str(e)}))
    sys.exit(1)
```

## Mock Implementation Notes
- Mock functions should be clearly marked with `# MOCK` comments
- Mock data should be realistic enough for testing
- Group mock functions at the top, real implementations replace them
- The CLI interface (argparse) must remain stable — only internals change when swapping mock → real

## Dependencies
- Only use Python standard library by default
- `python-dotenv` is optional (graceful fallback)
- Document any additional dependencies in the script header
