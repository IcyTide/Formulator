class Expression:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Expression):
            return Add(self, other)
        else:
            return Add(self, Constant(other))

    def __radd__(self, other):
        return Add(Constant(other), self)

    def __sub__(self, other):
        if isinstance(other, Expression):
            return Sub(self, other)
        else:
            return Sub(self, Constant(other))

    def __rsub__(self, other):
        return Sub(Constant(other), self)

    def __mul__(self, other):
        if isinstance(other, Expression):
            return Mul(self, other)
        else:
            return Mul(self, Constant(other))

    def __rmul__(self, other):
        return Mul(Constant(other), self)

    def __truediv__(self, other):
        if isinstance(other, Expression):
            return Div(self, other)
        else:
            return Div(self, Constant(other))

    def __rtruediv__(self, other):
        return Div(Constant(other), self)

    def __call__(self, params):
        return params[self.name]

    def __neg__(self):
        if isinstance(self, Negative):
            return self.expr
        else:
            return Negative(self)

    def diff(self, expr):
        if self.name == expr.name:
            return Constant(1)
        else:
            return Constant(0)

    def simplify(self):
        return self

    def simlify_deepest(self):
        origin = self
        while True:
            simplified = origin.simplify()
            if str(simplified) == str(origin):
                return simplified
            origin = simplified

    def __repr__(self):
        return self.name


class Constant(Expression):
    def __init__(self, value):
        super().__init__(type(self).__name__)
        self.value = value

    def __call__(self, params):
        return self.value

    def diff(self, expr):
        return Constant(0)

    def __repr__(self):
        return str(self.value)


class UnaryOperator(Expression):
    def __init__(self, expr: Expression):
        super().__init__(type(self).__name__)
        self.expr = expr


class Negative(UnaryOperator):
    def __call__(self, params):
        return -self.expr(params)

    def diff(self, expr):
        return -self.expr.diff(expr)

    def simplify(self):
        if isinstance(self.expr, Constant):
            return Constant(-self.expr.value)
        return Negative(self.expr.simplify())

    def __repr__(self):
        if isinstance(self.expr, BinaryOperator) or isinstance(self.expr, UnaryOperator):
            return f"-({self.expr})"
        else:
            return f"-{self.expr}"


class BinaryOperator(Expression):
    def __init__(self, left, right):
        super().__init__(type(self).__name__)
        self.left = left
        self.right = right


class Add(BinaryOperator):
    def __call__(self, params):
        return self.left(params) + self.right(params)

    def diff(self, expr):
        return Add(self.left.diff(expr), self.right.diff(expr))

    def simplify(self):
        if isinstance(self.left, Constant) and isinstance(self.right, Constant):
            return Constant(self.left.value + self.right.value)
        if isinstance(self.left, Constant) and self.left.value == 0:
            return self.right.simplify()
        if isinstance(self.right, Constant) and self.right.value == 0:
            return self.left.simplify()
        return Add(self.left.simplify(), self.right.simplify())

    def __repr__(self):
        return f"{self.left} + {self.right}"


class Sub(Add):
    def __call__(self, params):
        return self.left(params) - self.right(params)

    def diff(self, expr):
        return Sub(self.left.diff(expr), self.right.diff(expr))

    def simplify(self):
        if isinstance(self.left, Constant) and isinstance(self.right, Constant):
            return Constant(self.left.value - self.right.value)
        if isinstance(self.left, Constant) and self.left.value == 0:
            return (-self.right).simplify()
        if isinstance(self.right, Constant) and self.right.value == 0:
            return self.left.simplify()
        return Sub(self.left.simplify(), self.right.simplify())

    def __repr__(self):
        if isinstance(self.right, Add) or isinstance(self.right, Negative):
            return f"{self.left} - ({self.right})"
        return f"{self.left} - {self.right}"


class Mul(BinaryOperator):
    def __call__(self, params):
        return self.left(params) * self.right(params)

    def diff(self, expr):
        return Add(Mul(self.left.diff(expr), self.right), Mul(self.left, self.right.diff(expr)))

    def simplify(self):
        if isinstance(self.left, Constant) and isinstance(self.right, Constant):
            return Constant(self.left.value * self.right.value)
        if isinstance(self.left, Constant) and self.left.value == 0:
            return Constant(0)
        if isinstance(self.right, Constant) and self.right.value == 0:
            return Constant(0)
        if isinstance(self.left, Constant) and self.left.value == 1:
            return self.right.simplify()
        if isinstance(self.right, Constant) and self.right.value == 1:
            return self.left.simplify()
        return Mul(self.left.simplify(), self.right.simplify())

    def __repr__(self):
        if isinstance(self.left, Add) and isinstance(self.right, Add):
            return f"({self.left}) * ({self.right})"
        if isinstance(self.left, Add):
            return f"({self.left}) * {self.right}"
        if isinstance(self.right, Add):
            return f"{self.left} * ({self.right})"
        return f"{self.left} * {self.right}"


class Div(BinaryOperator):
    def __call__(self, params):
        return self.left(params) / self.right(params)

    def diff(self, expr):
        numerator = Sub(Mul(self.left.diff(expr), self.right), Mul(self.left, self.right.diff(expr)))
        denominator = Mul(self.right, self.right)
        return Div(numerator, denominator)

    def simplify(self):
        if isinstance(self.left, Constant) and isinstance(self.right, Constant):
            return Constant(self.left.value / self.right.value)
        if isinstance(self.right, Constant) and self.right.value == 1:
            return self.left.simplify()
        return Div(self.left.simplify(), self.right.simplify())

    def __repr__(self):
        if isinstance(self.left, Add) and isinstance(self.right, Add):
            return f"({self.left}) / ({self.right})"
        if isinstance(self.left, Add):
            return f"({self.left}) / {self.right}"
        if isinstance(self.right, Add):
            return f"{self.left} / ({self.right})"
        return f"{self.left} / {self.right}"


if __name__ == '__main__':
    x = Expression('x')
    y = Expression('y')
    z = (x + y) * 3 - 2 * y + 4 * x + x * y
    print(f"z = {z}")
    print(f"dz/dx = {z.diff(x).simlify_deepest()}")
    print(f"dz/dy = {z.diff(y).simlify_deepest()}")

    t = (x + 3 * y) * z
    print(f"t = (x + 3 * y) * z = {t}")
    print(f"dt/dx = {t.diff(x).simlify_deepest()}")
    print(f"dt/dy = {t.diff(y).simlify_deepest()}")
