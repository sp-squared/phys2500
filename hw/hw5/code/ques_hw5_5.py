from sympy import symbols, Eq, solve, sin, cos, rad, N

ax, ay = symbols('ax ay')

m = 2.0            # kg
th = rad(20)       # tilt of the axes, in radians

# Net force components in the tilted x and y directions
Fx = 1.0 - 5.0 - 3.0*sin(th)    # 1.0 N, 5.0 N (backward), 3.0 N's x-part
Fy = 2.82 - 3.0*cos(th)         # 2.82 N, 3.0 N's y-part

# Newton's second law: sum F = m*a, one equation per direction
sol = solve([Eq(Fx, m*ax), Eq(Fy, m*ay)], (ax, ay))

print(N(Fx, 4), N(Fy, 4))
print(N(sol[ax], 4), N(sol[ay], 4))