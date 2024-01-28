# -*- coding: utf-8 -*-

import numpy as np
import random
import scipy.sparse 


class ImageNoise:
    def __init__(self, X):
        #稀疏矩陣
        if scipy.sparse.isspmatrix(X):
            self.array_type         = 'Square'
            self.original_type      = type(X)
            self.Y                  = X.toarray() / 255
            self.height, self.width = self.Y.shape
        #RGB圖像
        elif len(X.shape) == 3:
            self.array_type                        = '3D_array'
            self.Y                                 = np.copy(X)
            self.height, self.width, self.channels = self.Y.shape
        #灰階圖像
        elif len(X.shape) == 2:
            self.array_type         = '2D_array'
            self.Y                  = np.copy(X)
            self.height, self.width = self.Y.shape
        else:
            raise ValueError("不支持的格式")
        
        
    def IfSparseConvert(self):
        if self.array_type == 'Square':
            self.Y = self.original_type((self.Y * 255).astype(np.uint8))
            
            
    def SaltedPepper(self, P, Noise_max = 1, Noise_min = 0):
        """
        Input Parameters 
        ----------
        P         : float; 雜訊百分比  e.g., 50.7 代表 50.7% 資料  
        Noise_max : float; 白噪點，正規化後圖片最大值為 1，預設為 1    
        Noise_min : float; 黑噪點，正規化後圖片最小值為 0，預設為 0  

        Output Parameters 
        ----------  
        Y      : np.array;  加噪後的圖片
        """
        # 全部雜訊數量(pixel數量)
        nz = int(self.height * self.width * P / 100)  

        # 確保雜訊數量為偶數
        if nz % 2 != 0:
            nz += 1

        # 分別為黑噪點和白噪點計算雜訊數量
        nz_per_salt = nz // 2

        # 生成隨機索引
        inf_indices = np.random.choice(self.height * self.width, nz, replace=False)
        
        # 轉換為行列索引
        inf_rows, inf_cols       = np.unravel_index(inf_indices[:nz_per_salt], (self.height, self.width))
        negInf_rows, negInf_cols = np.unravel_index(inf_indices[nz_per_salt:], (self.height, self.width))

        # 添加雜訊
        for row, col in zip(inf_rows, inf_cols):
            self.Y[row, col] = Noise_max

        for row, col in zip(negInf_rows, negInf_cols):
            self.Y[row, col] = Noise_min
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()

        return self.Y

    def LaplacianNoise(self, mu = 0, sigma = 0.1):
        """
        Input Parameters 
        ----------
        mu    :    float; 平均值
        sigma :    float; 標準差 

        Output Parameters 
        ----------  
        Y     : np.array;  加噪後的圖片
        """
        # 生成拉普拉斯雜訊並加入原本的矩陣
        self.Y = self.Y + np.random.laplace(mu, sigma, self.Y.shape)
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()

        return self.Y


    def ContinuousOcclusion(self, BlockSize, PosX):
        """
        Input Parameters 
        ----------
          BlockSize : list; 大小 1-by-2; e.g., [10, 10] Block大小為 10-by-10 
          PosX      : list; 大小 1-by-2; e.g., [0, 3]  表將該Block的左上放置於第1列, 第4行位置
          
        Output Parameters 
        ----------  
          Y        : np.array; 加噪後的圖片   
        """   
        # 計算需要遮擋的行和列的範圍
        row_range = slice(PosX[0], min(PosX[0] + BlockSize[0], self.height))
        col_range = slice(PosX[1], min(PosX[1] + BlockSize[1], self.width))
        
        # 在舉陣中遮擋指定的區塊
        self.Y[row_range, col_range] = np.NaN
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()
    
        return self.Y


    def GlitchNoise(self, P, orientation='vertical', param_nam='hetero'):
        """
        Input Parameters 
        ----------
        P           :   float; 雜訊百分比  e.g., 50.7 代表 50.7% 資料  
        orientation :     str; 傳入字串參數 = 'vertical':垂直故障雜訊 or ‘horizontal’:水平故障雜訊 
        param_nam   :     str; 傳入字串參數 = ‘homo’:各通道的故障雜訊位置一樣 or 'hetero':各通道的故障雜訊位置不一樣
          
        Output Parameters 
        ----------  
          Y        : np.array; 加噪後的圖片     
        """           
        
        def GlitchRndGen(N, P):
            # 選擇一個隨機起始點
            start_point = random.randint(0, int(N * 0.8))
    
            # 計算每個部分要抽取的元素數量，依照八二法則分佈
            num_80_percent = int(N * P/100 * 0.8)
            num_20_percent = int(N * P/100 * 0.2)
    
            # 確保不會從範圍外抽取元素
            end_point = min(start_point + int(N * 0.2), N)
    
            # 從 start_point 到 end_point 中選擇元素
            array_20_percent = range(start_point, end_point)
            num80_in_array20 = random.sample(array_20_percent, min(num_80_percent, len(array_20_percent)))
            
            # 計算溢出和剩餘數量
            overflow = num_80_percent - len(num80_in_array20)
            num_20_percent += overflow
    
            # 從剩餘範圍中選擇元素
            all_numbers       = set(range(N))
            excluded_range    = set(array_20_percent)
            available_numbers = list(all_numbers - excluded_range)
            num20_in_array80  = random.sample(available_numbers, min(num_20_percent, len(available_numbers)))
            
            noise_list = num80_in_array20  + num20_in_array80
            return noise_list
    
        def Glitch(Y, noise_list, orientation):
            if orientation == "vertical":
                Y[:, noise_list] = np.NaN
            elif orientation == "horizontal":
                Y[noise_list, :] = np.NaN    
            return Y
        
        # 辨識添加雜訊為垂直或水平
        if orientation == "vertical":
            N = self.width
        elif orientation == "horizontal":
            N = self.height
        
        # 灰階圖片
        if len(np.shape(self.Y)) == 2:
            noise_list = GlitchRndGen(N, P)
            Glitch(self.Y, noise_list, orientation)
        # RGB圖片
        elif len(np.shape(self.Y)) == 3:
            # RGB三層雜訊位置一樣
            if param_nam == "homo":
                noise_list = GlitchRndGen(N, P)
                for d in range(self.channels):
                    Glitch(self.Y[:, :, d], noise_list, orientation)
            # RGB三層雜訊位置不一樣
            elif param_nam == "hetero":
                for d in range(self.channels):
                    noise_list = GlitchRndGen(N, P)
                    Glitch(self.Y[:, :, d], noise_list, orientation)
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()
                    
        return self.Y


    def GaussianNoise(self, mu = 0, sigma = 0.1):
        """
        Input Parameters 
        ----------
        mu    :    float; 平均值
        sigma :    float; 標準差 

        Output Parameters 
        ----------  
        Y     : np.array;  加噪後的圖片
        """
        self.Y = self.Y + np.random.normal(mu, sigma, self.Y.shape)
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()
        
        return self.Y
      
        
    def PoissonNoise(self, plambda): 
        """
        Input Parameters 
        ----------
        plambda :    float; 建議大於 1.0

        Output Parameters 
        ----------  
        Y     : np.array;  加噪後的圖片
        """
        self.Y = np.random.poisson(self.Y * plambda, self.Y.shape) / float(plambda)
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()
                    
        return self.Y


    def SpeckleNoise(self): 
        """
        Output Parameters 
        ----------  
        Y     : np.array;  加噪後的圖片
        """
        gauss  = np.random.randn(*self.Y.shape)        
        self.Y = self.Y + self.Y * gauss
        
        # 稠密矩陣轉回稀疏矩陣
        self.IfSparseConvert()
            
        return self.Y