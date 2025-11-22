#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clinica Vida+ — App de Console
Recursos: cadastro de pacientes, estatísticas, busca, listagem
Requisitos: Python 3.8+
"""

from typing import List, Dict

Paciente = Dict[str, str]  # nome(str), telefone(str), idade(int como str internamente)

def _input_nao_vazio(rotulo: str) -> str:
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print("⚠ Campo obrigatório. Tente novamente.")

def _input_int(rotulo: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        entrada = input(rotulo).strip()
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"⚠ Valor mínimo é {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠ Valor máximo é {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠ Informe um número inteiro válido.")

def cadastrar_paciente(pacientes: List[Paciente]) -> None:
    print("\n=== Cadastro de Paciente ===")
    nome = _input_nao_vazio("Nome completo: ")
    idade = _input_int("Idade (em anos): ", minimo=0, maximo=130)
    telefone = _input_nao_vazio("Telefone (ex: 21 99999-0000): ")
    pacientes.append({"nome": nome, "idade": str(idade), "telefone": telefone})
    print(f"✅ Paciente '{nome}' cadastrado com sucesso!\n")

def ver_estatisticas(pacientes: List[Paciente]) -> None:
    print("\n=== Estatísticas ===")
    if not pacientes:
        print("Não há pacientes cadastrados.\n")
        return

    idades = [int(p["idade"]) for p in pacientes if p.get("idade")]
    if not idades:
        print("Não há idades válidas cadastradas.\n")
        return

    total = len(pacientes)
    media = sum(idades) / len(idades)
    mais_novo = min(idades)
    mais_velho = max(idades)

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f} anos")
    print(f"Mais novo: {mais_novo} anos")
    print(f"Mais velho: {mais_velho} anos\n")

def buscar_por_nome(pacientes: List[Paciente], termo: str) -> List[Paciente]:
    termo = termo.strip().lower()
    return [p for p in pacientes if termo in p.get("nome","").lower()]

def acao_busca(pacientes: List[Paciente]) -> None:
    print("\n=== Buscar por nome ===")
    termo = _input_nao_vazio("Digite parte do nome: ")
    achados = buscar_por_nome(pacientes, termo)
    if not achados:
        print("Sem resultados.\n")
        return
    for i, p in enumerate(achados, 1):
        print(f"{i}. {p['nome']} — {p['idade']} anos — {p['telefone']}")
    print()

def listar_pacientes(pacientes: List[Paciente]) -> None:
    print("\n=== Lista de Pacientes (ordenada por nome) ===")
    if not pacientes:
        print("Não há pacientes cadastrados.\n")
        return
    for i, p in enumerate(sorted(pacientes, key=lambda x: x.get("nome","").lower()), 1):
        print(f"{i}. {p['nome']} — {p['idade']} anos — {p['telefone']}")
    print()

def menu():
    pacientes: List[Paciente] = []
    opcoes = {
        "1": ("Cadastrar paciente", lambda: cadastrar_paciente(pacientes)),
        "2": ("Ver estatísticas", lambda: ver_estatisticas(pacientes)),
        "3": ("Buscar por nome", lambda: acao_busca(pacientes)),
        "4": ("Listar pacientes", lambda: listar_pacientes(pacientes)),
        "5": ("Sair", None),
    }

    while True:
        print("=== Clínica Vida+ ===")
        for k, (titulo, _) in opcoes.items():
            print(f"{k} - {titulo}")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "5":
            print("Encerrando... Até logo!")
            break
        if escolha in opcoes:
            try:
                acao = opcoes[escolha][1]
                if acao:
                    acao()
            except Exception as exc:
                print(f"⚠ Ocorreu um erro inesperado: {exc}")
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
