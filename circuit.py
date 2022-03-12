from circuitbreaker import CircuitBreaker


def local_call(args):
    return "I am a local method\n"


class CircuitBreakerConfig(CircuitBreaker):
    FAILURE_THRESHOLD = 5
    RECOVERY_TIMEOUT = 10
    FALLBACK_FUNCTION = local_call
