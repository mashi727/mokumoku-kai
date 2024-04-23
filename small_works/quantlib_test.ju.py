# %%

from datetime import date
import QuantLib as ql
import math

calendar = ql.UnitedStates(m)
day_count = ql.ActualActual()

# 設定
spot       = 3378.5     # 原資産価格
strike     = 3370.0     # 権利行使価格
volatility = 0.22635875427740032  #ボラティリティ
rate       = 0.670   # 金利（リスクフリーレート）＊パーセント
now_date   = date(2020,  8, 19)
last_date  = date(2020, 12, 18) # 満期日

# 変換
interest_rate = rate / 100
calc_date = ql.Date(now_date.day, now_date.month, now_date.year)
option_maturity_date = ql.Date(last_date.day, last_date.month, last_date.year) 

ql.Settings.instance().evaluationDate = calc_date

flavor = ql.Option.Call

yield_curve = ql.FlatForward(calc_date, 
                             interest_rate,
                             day_count,
                             ql.Compounded,
                             ql.Continuous)

discount = yield_curve.discount(option_maturity_date)
strikepayoff = ql.PlainVanillaPayoff(flavor, strike)
T = yield_curve.dayCounter().yearFraction(calc_date, option_maturity_date) # 満期までの期間（年）
stddev = volatility*math.sqrt(T)

# 算出
black = ql.BlackCalculator(strikepayoff, 
                           spot, 
                           stddev, 
                           discount)

print("%-20s: %4.4f" %("Option Price", black.value() ))
print("%-20s: %4.4f" %("Delta", black.delta(spot) ))
print("%-20s: %4.4f" %("Gamma", black.gamma(spot) ))
print("%-20s: %4.4f" %("Theta", black.theta(spot, T) ))
print("%-20s: %4.4f" %("Vega", black.vega(T) ))
print("%-20s: %4.4f" %("Rho", black.rho( T) ))

# Option Price        : 178.9641
# Delta               : 0.5325
# Gamma               : 0.0009
# Theta               : -262.5823
# Vega                : 770.5092
# Rho                 : 535.5627

# %%
