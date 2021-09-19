# NearlestStation
## 概要
住所から最寄り駅を検索します。  
例えば、住所として、”東京タワー”を指定すると、
下記のように最寄り駅が得られます。
```
35.658581 139.745433
3 個の最寄り駅を表示します
赤羽橋 都営大江戸線 430m
神谷町 東京メトロ日比谷線 490m
御成門 都営三田線 620m
```

下記の２つのWEB-APIを利用しています。<br>

| thAPI | th機能 | thLINK |
| :-- | :-: | --: |
| td | 住所から緯度を算出する | https://www.geocoding.jp/api/ |
| td | 最寄り駅名を検索する | http://express.heartrails.com/api/xml |
