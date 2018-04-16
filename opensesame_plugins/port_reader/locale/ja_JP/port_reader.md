# Port_reader Plugin: ポート読み取りプラグイン

port_readerプラグインは、パラレルポートまたはシリアルポートなどの任意のポートから入力を読み取り、戻り値を参加者の応答(ボタン押下など)として解釈します。

- **Dummy mode (ダミーモード)** -- 'yes'が選択されている場合、代わりにキーボードが使用されます。開発段階で役立ちます。
- **Port number (ポート番号)** -- 使用したいポート番号
- **Resting-state value (無入力状態値)** -- 無入力(ボタンが謳歌されていない)状態における入力値
- **Correct response (正しい応答)** -- 予期される応答
- **Timeout (タイムアウト)** -- 最大応答時間。その後、
タイムアウトを通知する必要があります。