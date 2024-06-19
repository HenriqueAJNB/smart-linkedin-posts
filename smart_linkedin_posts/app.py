from pathlib import Path

from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings

if __name__ == "__main__":
    load_dotenv()
    project_root = Path(__file__).parent[1]
    post_history_csv_filepath = project_root / "data" / "shares.csv"

    loader = CSVLoader(
        file_path=post_history_csv_filepath,
        encoding="utf8",
        source_column="ShareCommentary",  # Nome da coluna no arquivo CSV com o conteúdo dos posts
    )
    docs = loader.load()

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embedding=embeddings)

    model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.8)

    # Prompt template
    prompt = ChatPromptTemplate.from_template("""
    Escreva um post para o LinkedIn para atrair o máximo possível de pessoas engajando e compartilhando.
    Use as minhas mensagens anteriores como contexto para extrair somente o tom e forma de escrita.
    Retorne também o tom usado na mensagem criada.
    Traga exemplos para o tema proposto.
    Contexto: {context}
    Tema: {input}
    """)

    # Criação do chain
    # chain = prompt | llm
    chain = create_stuff_documents_chain(llm=model, prompt=prompt)

    retriever = vector_store.as_retriever(search_kwargs={"k": 15})

    retrieval_chain = create_retrieval_chain(
        retriever=retriever, combine_docs_chain=chain
    )
    theme = input("Digite um tema para gerar um post sobre ele: ")
    response = retrieval_chain.invoke({"input": theme})
    print("Sugestão de post:\n\n")
    print(response["answer"])
