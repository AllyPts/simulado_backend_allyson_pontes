class Calculator:
    def add(self, a: float, b: float) -> float:
        """Metodo ja implementado para servir de exemplo."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Metodo subitração implementado"""
        return a - b 

    def multiply(self, a: float, b: float) -> float:
        """Metodo multiplicação implementado"""
        return a * b
    def divide(self, a: float, b: float) -> float:
        """Metodo divisão implementado"""
        if b == 0:
            raise ValueError("divisão por zero não é permitida.")
        return a / b