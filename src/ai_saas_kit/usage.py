from __future__ import annotations
from dataclasses import dataclass, field
import time

def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)

@dataclass
class TokenBudget:
    limit: int
    used: int = 0
    def can_spend(self, n: int) -> bool:
        return self.used + n <= self.limit
    def spend(self, n: int) -> bool:
        if not self.can_spend(n):
            return False
        self.used += n
        return True
    @property
    def remaining(self) -> int:
        return max(0, self.limit - self.used)

@dataclass
class RateLimiter:
    max_calls: int
    window_sec: float
    _times: list[float] = field(default_factory=list)
    def allow(self, now: float | None = None) -> bool:
        now = time.time() if now is None else now
        self._times = [t for t in self._times if now - t < self.window_sec]
        if len(self._times) >= self.max_calls:
            return False
        self._times.append(now)
        return True
