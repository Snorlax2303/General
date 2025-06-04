# Sistema de Controle de Férias

Este projeto é um exemplo simples de aplicação em Python para registrar funcionários e controlar suas férias.

## Requisitos
- Python 3.8+

## Como usar
Execute os comandos abaixo a partir do diretório `ferias`.

### Adicionar funcionário
```bash
python ferias.py add_employee "Nome do Funcionário"
```

### Listar funcionários
```bash
python ferias.py list_employees
```

### Registrar férias
```bash
python ferias.py add_vacation <id_funcionario> 2023-12-01 2023-12-10
```

### Listar férias
```bash
python ferias.py list_vacations [--emp_id <id_funcionario>]
```

Os dados são armazenados no arquivo `data.json`.
