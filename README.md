閉めルンです
====

![S__163815430 (2)](https://user-images.githubusercontent.com/48121881/77843198-d1336300-71d5-11ea-8d9c-aa0ea4339d8f.jpg)

## Description

ID・パスワードを渡すと鍵を自動で解錠してくれるWEBアプリ

(A web application that automatically unlocks the key when you pass your ID and password)

## Function

・IDとパスワードをデータベース上の値と照合し、値が正しければArduino経由でサーボモータを回転させ、鍵を解除する。その際に、データベースに登録されたメールアドレスに通知メールを送信する。

(You can unlock the key and get the notification by Gmail if you enter your ID and password.)
<br>

・サーボモータの回転状態を取得しておくことで、ページ上のボタンを押すと鍵が閉まっているか確認できる。
<br>
(You can check if the key is locked by pressing a button.)

<br>
・IDを忘れた場合は登録済みのメールアドレスを入力すると、メールでパスワード通知をしてくれる。

(When you forget your ID, you can get it by entering your registered Gmail adress.)

## Demo

https://www.slideshare.net/secret/GcZBZEwwJ8iReY

<br>
デモ動画① (スライド16)：https://youtu.be/yPeY-DcyLYs
<br>
デモ動画② (スライド17)：https://youtu.be/7T0FOpfCuQI
<br>
デモ動画③ (スライド18)：https://youtu.be/a-9NaD4W4_Q

## Requirement

・Python 3.x

#### ハード機構
・サーボモータ

・ドアスイッチ

・導線

(・Arduino)

## Install

・Flask 1.1.1

(You can get by 'pip install flask==1.1.1')

・SQLAlchemy

(You can get by 'pip install sqlalchemy')

## Author

・[tkyawa](https://github.com/tkyawa) : In charge of Hardware

・[tehhuu](https://github.com/tehhuu) : In charge of Software
