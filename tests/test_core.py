from ai_saas_kit import TokenBudget, RateLimiter, estimate_tokens

def test_tokens():
    assert estimate_tokens("abcd") == 1

def test_budget():
    b = TokenBudget(10)
    assert b.spend(4)
    assert b.remaining == 6
    assert not b.spend(10)

def test_rate():
    r = RateLimiter(2, window_sec=60)
    assert r.allow(1.0) and r.allow(1.1)
    assert not r.allow(1.2)
