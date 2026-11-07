# Ver.4.0.7 — 敵ウェーブ方向指定エラー修正

無名都市の包囲ウェーブで方向番号が4〜6となり、存在しない方向を参照して「side is not a function or its return value is not iterable」が発生していたため、0〜3の範囲に正規化しました。6ウェーブ構成・進化・難易度・セーブ形式は変更していません。

# Ver.4.0.6 — 無名都市パイロット改修 / GitHub Pages対応

## 今回の試作変更

- **無名都市のみ**、敵撃破の経験値を自動加算せず、青い結晶としてドロップさせる。近寄ると吸い寄せられ、拾うと経験値になる。勧誘・エリア移動報酬は従来どおり。
- 無名都市に時間・攻略エリアで変化する敵ウェーブを追加。包囲・両側からの挟撃・集中突入を組み合わせる。ほかの舞台の出現ロジックは維持。
- 無名都市の7エリアそれぞれの広さと床材、石造建築オブジェクトの配置を変更。実際の衝突判定にも反映。
- 無名都市に限り、上位信者の通常攻撃倍率と2回攻撃ごとの範囲波及を試験的に強化。ほかの舞台は従来値を維持。
- 既存セーブキー・モードとステージ別の難易度解放・GitHub Pages構成を維持。

**範囲**: 無名都市の戦闘ループを試す検証版です。他4舞台のアート全面改修、全キャラ新規ドット絵、長時間の実戦バランス調整は未完了です。地形素材は旧ドット絵の質感を保ちながら再着彩した統一素材を使用しています。

# マレモン・サバイバーズ — GitHub Pages公開版 Ver.4.0.5

このフォルダの中身を **GitHubリポジトリ直下** に配置し、GitHub Pagesとして公開します。ビルドツールやNode.jsは不要です。ZIPそのものをGitHubへ置くだけでは動きません。ZIPを**解凍して**、ファイルとフォルダを登録してください。

## 最も簡単な公開手順
1. GitHubに新しいリポジトリを作成（例：`maremon-survivors`）。公開サイトになるため、公開可能な画像・音源だけを含めてください。
2. 本ZIPを解凍。`index.html`、`game.js`、`styles.css`、`assets/`、`sfx/`、`music/`、`.github/workflows/deploy-pages.yml`、`tools/` などを、**フォルダ構造を維持**してリポジトリ直下に置きます。Gitのデスクトップクライアントを使うとフォルダと多数のファイルを安全に反映できます。
3. `main`（または `master`）にコミットしてプッシュします。
4. GitHub → リポジトリの **Settings → Pages → Build and deployment → Source: GitHub Actions** を選びます。
5. **Actions → Deploy Maremon Survivors to GitHub Pages** の成功を確認。`https://<ユーザー名>.github.io/<リポジトリ名>/` からプレイできます（URLは例です）。

## データ配置
```
index.html
game.js    # 実装本体（バージョン管理しやすい独立ファイル）
styles.css # UIデザイン
.nojekyll
.github/workflows/deploy-pages.yml
assets/    # ドット絵、地形、キャラ、攻撃画像
sfx/       # SE
music/     # BGM（オプション・別パックで追加可能）
tools/check_assets.py
README.md
```

ページは `index.html` を起点として、`assets/` / `sfx/` / `music/` を**相対パス**で参照します。独自ドメイン・`<ユーザー名>.github.io/リポジトリ名` のどちらでも同じデータ構造で動作します。

## BGM別パック運用
軽量版から公開する場合は、`index.html`、`game.js`、`styles.css` と `assets/`、`sfx/`、`.github/`、`tools/` を配置すれば、BGMなしでプレイできます。後から `music/` に16曲のMP3を追加するとBGMが使えます。日本語MP3名は**変更しない**でください。

## セーブデータについて
- GitHub Pagesでもブラウザ内保存・JSON書き出し/読み込みを利用できます。
- **ローカルファイル起動版とGitHub Pages版のブラウザ保存領域は別**です。旧版の保存データを引き継ぐ場合は、旧版からJSONをエクスポートし、公開ページ側でインポートしてください。
- ブラウザによっては保存先ファイルへの自動上書きが使えないため、JSONのバックアップを推奨します。

## 更新手順
`game.js`・`styles.css`・`index.html` と変わったアセットのみ上書きして `main` にプッシュすると、GitHub Actionsで自動公開されます。ページ更新後に古い画像が出る場合はブラウザを強制再読み込みしてください。

## GitHub Pagesに関する注意
- GitHub Pagesは静的配信サービスです。ログイン/対戦同期/ランキングなどサーバー機能は含まれません。
- サイトが公開されると、画像・BGM・ソースは基本的に誰でも参照できます。利用許諾を確認してください。
- GitHub Pagesへの公開はまだ行っていません。このZIPは**公開の準備が整ったファイル一式**です。
- GitHub Pages公開設定の詳細: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
