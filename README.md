# 圖像雜訊

## 介紹
### 椒鹽雜訊 (SaltedPepper Noise)
椒鹽雜訊是因數據丟失而產生的，常見於數位影像傳輸或存儲過程中。它表現為隨機分佈的亮點和暗點，類似於老式電視屏幕上的靜電噪聲或掃描文件中的灰塵顆粒。
### 拉普拉斯雜訊 (Laplacian Noise)
拉普拉斯雜訊具有尖峰的分布特性，能夠模擬圖像中的異常點或邊緣噪聲，特別適用於強調圖像細節或進行邊緣檢測。
### 連續遮擋 (Continuous Occlusion)
連續遮擋是指在動態環境中物體不斷地被其他物體遮擋的情況。這種情況在監控攝像、自動駕駛和人群分析等場景中特別常見，對於訓練機器學習模型處理遮擋問題非常有用，特別是在需要分析和識別遮擋物體的應用中。
### 故障雜訊 (Glitch Noise)
故障雜訊模仿數碼裝置或信號傳輸中的故障，如圖像或影片的意外扭曲。這種雜訊常用於測試圖像處理算法的強健性，或在藝術創作中產生獨特效果。
### 高斯雜訊 (Gaussian Noise)
高斯雜訊具有正態分佈的統計特性，是自然界和人造圖像中最常見的雜訊類型之一。它廣泛應用於圖像處理、機器學習等領域，用於模擬現實世界中的隨機雜訊，並進行降噪算法的開發和測試。
### 泊松雜訊 (Poisson Noise)
泊松雜訊，也稱為光子雜訊，是在低光照條件下拍攝的圖像中常見的雜訊類型，與光的量子性質有關。這種雜訊在天文攝影、醫學影像等領域中尤為重要，用於模擬和處理低光照條件下的影像，特別是在需要考慮光照變化的應用中。
### 斑點雜訊 (Speckle Noise)
斑點雜訊是一種乘性雜訊，常見於雷達、超聲波和某些類型的光學圖像。這種雜訊由相干波的隨機干涉引起，對於提高圖像品質和分辨率的研究至關重要，特別是在雷達和醫學影像處理中。

## 執行
### 原圖
為了明顯看出添加雜訊的效果，使用兩種不同大小的圖片，512x512像素的萊娜圖和32x32像素cifar10資料庫內的其中一張圖片。
| 萊娜圖 | cifar10 |
| --- | --- |
| <img src="https://github.com/PHW22/Noise/assets/116903114/5c20a6b0-8d5d-431c-b824-ee72c1f09158" style="width: 180px; height: auto;" /> | <img src="https://github.com/PHW22/Noise/assets/116903114/e2e1bbf2-178d-4e1d-a850-1924c8e5264c" style="width: 180px; height: auto;" /> |



### 添加雜訊結果 

<table style="width: 100%; table-layout: fixed;">
  <tr>
    <th style="width: 25%;">椒鹽雜訊</th>
    <th style="width: 25%;">拉普拉斯雜訊</th>
    <th style="width: 25%;">連續遮擋</th>
    <th style="width: 25%;">故障雜訊</th>
  </tr>
  <tr>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/e6c92fcc-9bec-47b8-a999-f164e6497e15" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/591b9011-662a-4a7c-8a63-de13238df4f6" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/f0909275-708a-427c-b618-0b476a1124cb" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/c37effe9-753d-482d-87bf-4358dd57e867" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
  </tr>
  <tr>
    <th>高斯雜訊</th>
    <th>泊松雜訊</th>
    <th>斑點雜訊</th> 
  </tr>
  <tr>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/9fbaa785-baab-4e81-bf41-002814d8284b" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/e46a4469-07dc-42be-876b-64f69347148a" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
    <td style="width: 25%; text-align: center;">
      <img src="https://github.com/PHW22/Noise/assets/116903114/ecc1d2dd-28e1-4771-8082-59a163e0d5bc" style="width: 100%; max-width: 300px; height: auto;" />
    </td>
  </tr>
</table>





