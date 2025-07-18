import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            list_dic = []
            for obj in clientes:
                dic_cliente = obj.__dict__.copy()
                if "senha" in dic_cliente:
                    del dic_cliente["senha"]
                list_dic.append(dic_cliente)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        if st.button("Cadastrar"):
            try:
                View.cliente_inserir(nome, email, "1234", fone)
                st.success("Cliente inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)    
                time.sleep(2)
                st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", clientes)
            nome = st.text_input("Informe o novo nome", op.getNome())
            email = st.text_input("Informe o novo e-mail", op.getEmail())
            fone = st.text_input("Informe o novo fone", op.getFone())
            if st.button("Atualizar"):
                try:
                    View.cliente_atualizar(op.getId(), nome, email, op.getSenha(), fone)
                    st.success("Cliente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)    
                    time.sleep(2)
                    st.rerun()

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de cliente", clientes)
            if st.button("Excluir"):
                try:
                    View.cliente_excluir(op.getId())
                    st.success("Cliente excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(f"Erro: {erro}")
                    time.sleep(2)
                    st.rerun()

    def listarCompras():
        st.header("Minhas Compras")
        vendas = View.listar_carrinhos_finalizados(st.session_state["cliente_id"])
        if len(vendas) == 0:
            st.write("Nenhuma compra foi realizada ainda.")
        else:
            df = pd.DataFrame(vendas)
            st.dataframe(df)