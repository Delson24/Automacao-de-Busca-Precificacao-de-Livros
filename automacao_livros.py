"""
Automa√ß√£o de Busca de Livros
Busca livros no Project Gutenberg e Books to Scrape
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time


def pesquisar_gutenberg(nome, autor, navegador):
    """Pesquisa livro no Project Gutenberg"""
    lista_palavras_autor = autor.split(" ")
    navegador.get("https://www.gutenberg.org/ebooks/search/?query=")
    
    try:
        campo_busca = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-input"))
        )
        campo_busca.send_keys(nome)
        campo_busca.send_keys(Keys.ENTER)
        time.sleep(2)
        
        lista_de_resultados = navegador.find_elements(By.CLASS_NAME, "booklink")
        link = None
        
        for resultado in lista_de_resultados:
            texto = resultado.text
            if nome.lower() in texto.lower():
                if all(palavra in texto for palavra in lista_palavras_autor):
                    link = resultado.find_element(By.CLASS_NAME, "link").get_attribute("href")
                    break
        
        preco = 0 if link else None
            
    except Exception as e:
        print(f"Erro no Gutenberg: {e}")
        link = None
        preco = None
    
    return link, preco


def pesquisar_books_toscrape(nome, autor, categoria, navegador):
    """Pesquisa livro no Books to Scrape"""
    navegador.get("https://books.toscrape.com/")
    time.sleep(2)
    
    try:
        navegador.find_element(By.LINK_TEXT, categoria.title()).click()
        time.sleep(2)
    except:
        print(f"Categoria '{categoria}' n√£o encontrada, buscando em todas")
    
    link = None
    preco = None
    encontrado = False
    
    while not encontrado:
        lista_de_resultados = navegador.find_elements(By.CLASS_NAME, "product_pod")
        
        for resultado in lista_de_resultados:
            try:
                elemento_h3 = resultado.find_element(By.TAG_NAME, "h3")
                elemento_do_link = elemento_h3.find_element(By.TAG_NAME, "a")
                titulo = elemento_do_link.get_attribute("title")
                
                if nome.lower() in titulo.lower():
                    encontrado = True
                    link = elemento_do_link.get_attribute("href")
                    preco = resultado.find_element(By.CLASS_NAME, "price_color").text
                    break
            except:
                continue
        
        if not encontrado:
            try:
                botao_next = navegador.find_element(By.LINK_TEXT, "next")
                botao_next.click()
                time.sleep(2)
            except:
                break
    
    return link, preco


def main():
    """Fun√ß√£o principal"""
    print("Ìºê Iniciando navegador...")
    navegador = webdriver.Chrome()
    
    print("Ì≥Ç Carregando lista de produtos...")
    df_produtos = pd.read_excel('produtos.xlsx')
    
    # Configurar colunas
    df_produtos['preco'] = df_produtos['preco'].astype('object')
    df_produtos['link'] = df_produtos['link'].astype('object')
    
    print(f"Ì∫Ä Processando {len(df_produtos)} livros\n")
    
    for linha in df_produtos.index:
        nome = df_produtos.loc[linha, "nome"]
        autor = df_produtos.loc[linha, "autor"]
        categoria = df_produtos.loc[linha, "categoria"]
        
        print(f"\n{'='*70}")
        print(f"Ì≥ö Livro {linha + 1}/{len(df_produtos)}: {nome}")
        print(f"{'='*70}")
        
        try:
            # Buscar no Gutenberg
            print("Ì¥é Buscando no Gutenberg...")
            link1, preco1 = pesquisar_gutenberg(nome, autor, navegador)
            
            if link1:
                print(f"‚úÖ Encontrado no Gutenberg (Gratuito)")
                df_produtos.loc[linha, "preco"] = 0
                df_produtos.loc[linha, "link"] = link1
            else:
                print("Ì¥é Buscando no Books to Scrape...")
                link2, preco2 = pesquisar_books_toscrape(nome, autor, categoria, navegador)
                
                if link2:
                    print(f"‚úÖ Encontrado ({preco2})")
                    df_produtos.loc[linha, "preco"] = preco2
                    df_produtos.loc[linha, "link"] = link2
                else:
                    print("‚ùå N√£o encontrado")
                    df_produtos.loc[linha, "preco"] = "N√£o encontrado"
                    df_produtos.loc[linha, "link"] = "N√£o encontrado"
            
            df_produtos.to_excel("produtosAtualizados.xlsx", index=False)
            print(f"Ì≤æ Progresso salvo ({linha + 1}/{len(df_produtos)})")
            
        except Exception as e:
            print(f"Ì∫® Erro: {e}")
            df_produtos.loc[linha, "preco"] = "ERRO"
            df_produtos.loc[linha, "link"] = "ERRO"
    
    print("\nÌæâ Automa√ß√£o conclu√≠da!")
    navegador.quit()


if __name__ == "__main__":
    main()
