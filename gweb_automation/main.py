from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="ANA ALVES DOS SANTOS ARAUJO 83228047172").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #("equilibriocontab.diretoria@gmail.com")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Café Baguaçú")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

    from playwright.sync_api import Playwright, sync_playwright, expect





def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="JOAQUIM JUNIOR GONCALVES 22950223800").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@dataconcontabil.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Joaquim Ferro e Máquinas")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

    from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="JOAQUIM JUNIOR GONCALVES 22950223800").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@dataconcontabil.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Joaquim Ferro e Máquinas")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


    from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="MAICON DA SILVA CAMPOS - ME").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@dataconcontabil.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Churros da Praça")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/")
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="ALDERICO PARDINI MERCEARIA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("escritafiscal@martinezcontabil.com.br")
    page.get_by_label("Nome").click(modifiers=["Control"])
    page.get_by_label("Nome").fill("Mercearia São Pedro")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("Nome").click()
    page.get_by_label("Nome").fill("Mercearia São Pedro")
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("escritafiscal@martinezcontabil.com.br")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="ZILDETE OTTANI").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@dataconcontabil.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("MZ RECICLAGEM")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="LARISSA GATTI BARBOZA DE SOUZA LTDA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscalgonsales@gmail.com")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("J. Marques Aambientes Planejados")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="J C DE O MARQUES EIRELI").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@onixcontabeis.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("J. Marques Aambientes Planejados")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="RB DIST E REPRES DE PRODUTOS HOSPITALARES LTDA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@onixcontabeis.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Rb Insumos Hospitalares")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="ALEXANDRE VICENTE DO NASCIMENTO ENERGIA FOTOVOLTAICA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("carlos@escritorioipiranga.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("SA Energia Fotovoltaica")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="CAMILA CARLA DE ANDRADE LOPES 38385976809").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("carlos@escritorioipiranga.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("Zanini Distribuidora de Congelados")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/")
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="MARIA ANTONIETA DA FONSECA ALVES").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("escritafiscal@martinezcontabil.com.br")
    page.get_by_label("Nome").click(modifiers=["Control"])
    page.get_by_label("Nome").fill("Bazar Progresso")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("Nome").click()
    page.get_by_label("Nome").fill("Bazar Progresso")
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("escritafiscal@martinezcontabil.com.br")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="MAURILIO DE ARIMATEIA 26969809854").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("carlos@escritorioipiranga.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("MAURILIO DE ARIMATEIA")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="VILSON PEREIRA MINIMERCADO").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("fiscal@onixcontabeis.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("VILSON")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="A J COMERCIO DE AGUA E GAS LTDA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="PDV").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("datacon@terra.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("A J COMERCIO DE AGUA E GAS LTDA")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.gdoorweb.com.br/login")
    page.get_by_label("E-mail *").fill("suporte3.excelent@gmail.com")
    page.get_by_label("E-mail *").press("Enter")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").press("CapsLock")
    page.get_by_label("Senha *").fill("parceria94@")
    page.get_by_label("Senha *").press("Enter")
    page.get_by_role("heading", name="DISTRIBUIDORA DE LUBRIFICANTES MARIN LTDA").click()
    page.get_by_role("button", name="Movimentações").click()
    page.get_by_role("link", name="NF-e").click()
    page.get_by_role("heading", name="XML do mês").click()
    page.get_by_text("Enviar por e-mail").click()
    page.get_by_label("E-mail *").click()
    page.get_by_label("E-mail *").fill("suporte6.excelent@gmail.com")
    #page.get_by_label("E-mail *").fill("datacon@terra.com.br")
    page.get_by_label("E-mail *").press("Tab")
    page.get_by_label("Nome").fill("DISTRIBUIDORA DE LUBRIFICANTES MARIN LTDA")
    page.get_by_role("button", name="Confirmar").click()
    page.get_by_role("button", name="Ok").press("Enter")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import Playwright, sync_playwright, expect










    