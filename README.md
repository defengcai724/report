# 零基礎AI編程 : 如何使用ChatGPT批量處理文件?
我們用ChatGPT製作Python程序，提取Word/PDF的標題，將文件名取為標題，對圖片檔取拍照的地點及時間為檔名，並有刪除大量重複相同檔案的功能。


核心對話指令1：

幫我寫一個python程序，用於提取word的標題，而後將文件名改為標題。

<img width="1017" height="608" alt="image" src="https://github.com/user-attachments/assets/9fe49ef1-2969-4338-a9c0-0fbe0c0cf15c" />

<img width="1024" height="340" alt="image" src="https://github.com/user-attachments/assets/c65fcd24-8d92-4ccd-915b-9e32e1929449" />

<img width="996" height="362" alt="image" src="https://github.com/user-attachments/assets/87adb076-5b4f-4a7b-9e26-000a6d9d1969" />

照著ChatGPT的要求安裝套件

<img width="1157" height="360" alt="image" src="https://github.com/user-attachments/assets/b1f50530-864e-4111-a784-73921d9a504c" />

這邊錯誤把檔案路徑打成對單一一個Word檔案，而程式要的是對資料夾檔案所以發生錯誤，因此創建一個新的資料夾在拉Word檔到其中便可執行。

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

接下來要求ChatGPT能讓圖片也改名

<img width="950" height="538" alt="image" src="https://github.com/user-attachments/assets/29e171ab-a79d-4082-a2ba-fe7df97072ad" />

<img width="1053" height="240" alt="image" src="https://github.com/user-attachments/assets/86abd0d7-ce29-4fd9-abaf-f39fc3f5096d" />

安裝套件

<img width="891" height="701" alt="image" src="https://github.com/user-attachments/assets/68823b2b-59f2-4b18-a34c-51770bb4f7a8" />

我們的圖片是網上下載下來的，EXIF資料被消除了，後來改用筆電拍照才成功運行。

EXIF 資料是數位相片內建的「拍攝資訊」，記錄相機設定、拍攝時間、地點、影像尺寸等技術細節，像是照片的附加說明。

<img width="918" height="605" alt="image" src="https://github.com/user-attachments/assets/9fc76201-bcb6-4359-bb9c-64bd8295f306" />

<img width="545" height="132" alt="image" src="https://github.com/user-attachments/assets/4fcd5aec-91f9-4396-8eb7-0fd5c1f72d6c" />

功能:刪除重複文件，保留最新版本

<img width="1005" height="444" alt="image" src="https://github.com/user-attachments/assets/4ab6193b-1f4e-4c54-8aae-7a03df11d838" />

<img width="963" height="655" alt="image" src="https://github.com/user-attachments/assets/dcd1cbd3-5f09-460b-b91c-a9015fdd21c6" />

執行結果:

<img width="1504" height="306" alt="image" src="https://github.com/user-attachments/assets/32c6078d-f655-46c1-ab0d-f37f280e44c0" />

最後把所有功能整合到一起

<img width="925" height="534" alt="image" src="https://github.com/user-attachments/assets/0120bb68-4256-4aaa-93f5-e40ba698414f" />

最終結果:

<img width="1029" height="315" alt="image" src="https://github.com/user-attachments/assets/ac25ca28-88c3-41be-ba12-18575f190f18" />

核心指令：如何將這個python程式碼打包成一個可以獨立執行的執行檔？

<img width="937" height="719" alt="image" src="https://github.com/user-attachments/assets/5a83ba19-3589-468f-bc5d-90da7cc6b263" />

<img width="978" height="558" alt="image" src="https://github.com/user-attachments/assets/4c7bb526-9765-4b5a-b967-01cbfa0f16bf" />

執行檔在dist資料夾中

<img width="853" height="237" alt="image" src="https://github.com/user-attachments/assets/b9ccd2b2-263c-4abe-8b8f-2ba42331928d" />


# 結語

這套工具將常見的文件整理與批量重命名需求整合在一起，大大提高了文件管理效率。無論是清理重複文件、整理 Word/PDF 文檔，還是按照拍攝日期和地點管理圖片，都能輕鬆完成，並且操作簡單直觀。通過 GUI 與可執行檔打包，普通使用者也能直接使用，實用性與易用性兼具。總體而言，這次專案讓我們越來越佩服AI，也提升我們對實用工具設計的思維，體會到程式可以如何真正幫助日常生活與工作中的繁瑣任務自動化，提高效率。
