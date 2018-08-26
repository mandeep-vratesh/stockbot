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
    # bullish
    def hammer(stock):
        """
        Hammer is a one candle pattern that occurs in a downtrend when bulls make a start to
        step into the rally. It is so named because it hammers out the bottom. The lower shadow of
        hammer is minimum of twice the length of body. Although, the color of the body is not of
        much signifi cance but a white candle shows slightly more bullish implications than the black
        body. A positive day i.e. a white candle is required the next day to confi rm this signal.

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
        lastDay = getLast(1)    # (open, high, low, close)
        if (getBody(lastDay) <= 2*getShadow(lastDay))
        print('hammmer') 

    def inverted_hammer(stock):
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

    def dragonfly_doji(stock):
        print()
    
    def bullish_spinning_top(stock):
        print()
    
    # bearish
    def hanging_man(stock):
        """
        The hanging man appears during an uptrend, and its real body can be either black or white.
        While it signifi es a potential top reversal, it requires confi rmation during the next trading
        session. The hanging man usually has little or no upper shadow.
        """
        pass
    
    def shooting_star(stock):
        pass
    
    def gravestone_doji(stock):
        pass
    
    def bearish_spinning_top(stock):
        pass
    
class Double:
    #bulllish
    def bullish_kicker(stock):
        
    
    def bullish_engulfing(stock):
        pass
    
    def bullish_harami(stock):
        pass
    
    def piercing_line(stock):
        pass
    
    def tweezer_bottom(stock):
        pass

    #bearish
    def bearish_kicker(stock):
        pass
    
    def bearish_engulfing(stock):
        pass
    
    def bearish_harami(stock):
        pass

    def dark_cloud_cover(stock):
        pass
    
    def tweezer_top(stock):
        pass
    
class Triple:
    # bullish
    def morning_star(stock):
        pass
    
    def bullish_abandoned_baby(stock):
        pass

    def three_white_soldiers(stock):
        pass
    
    def three_line_strike(stock):
        pass
    
    # bearish
    def bearish_abandoned_body(stock):
        pass
    
    def three_black_cows(stock):
        pass
    
    def evening_doji_star(stock):
        pass
    
    def evening_star(stock):
        pass
    