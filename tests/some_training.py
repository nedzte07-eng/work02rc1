from playwright.sync_api import sync_playwright

def demo_auto_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Переходимо на сторінку з динамічним завантаженням
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        print("Натискаємо кнопку Start...")
        # Натискаємо кнопку для початку завантаження
        page.locator("button").click()

        print("Очікуємо появи тексту...")
        # Playwright автоматично чекає, поки текст стане видимим
        # Це займе кілька секунд, але нам не потрібно писати явні очікування
        text_element = page.locator("#finish h4")

        # Перевіряємо, що текст з'явився
        assert text_element.text_content() == "Hello World!"
        print("Текст з'явився! Тест пройдено успішно.")

        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    demo_auto_wait()