def Bernoulli (k , p):
    return p if k == 1 else (1 - p )

Bernoulli(0, 0.7)

def uniform_pdf(x, a, b):
    if a <= x <= b:
        return 1.0 / (b - a)
    return 0.0
########
uniform_pdf(6, 0, 10)  # Should return 0.1
uniform_pdf(0, 0, 10)  # Should return 0.1
uniform_pdf(10, 0, 10)  # Should return 0.1
uniform_pdf(4, 0, 10)  # Should return 0.1
uniform_pdf(11, 0, 10)  # Should return 0.0

# so the uniform pdf is a constant function between a and b, and 0 outside that range.