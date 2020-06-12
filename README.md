閉めルンです
====

![スクリーンショット 2020-06-05 3 06 20](https://user-images.githubusercontent.com/48121881/83794928-b0a5ee80-a6d9-11ea-88e6-b2ee08a95fab.png)

## Description

ID・パスワードを渡すと鍵を自動で解錠し、メールで通知してくれるWEBアプリ

(A web application that automatically unlocks the key and notify it by Gmail when you enter your ID and password)

## Function

・IDとパスワードをデータベース上の値と照合し、値が正しければArduino経由でサーボモータを回転させ、鍵を解除する。その際に、データベースに登録されたメールアドレスに通知メールを送信する。
<br>
(You can unlock the key and get the notification by Gmail if you enter your ID and password.)
<br>

・ページ上のボタンを押すと、ドアスイッチ上の電流状態から鍵が閉まっているか確認し、表示する。
<br>
(You can check if the key is locked by pressing a button.)
<br>

・IDを忘れた場合は登録済みのメールアドレスを入力すると、メールでパスワード通知をしてくれる。
<br>
(When you forget your ID, you can get it by entering your registered Gmail adress.)

## mechanism, Demo

https://www.slideshare.net/secret/1ntxkdjvIRdAy4

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

・Arduino

・導線

## Install

・Flask 1.1.1

(You can get by 'pip install flask==1.1.1')

・SQLAlchemy

(You can get by 'pip install sqlalchemy')

## Author

・[tkyawa](https://github.com/tkyawa) : In charge of Hardware part

・[tehhuu](https://github.com/tehhuu) : In charge of Software part
