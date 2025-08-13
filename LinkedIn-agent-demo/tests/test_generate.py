
---

## **20. Tests**

### `tests/test_generate.py`
```python
from backend.app.services.generate_service import generate_post

def test_generate_post():
    post = generate_post("AI in Marketing")
    assert isinstance(post, str)
    assert len(post) > 0
