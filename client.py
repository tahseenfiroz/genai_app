from src.model import embedding
from src.data import data_raw
from src.database import shared
# import streamlit as st

df_raw = data_raw.data_raw()
# df_raw['question_embedding'] = df_raw['question]'.apply(embedding.get_embeddings)
df_raw['question_embedding'] = df_raw['question'].apply(embedding.get_embeddings)
df_raw['answer_embedding'] = df_raw['answer'].apply(embedding.get_embeddings)
shared.pgv_truncate('app_semantic','player')
shared.pgv_insert(df_raw,'app_semantic','player')
df = shared.pgv_semantic_search('who is Kohli', 'app_semantic', 'player', 'question_embedding')
print(1)
# # Initialize st.session_state.beans
# st.session_state.beans = st.session_state.get("beans", 0)
#
# st.title("Bean counter :paw_prints:")




addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):


    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")

print(1)

