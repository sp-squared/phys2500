from sympy import symbols, Eq, solve, simplify, N

n, m, g, a = symbols('n m g a', positive=True)

# Newton's second law for the astronaut (up is positive)
eq = Eq(n - m*g, m*a)

n_expr = solve(eq, n)[0]
print(simplify(n_expr))            # symbolic result: m*(a + g)

# Part (a): at rest
vals_a = {m: 80, g: 9.8, a: 0}
n_a = n_expr.subs(vals_a)

# Part (b): accelerating up at 10 m/s^2
vals_b = {m: 80, g: 9.8, a: 10}
n_b = n_expr.subs(vals_b)

print("(a) n =", N(n_a, 4), "N")
print("(b) n =", N(n_b, 4), "N")

# Checks
print("net force in (a):", N(n_a - 80*9.8, 4))      # should be 0
print("net force in (b):", N(n_b - 80*9.8, 4))      # should be 800
print("m*a in (b):", 80*10)                          # should match the line above