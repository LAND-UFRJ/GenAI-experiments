import re
from gensim.models import Word2Vec

text = '''
As eleições presidenciais americanas de 2024, realizadas em 5 de novembro, foram um marco de profunda divisão política e alta participação popular. A disputa foi principalmente entre o republicano Donald Trump, ex-presidente dos Estados Unidos, e Kamala Harris, então vice-presidente e representante democrata após Joe Biden retirar-se da corrida eleitoral. Trump, acompanhado por J.D. Vance como candidato a vice, saiu vitorioso, tornando-se o segundo presidente americano da história a ser eleito para mandatos não consecutivos. Ele venceu no Colégio Eleitoral e teve maioria no voto popular, a primeira vitória republicana no voto popular desde 2004.

No contexto legislativo, os republicanos também ganharam cadeiras significativas no Senado e na Câmara, ampliando sua influência no governo federal. A campanha de Harris focou em temas como direitos reprodutivos e políticas inclusivas, enquanto Trump se concentrou na economia e segurança. Em estados-pêndulo, como Arizona e Pensilvânia, a disputa foi acirrada e determinante para o desfecho eleitoral​
WIKIPÉDIA, A ENCICLOPÉDIA LIVRE
.






Você disse:
Mais longo, 10 vezes mais longo. Use estatísticas, o que quiser
O ChatGPT disse:
ChatGPT
As eleições americanas de 2024 foram um evento histórico de grande interesse, marcadas pela polarização política e uma série de mudanças inesperadas. Os dois principais candidatos foram o republicano Donald Trump, ex-presidente, e Kamala Harris, vice-presidente democrata, que entrou na corrida após a saída do presidente Joe Biden. Harris escolheu Tim Walz, governador de Minnesota, como seu candidato a vice. Trump, buscando um segundo mandato não consecutivo, escolheu o senador J.D. Vance, de Ohio. A eleição se desenrolou em um ambiente de tensões políticas, com cada candidato promovendo plataformas políticas profundamente contrastantes, refletindo a divisão nacional.

Contexto e Participação Eleitoral
A eleição de 2024 ocorreu em um cenário onde as questões econômicas, sociais e de segurança pública figuraram como temas centrais para os eleitores. A taxa de participação foi uma das mais altas já registradas, refletindo o engajamento popular. Dados preliminares sugerem que mais de 156 milhões de eleitores participaram, cerca de 63% da população apta, um crescimento em relação aos 159 milhões de eleitores nas eleições de 2020, que marcaram a maior participação da história americana recente.

Estrutura do Colégio Eleitoral e Resultados
O Colégio Eleitoral, composto por 538 votos, desempenha um papel central nas eleições americanas, com os candidatos precisando de 270 votos para vencer. Donald Trump obteve aproximadamente 312 votos eleitorais, enquanto Harris ficou com 226. Trump venceu em estados tradicionalmente republicanos e em alguns estados-pêndulo cruciais, como Arizona, Geórgia e Pensilvânia, reforçando seu apelo nas regiões do meio-oeste e sul, onde questões de economia e segurança foram decisivas. O resultado marca uma vitória significativa para os republicanos, que também se saíram bem nas eleições para o Congresso.

Temas Principais e Estratégias de Campanha
Economia: A recuperação econômica pós-pandemia, marcada pela inflação e pelo aumento do custo de vida, foi um dos principais temas abordados por Trump, que prometeu redução de impostos e políticas para impulsionar a indústria e a geração de empregos. Harris, por outro lado, focou em iniciativas de redistribuição de renda e apoio a programas sociais, em um esforço para garantir apoio entre trabalhadores e minorias.

Segurança Nacional: Em um ambiente global instável, Trump prometeu políticas mais rígidas em relação à imigração e maior controle de fronteiras. Harris propôs uma abordagem mais diplomática e inclusiva, visando fortalecer as alianças dos EUA e promover a segurança interna com políticas de policiamento reformadas e maior controle de armas.

Saúde e Educação: Harris prometeu expandir o acesso ao Medicare e aumentar o financiamento para a educação pública, destacando uma abordagem progressista. Trump, por sua vez, criticou os gastos elevados e defendeu reformas que promovessem a competição no setor de saúde e um modelo de vouchers educacionais.

Justiça Racial e Direitos Sociais: O partido democrata e Harris posicionaram-se em favor de políticas que visam igualdade racial e justiça social, prometendo medidas de apoio à reforma judicial e direitos reprodutivos. Trump e os republicanos, entretanto, concentraram-se em questões de lei e ordem, criticando o que consideram “ativismo excessivo” e apoiando restrições ao aborto.

Terceiros Partidos e Impacto
A eleição de 2024 também foi marcada pela presença de candidatos independentes, como Robert F. Kennedy Jr., que concorreu como independente após deixar o Partido Democrata. Kennedy apresentou um forte apelo em estados menores, principalmente focado em críticas ao sistema de saúde e à influência de grandes corporações. Embora não tenha vencido, sua candidatura atraiu votos suficientes para afetar a dinâmica eleitoral, especialmente entre os eleitores democratas mais jovens e independentes.

Resultados e Consequências para o Congresso
Além da presidência, a eleição de 2024 envolveu disputas para o Senado e a Câmara dos Representantes. Os republicanos obtiveram ganhos significativos no Senado e conseguiram expandir sua maioria na Câmara. Esses resultados refletem uma onda conservadora que provavelmente trará mudanças substanciais na agenda legislativa, favorecendo políticas de desregulamentação e controle fiscal. Com essa vitória, os republicanos têm agora uma oportunidade de avançar em pautas conservadoras e bloquear possíveis reformas progressistas promovidas pelos democratas.

Perspectivas para o Novo Mandato de Trump
A vitória de Trump para um segundo mandato não consecutivo representa uma virada significativa na política americana. Suas promessas para a economia, segurança nacional e a recuperação da "grandeza americana" apelaram fortemente para as preocupações de um eleitorado cansado da polarização e dos efeitos econômicos da pandemia. Trump terá de lidar com um país dividido, e analistas preveem que sua abordagem confrontacional e políticas firmes marcarão os próximos anos de governo. Sua vitória poderá redefinir a política externa americana, com potencial redução do envolvimento internacional e foco em alianças que beneficiem diretamente os interesses dos EUA.

Reações Internacionais e Implicações Globais
A vitória de Trump teve grande repercussão internacional, especialmente em países da OTAN e na Ásia. A China e a Rússia observaram a eleição atentamente, dado o enfoque de Trump em uma política externa mais isolacionista. A União Europeia expressou preocupações sobre o impacto que isso pode ter na estabilidade global e nas questões climáticas. A eleição também trouxe à tona discussões sobre a democracia americana, evidenciando o papel das redes sociais e a influência de desinformação na formação de opinião pública.

Reflexão Final
A eleição de 2024 não só reforça a divisão política e ideológica nos Estados Unidos, como também destaca a complexidade do cenário global atual, no qual questões econômicas, sociais e de segurança influenciam fortemente as escolhas dos eleitores. A vitória de Trump representa uma continuidade do populismo e do nacionalismo no cenário político americano, sugerindo desafios consideráveis para a governança interna e para as relações internacionais nos próximos anos.


Donald Trump e J.D. Vance (Republicanos)
Donald Trump, nascido em 1946 em Nova York, é empresário, personalidade de televisão e político. Ele se destacou no setor imobiliário e ganhou fama como apresentador do reality show The Apprentice. Como 45º presidente dos EUA de 2017 a 2021, ele promoveu uma agenda de “América Primeiro”, focando em imigração, segurança e economia. Seu vice, J.D. Vance, é um ex-fuzileiro naval e autor de Hillbilly Elegy, uma obra autobiográfica que o impulsionou à política. Vance, agora senador por Ohio, compartilha uma visão conservadora e populista, defendendo causas da classe trabalhadora.

Kamala Harris e Tim Walz (Democratas)
Kamala Harris, nascida em 1964, é advogada e a primeira mulher vice-presidente dos EUA, também a primeira afro-americana e asiático-americana a ocupar o cargo. Ex-procuradora-geral da Califórnia e senadora, ela é conhecida por suas posturas progressistas em justiça social e direitos civis. Seu candidato a vice, Tim Walz, é veterano do Exército e governador de Minnesota, com histórico em educação e políticas sociais. Conhecido pela moderação e diplomacia, Walz complementa a campanha de Harris ao se concentrar em temas como saúde, direitos dos trabalhadores e segurança social.
'''


