# インポート定義
from playwright.sync_api import sync_playwright

# run関数
def run():
    # sync_playwrightをpという名称インスタンス化（with句によりコンテキストマネージャされ、自動的に破棄される）
    with sync_playwright() as p:
        # Chromiumブラウザを起動
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 指定したURLにアクセス
        page.goto('https://friendsspring.essay.jp/laravel_subquery/')

        # ページタイトルを取得して表示
        print("Page Title:", page.title())

        # ページ内の任意の要素を取得
        heading = page.query_selector('h1')
        if heading:
            print("Heading Text:", heading.inner_text())
        else:
            print("Heading not found")

        # スクリーンショットを撮る
        page.screenshot(path='screenshot.png')

        # ブラウザを閉じる
        browser.close()

# 直接実行された場合にだけ実行される
if __name__ == "__main__":
    run()