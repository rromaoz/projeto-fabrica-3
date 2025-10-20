import streamlit as st

st.set_page_config(page_title="Your Price", layout="centered")

# Minimal CSS for large logo and top nav
st.markdown(
    """
    <style>
    .logo {
        font-family: 'Arial', sans-serif;
        font-size: 56px;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 18px 0 8px 0;
    }
    .subtitle {
        font-size:14px;
        color: #444;
        margin-bottom: 18px;
    }
    .nav {
        display:flex;
        gap:20px;
        padding: 10px 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 18px;
    }
    .nav a {
        text-decoration: none;
        color: #222;
        font-weight:600;
    }
    .card {
        padding: 14px;
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Top navigation with tabs
tabs = st.tabs(["Início", "Comparar preços"])

# ==================== Página Início ====================
with tabs[0]:
    st.markdown('<div class="logo">Your Price</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Comparador minimalista para decidir onde comprar mais barato o mesmo produto.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="nav">
            <a href="#inicio">Início</a>
            <a href="#comparar">Comparar preços</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### Como usar
        - Clique na aba "Comparar preços".
        - Digite o nome do produto e os preços nos três mercados (Walmart, Carrefour, Pão de Açúcar).
        - **Importante:** não haverá limpeza de string nem formatação de moeda — digite os preços como *float* usando ponto (ex.: 27.90).
        """
    )

# ==================== Página Comparar preços ====================
with tabs[1]:
    st.markdown('<div class="logo">Your Price</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Comparar preços entre Walmart, Carrefour e Pão de Açúcar</div>',
        unsafe_allow_html=True,
    )

    with st.form(key="compare_form"):
        produto = st.text_input("Nome do produto")
        st.markdown("**Digite os preços como float usando ponto (ex.: 27.90).**")

        w_text = st.text_input("Walmart - preço (float, use ponto)")
        c_text = st.text_input("Carrefour - preço (float, use ponto)")
        p_text = st.text_input("Pão de Açúcar - preço (float, use ponto)")

        submitted = st.form_submit_button("Comparar")

    if submitted:
        errors = []
        try:
            w = float(w_text)
        except Exception:
            errors.append("Walmart: valor inválido. Digite um float com ponto.")
        try:
            c = float(c_text)
        except Exception:
            errors.append("Carrefour: valor inválido. Digite um float com ponto.")
        try:
            p = float(p_text)
        except Exception:
            errors.append("Pão de Açúcar: valor inválido. Digite um float com ponto.")

        if not produto:
            errors.append("Nome do produto está vazio.")

        if errors:
            st.error("\n".join(errors))
        else:
            st.markdown("### Resultado")
            st.markdown(f"Produto: {produto}")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("**Walmart**")
                st.write(w)
            with col2:
                st.markdown("**Carrefour**")
                st.write(c)
            with col3:
                st.markdown("**Pão de Açúcar**")
                st.write(p)

            prices = {"Walmart": w, "Carrefour": c, "Pão de Açúcar": p}
            min_price = min(prices.values())
            cheapest = [k for k, v in prices.items() if v == min_price]

            if len(cheapest) == 1:
                st.success(f"O menor preço é em {cheapest[0]}: {min_price}")
                diffs = {k: (v - min_price) for k, v in prices.items() if v != min_price}
                if diffs:
                    st.markdown("Diferença em relação ao menor preço:")
                    for k, d in diffs.items():
                        st.write(f"{k}: {d}")
            else:
                st.info("Há um empate nos menores preços entre: " + ", ".join(cheapest))
    else:
        st.info('Preencha os preços e clique em "Comparar".')

st.markdown("---")
st.markdown("Made with minimal design — Your Price")