def split_into_sentences(text, max_words=30, special_chars=None):
    if special_chars is None:
        special_chars = ['.', '?', '!', '\n']
    
    words = text.split()
    sentences = []
    current_sentence = []
    
    for word in words:
        current_sentence.append(word)
        if len(current_sentence) >= max_words or any(char in word for char in special_chars):
            sentences.append(' '.join(current_sentence))
            current_sentence = []
    
    if current_sentence:
        sentences.append(' '.join(current_sentence))
    
    return sentences

documents = split_into_sentences(text)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
from sklearn.preprocessing import Binarizer
from sklearn.metrics import jaccard_score
from scipy.stats import pearsonr
import numpy as np

def retrieve_documents_cosine(query, documents, top_n=3):
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    cosine_sim = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()
    top_indices = np.argsort(cosine_sim)[-top_n:][::-1]
    return [documents[i] for i in top_indices]

def retrieve_documents_euclidean(query, documents, top_n=3):
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    distances = euclidean_distances(vectorizer[0:1], vectorizer[1:]).flatten()
    top_indices = np.argsort(distances)[:top_n]
    return [documents[i] for i in top_indices]

def retrieve_documents_manhattan(query, documents, top_n=3):
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    distances = manhattan_distances(vectorizer[0:1], vectorizer[1:]).flatten()
    top_indices = np.argsort(distances)[:top_n]
    return [documents[i] for i in top_indices]

