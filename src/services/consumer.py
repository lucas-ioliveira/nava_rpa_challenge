from pathlib import Path
from datetime import datetime

from decouple import config
from playwright.sync_api import sync_playwright

from src.services.handler import Handler
from src.utils.logger import get_logger


class Consumer:

    def __init__(self):
        self.handler = Handler()
        self.logger = get_logger(__name__)
        self.url = config('RPA_CHALLENGE_URL')
        self.folder_screenshot = Path("src/screenshots")
    
    def fill_out_the_web_form(self):
        self.logger.info("Iniciando a automação web para preenchimento do formulário.")

        try:
            people = self.handler.read_file()
            if not people:
                self.logger.warning('Não foram encontrados dados para serem processados.')
                return

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False) 
                page = browser.new_page()
                page.goto(self.url)

                page.get_by_role("button", name="Start").click()

                for item in people:
                    try:
                        page.locator("label").filter(has_text="First Name").locator("..").locator("input").fill(item['first_name'])
                        page.locator("label").filter(has_text="Last Name").locator("..").locator("input").fill(item['last_name'])
                        page.locator("label").filter(has_text="Company Name").locator("..").locator("input").fill(item['company_name'])
                        page.locator("label").filter(has_text="Role in Company").locator("..").locator("input").fill(item['role_in_company'])
                        page.locator("label").filter(has_text="Address").locator("..").locator("input").fill(item['address'])
                        page.locator("label").filter(has_text="Email").locator("..").locator("input").fill(item['email'])
                        page.locator("label").filter(has_text="Phone Number").locator("..").locator("input").fill(str(item['phone_number']))

                        page.get_by_role("button", name="Submit").click()
                        self.logger.info(f"Preenchimento para a pessoa: {item['first_name']} {item['last_name']} referente a empresa: {item['company_name']} - OK")

                    except Exception as e:
                        self.logger.exception(f"Preenchimento para a pessoa: {item['first_name']} {item['last_name']} referente a empresa: {item['company_name']} - NOK")
                        continue

                page.locator("text=Congratulations").wait_for(timeout=10000) 

                self.folder_screenshot.mkdir(parents=True, exist_ok=True)
                date_screenshot = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                path_screenshot = self.folder_screenshot / f"result_{date_screenshot}.png"

                page.screenshot(path=path_screenshot, full_page=True)

                self.logger.info(f"Screenshot salvo com sucesso em: {path_screenshot}")
                self.logger.info("Automação finalizada.")
                browser.close()

        except Exception as e:
            self.logger.exception(f'Erro global, detalhes: {e}')
            return
