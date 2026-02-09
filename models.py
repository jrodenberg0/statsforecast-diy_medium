from statsforecast.models import (
_TS, 
_repeat_val_seas,
_seasonal_naive,
_ensure_float
) 
import numpy as np 
from pydlm import dlm, trend, seasonality,autoReg, modelTuner
from sklearn.preprocessing import RobustScaler 


from typing import Optional,List

class SeasonalNaiveWDrift(_TS):
    def __init__(self,season_length,alias:str = 'SeasonalNaiveWDrift'):
        self.alias = alias
        self.season_length = season_length 
    
    def fit(self,y: np.ndarray, X: Optional[np.ndarray] = None):
        # estimate a robust drift form... 
        log_y = np.log1p(y)
        self.drift = np.diff(log_y).mean()
        self.seas_val = log_y[-self.season_length:]
        return self


    def predict(self,h: int,X: Optional[np.ndarray] = None,):
        # repeat seasonal naive val... 
        preds = _repeat_val_seas(season_vals=self.seas_val,h=h)
        # get drift term 
        return {'mean':np.expm1(preds + h * self.drift)}

    def forecast(self,
                y: np.ndarray,
                h: int,
                X: Optional[np.ndarray] = None,
                X_future: Optional[np.ndarray] = None,
                level: Optional[List[int]] = None,
                fitted: bool = False):

                self.fit(y,X=X)
                return self.predict(h=h,X=X_future)

class PyDLM(_TS):
    def __init__(self,model_components:list,alias:str = 'DLM'):
        self.alias = alias
        self.model_components = model_components
        self.scaler = RobustScaler()

    def fit(self,y: np.ndarray, X: Optional[np.ndarray] = None):

        #instantiate base dynamic linear model 
        y = _ensure_float(y).reshape(-1,1)
        y = self.scaler.fit_transform(y).flatten()

        DLM_MODEL = dlm(y)
        DLM_MODEL.setLoggingLevel("WARNING")

        for component in self.model_components:
            DLM_MODEL.add(component) # add components to model... 

       # model_tune = modelTuner(method='gradient_descent', loss='mse')
        self.model = DLM_MODEL
        self.model.fit() # fit model
        return self 

    def predict(self, h: int,X: Optional[np.ndarray] = None):
        predictions, variances = self.model.predictN(N=h)
        
        return {
            'mean': self._reshape_and_transform(predictions),
            'variances': self._reshape_and_transform(variances)
        }

    def forecast(self,
                y: np.ndarray,
                h: int,
                X: Optional[np.ndarray] = None,
                X_future: Optional[np.ndarray] = None,
                level: Optional[List[int]] = None,
                fitted: bool = False):

                self.fit(y,X=X)
                return self.predict(h=h,X=X_future)


    
    def _reshape_and_transform(self,y):
        return self.scaler.inverse_transform(np.array(y).reshape(-1, 1)).flatten()
    
    
