from dataquantum_load_csv.load_csv import get_load_csv


def test_get_load_csv() -> None:
    """Testa se a função retorna o valor recebido."""
    resultado = get_load_csv("teste_início")

    assert resultado == "teste_início"
