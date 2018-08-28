from nsetools import Nse
import json
from pprint import pprint
from datetime import datetime, timedelta
import urllib

"""
Given:
m1(minus-1) : {
    0 : open
    1 : high
    2 : low
    3 : close
}
similarly m2 and m3
"""
class Single:

    def getCorrected_ith_Date(self, back):
        # TODO: add holiday handling
        return_date = (datetime.today() - timedelta(back)).strftime('%Y-%m-%d')
        return return_date

    def getLast(self, days, stock_code):
        with open('files/stock_data_min.json') as f :
            min_stock_data = json.load(f)
            # {'TITAN': {'2018-08-26': {'close': 0, 'high': 100, 'low': 60, 'open': 100}}}

        return_data = []
        for i in range(days):
            date = self.getCorrected_ith_Date(i)
            try:
                data = {'close': -1, 'high': -1, 'low': -1, 'open': -1}
                data = min_stock_data[stock_code][date]
            except Exception as e:
                print("-1")
            return_data.append((data["open"],data["high"],data["low"],data["close"]))

        return return_data

    def getBodyHeight(self, data):
        # print("Body height is : " + str(data[3] - data[0]))
        return data[3] - data[0]

    def getBottomShadowHeight(self, data):
        if data[0] <= data[3] :
            # print("Bottom shadow is : " + str(data[2] - data[0]))
            return data[2] - data[0]
        else :
            # print("Bottom shadow is : " + str(data[2] - data[3]))
            return data[2] - data[3]

    def getTopShadowHeight(self, data):
        if data[0] <= data[3] :
            return data[1] - data[3]
        else :
            return data[1] - data[0]


    # bullish
    def hammer(self, stock):
        """
        Hammer is a one candle pattern that occurs in a downtrend when bulls make a start to
        step into the rally. It is so named because it hammers out the bottom. The lower shadow of
        hammer is minimum of twice the length of body. Although, the color of the body is not of
        much signifi cance but a white candle shows slightly more bullish implications than the black
        body. A positive day i.e. a white candle is required the next day to confirm this signal.

        Criteria
        1. The lower shadow should be at least two times the length of the body.
        2. There should be no upper shadow or a very small upper shadow.
        3. The real body is at the upper end of the trading range. The color of the body is not
        important although a white body should have slightly more bullish implications.
        4. The following day needs to confi rm the Hammer signal with a strong bullish day.

        Signal enhancements
        1. The longer the lower shadow, the higher the potential of a reversal occurring.
        2. Large volume on the Hammer day increases the chances that a blow off day has
        occurred.
        3. A gap down from the previous day’s close sets up for a stronger reversal move provided
        the day after the Hammer signal opens higher.

        Pattern psychology
        The market has been in a downtrend, so there is an air of bearishness. The price opens and
        starts to trade lower. However the sell-off is abated and market returns to high for the day as
        the bulls have stepped in. They start bringing the price back up towards the top of the trading
        range. This creates a small body with a large lower shadow. This represents that the bears
        could not maintain control. The long lower shadow now has the bears questioning whether
        the decline is still intact. Confi rmation would be a higher open with yet a still higher close on
        the next trading day.
        """
        lastDay = self.getLast(1, stock)[0]    # [(open, high, low, close),(open, high, low, close),(open, h....
        # TODO: check if any value is negative in ohlc, then print not enough data
        if (2*abs(self.getBodyHeight(lastDay)) <= abs(self.getBottomShadowHeight(lastDay))) :
            print(stock,": hammer") 
        else:
            pass
            # print('no hammer')

    def inverted_hammer(self, stock):
        """
        Description
        Inverted hammer is one candle pattern with a shadow at least two times greater than the
        body. This pattern is identifi ed by the small body. They are found at the bottom of the decline
        which is evidence that bulls are stepping in but still selling is going on. The color of the small
        body is not important but the white body has more bullish indications than a black body. A
        positive day is required the following day to confi rm this signal.

        Signal enhancements
        1. The longer the upper shadow, the higher the potential of a reversal occurring.
        2. A gap down from the previous day’s close sets up for a stronger reversal move.
        3. Large volume on the day of the inverted hammer signal increases the chances that a
        blow off day has occurred
        4. The day after the inverted hammer signal opens higher.

        Pattern psychology
        After a downtrend has been in effect, the atmosphere is bearish. The price opens and starts to
        trade higher. The Bulls have stepped in, but they cannot maintain the strength. The existing
        sellers knock the price back down to the lower end of the trading range. The Bears are still in
        control. But the next day, the Bulls step in and take the price back up without major resistance
        from the Bears. If the price maintains strong after the Inverted Hammer day, the signal is
        confi rmed.
        """
        print('inverted hamer')

    def dragonfly_doji(self, stock):
        print()
    
    def bullish_spinning_top(self, stock):
        print()
    
    # bearish
    def hanging_man(self, stock):
        """
        The hanging man appears during an uptrend, and its real body can be either black or white.
        While it signifi es a potential top reversal, it requires confi rmation during the next trading
        session. The hanging man usually has little or no upper shadow.
        """
        pass
    
    def shooting_star(self, stock):
        pass
    
    def gravestone_doji(self, stock):
        pass
    
    def bearish_spinning_top(self, stock):
        pass
    
class Double:
    #bulllish
    def bullish_kicker(self, stock):
        pass
    
    def bullish_engulfing(self, stock):
        pass
    
    def bullish_harami(self, stock):
        pass
    
    def piercing_line(self, stock):
        pass
    
    def tweezer_bottom(self, stock):
        pass

    #bearish
    def bearish_kicker(self, stock):
        pass
    
    def bearish_engulfing(self, stock):
        pass
    
    def bearish_harami(self, stock):
        pass

    def dark_cloud_cover(self, stock):
        pass
    
    def tweezer_top(self, stock):
        pass
    
class Triple:
    # bullish
    def morning_star(self, stock):
        pass
    
    def bullish_abandoned_baby(self, stock):
        pass

    def three_white_soldiers(self, stock):
        pass
    
    def three_line_strike(self, stock):
        pass
    
    # bearish
    def bearish_abandoned_body(self, stock):
        pass
    
    def three_black_cows(self, stock):
        pass
    
    def evening_doji_star(self, stock):
        pass
    
    def evening_star(self, stock):
        pass

if __name__ == "__main__" :
    sin = Single()

    #instantiating NSE
    nse = Nse()
    try:
        all_stock_codes = nse.get_stock_codes()
    except urllib.error.URLError as e:
        all_stock_codes = {}
    except Exception as e:
        print(str(e))
        
    for stock_code in all_stock_codes.keys() :
        sin.hammer(stock=stock_code)

    sin.hammer(stock='TATAINVEST')
