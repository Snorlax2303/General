import json
import argparse
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name('data.json')

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'employees': [], 'vacations': []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_employee(name):
    data = load_data()
    next_id = (max([e['id'] for e in data['employees']] or [0]) + 1)
    data['employees'].append({'id': next_id, 'name': name})
    save_data(data)
    print(f'Funcionário {name} adicionado com id {next_id}')

def list_employees():
    data = load_data()
    for e in data['employees']:
        print(f"{e['id']}: {e['name']}")

def add_vacation(emp_id, start, end):
    data = load_data()
    employee = next((e for e in data['employees'] if e['id'] == emp_id), None)
    if not employee:
        print('Funcionário não encontrado')
        return
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    data['vacations'].append({'emp_id': emp_id, 'start': start, 'end': end})
    save_data(data)
    print(f'Férias registradas para {employee["name"]} de {start} até {end}')

def list_vacations(emp_id=None):
    data = load_data()
    vacations = data['vacations']
    if emp_id:
        vacations = [v for v in vacations if v['emp_id'] == emp_id]
    for v in vacations:
        emp = next((e for e in data['employees'] if e['id'] == v['emp_id']), None)
        name = emp['name'] if emp else 'Desconhecido'
        print(f"{name}: {v['start']} -> {v['end']}")

def main():
    parser = argparse.ArgumentParser(description='Sistema de controle de férias')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list_employees')

    add_emp = subparsers.add_parser('add_employee')
    add_emp.add_argument('name')

    add_vac = subparsers.add_parser('add_vacation')
    add_vac.add_argument('emp_id', type=int)
    add_vac.add_argument('start')
    add_vac.add_argument('end')

    list_vac = subparsers.add_parser('list_vacations')
    list_vac.add_argument('--emp_id', type=int)

    args = parser.parse_args()

    if args.command == 'add_employee':
        add_employee(args.name)
    elif args.command == 'list_employees':
        list_employees()
    elif args.command == 'add_vacation':
        add_vacation(args.emp_id, args.start, args.end)
    elif args.command == 'list_vacations':
        list_vacations(args.emp_id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