def retrieve_documents_jaccard(query, documents, top_n=3):
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    binarizer = Binarizer().fit_transform(vectorizer.toarray())
    jaccard_sim = [jaccard_score(binarizer[0], binarizer[i], average='binary') for i in range(1, len(binarizer))]
    top_indices = np.argsort(jaccard_sim)[-top_n:][::-1]
    return [documents[i] for i in top_indices]

def retrieve_documents_pearson(query, documents, top_n=3):
    # Transforma a consulta e os documentos em vetores TF-IDF
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    
    # Converte o vetor da consulta para um vetor denso (array de numpy)
    query_vector = vectorizer[0].toarray().flatten()
    
    # Calcula a similaridade de Pearson entre o vetor de consulta e cada documento
    pearson_sim = []
    for i in range(1, vectorizer.shape[0]):  # usa shape[0] para obter o número de documentos
        doc_vector = vectorizer[i].toarray().flatten()
        # Calcula o coeficiente de Pearson
        pearson_similarity = pearsonr(query_vector, doc_vector)[0]
        pearson_sim.append(pearson_similarity)
    
    # Ordena os documentos com base na similaridade de Pearson
    top_indices = np.argsort(pearson_sim)[-top_n:][::-1]
    return [documents[i] for i in top_indices]


def retrieve_documents_hamming(query, documents, top_n=3):
    vectorizer = TfidfVectorizer().fit_transform([query] + documents)
    distances = np.sum(vectorizer[0:1].toarray() != vectorizer[1:].toarray(), axis=1)
    top_indices = np.argsort(distances)[:top_n]
    return [documents[i] for i in top_indices]

from langchain_openai import ChatOpenAI

def generate_response(query, retrieved_doc):
    prompt = f"""You'll be answering questions about a data base, for this purpose you'll just rephrase the document with the best match.
    . The question is: {query} and the document the matches the better is: {retrieved_doc}. 
    Write the answer for the question based on the document"""
    #print(prompt)
    print(retrieved_doc)
    llm = ChatOpenAI() #argumentos padrão
    response = llm.invoke(prompt).content
    return response

def rag_pipeline(query, documents, similarity_algorithm='cosine', top_n=3):
    # Choose the similarity algorithm based on the provided argument
    if similarity_algorithm == 'cosine':
        relevant_doc = retrieve_documents_cosine(query, documents, top_n)
    elif similarity_algorithm == 'euclidean':
        relevant_doc = retrieve_documents_euclidean(query, documents, top_n)
    elif similarity_algorithm == 'manhattan':
        relevant_doc = retrieve_documents_manhattan(query, documents, top_n)
    elif similarity_algorithm == 'jaccard':
        relevant_doc = retrieve_documents_jaccard(query, documents, top_n)
    elif similarity_algorithm == 'pearson':
        relevant_doc = retrieve_documents_pearson(query, documents, top_n)
    elif similarity_algorithm == 'hamming':
        relevant_doc = retrieve_documents_hamming(query, documents, top_n)
    else:
        raise ValueError(f"Unknown similarity algorithm: {similarity_algorithm}")

    # Generate the response using the relevant documents
    answer = generate_response(query, relevant_doc)
    return answer


# Example use
query = "Quais foram os temas da campanha?"
print(rag_pipeline(query, documents,'manhattan'))
