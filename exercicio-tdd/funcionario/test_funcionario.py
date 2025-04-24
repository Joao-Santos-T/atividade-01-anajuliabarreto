"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def setUp(self):
            self.func = Funcionario(
                nome="João",
                matricula=123,
                salario_hora=50.0,
                horas_trabalhadas=160,
                custo_empregador=1000.0,
                tem_comissao=True,
                valor_comissao=200.0,
                contratos_fechados=5
            )

    def test_calcular_salario_bruto(self):
        self.assertEqual(self.func.calcular_salario_bruto(), 50.0 * 160)

    def test_calcular_custo_total(self):
        salario = self.func.calcular_salario_bruto()
        comissao = self.func.calcular_comissao()
        custo_total_esperado = salario + self.func.custo_empregador + comissao
        self.assertEqual(self.func.calcular_custo_total(), custo_total_esperado)

    def test_calcular_comissao(self):
        self.assertEqual(self.func.calcular_comissao(), 200.0 * 5)



if __name__ == "__main__":
    unittest.main() 