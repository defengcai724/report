# 零基礎AI編程 : 如何使用ChatGPT批量處理文件?
我們用ChatGPT製作Python程序，提取Word/PDF的標題，將文件名取為標題，對圖片檔取拍照的地點及時間為檔名，並有刪除大量重複相同檔案的功能。


核心對話指令1：

幫我寫一個python程序，用於提取word的標題，而後將文件名改為標題。

<img width="1017" height="608" alt="image" src="https://github.com/user-attachments/assets/9fe49ef1-2969-4338-a9c0-0fbe0c0cf15c" />

<img width="1024" height="340" alt="image" src="https://github.com/user-attachments/assets/c65fcd24-8d92-4ccd-915b-9e32e1929449" />

<img width="996" height="362" alt="image" src="https://github.com/user-attachments/assets/87adb076-5b4f-4a7b-9e26-000a6d9d1969" />

造著ChatGPT的要求安裝套件

<img width="1157" height="360" alt="image" src="https://github.com/user-attachments/assets/b1f50530-864e-4111-a784-73921d9a504c" />

這邊我把檔案路徑打成對單一一個Word檔案，而程式要的是對資料夾檔案所以發生錯誤，因此創建一個新的資料夾在拉Word檔到其中便可執行。

<img width="965" height="739" alt="image" src="https://github.com/user-attachments/assets/eeef8f39-001b-4dda-b035-e65aeefb5556" />


核心對話指令2：

如果文件是pdf，能否給我一個完整的程式碼，既能修改word檔名，同時也能根據文件的第一行內容，修改pdf的檔名。


<img width="954" height="607" alt="image" src="https://github.com/user-attachments/assets/243c4431-df07-415a-90c7-3815c0aa1b6e" />

<img width="1286" height="367" alt="image" src="https://github.com/user-attachments/assets/088c2b7f-069d-4fa2-a101-a8d31ca04a09" />


一樣按照要求安裝套件

<img width="954" height="380" alt="image" src="https://github.com/user-attachments/assets/d045da4b-fa8f-4f37-811c-1b7aacf9be72" />

這邊如果每次都要修改檔案路徑太麻煩，所以給GPT提出要求，產生一個按鈕檔：

<img width="903" height="375" alt="image" src="https://github.com/user-attachments/assets/8fddc2bd-09fc-4d36-a66d-d80b1ab0c4d5" />

執行結果:

<img width="1074" height="280" alt="image" src="https://github.com/user-attachments/assets/390a4d45-cbb9-486a-805d-1b09c17c8872" />
