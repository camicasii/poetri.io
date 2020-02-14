from pytz import  timezone
from datetime import datetime, time
import datetime as dt
import  time
import copy
import  pytz
from tzlocal import get_localzone # $ pip install tzlocal

London_StockExchange={
   "open":(dt.time(9, 30, 00),),
    "close":(dt.time(17, 30, 00),)
}
TYO_StockExchange={
   "open":(dt.time(16, 00, 00),dt.time(22, 00, 00)),
    "close":(dt.time(18, 00, 00),dt.time(00, 45, 00))
}
ASX_StockExchange={
   "open":(dt.time(10, 00, 00),),
    "close":(dt.time(19, 30, 00),)
}
NYSE_StockExchange={
   "open":(dt.time(9,30, 00),),
    "close":(dt.time(4, 00, 00),)
}
VenezuelaTimeZone = [timezone('America/Caracas')]
#ASX (Australian Securities Exchange)
ASXTimeZone = (timezone('Australia/Sydney'), ASX_StockExchange)
#TYO (Bolsa de Tokio)
TYOTimeZone = (timezone('Asia/Tokyo'),TYO_StockExchange)
#London Stock Exchange
LondonTimeZone = (timezone('Europe/London'),London_StockExchange)
#New York Stock Exchange (Bolsa de Nueva York)
NYSETimeZone = (timezone('America/New_York'),NYSE_StockExchange)

StockExchanges=[ASXTimeZone,TYOTimeZone,LondonTimeZone,NYSETimeZone]

def __isWeekEnd() -> bool:
    #["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekEnd_ = datetime.now().weekday()
    if weekEnd_ == 5 or weekEnd_ == 6:
        return True
    else:
        return False

def _timeStockExchange(date):
        if __isWeekEnd():
            return [False,"is Weekend"]
        [StockExchangeHours,openClose]=date

        timeStock=datetime.now(StockExchangeHours).time()

        for state in  openClose:
            if len(openClose[state])>1:
                break
            [openState] = openClose["open"]
            [closeState] = openClose["close"]
            state_= closeState>timeStock>openState
            return [state_, timeStock.strftime("%H:%M:%S")]

        [open_, close_] = openClose.items()
        [_,[open_one,open_two]]=open_
        [_, [close_one, close_two]] = close_
        state_=close_one>timeStock>open_one  or close_two>timeStock>open_two
        return  [state_,timeStock.strftime("%H:%M:%S")]

def timeConvert(arg):
    res = copy.copy(arg)
    for key,val  in arg.items():

        if len(val) >1:
            tyo_str=[]
            for _time in val:
                tyo_str.append(_time.strftime("%H:%M:%S"))
            res[key] = tyo_str
        else:
            [time_] =val
            #if isinstance(time_,time):
            res[key]=time_.strftime("%H:%M:%S")
    return res






def stateStockExchange():
    stock_Exchange=[]
    global StockExchanges
    for date in StockExchanges:
        [timeZone_,StockExchange_]=date

        stock_Exchange.append({"stock_Exchange":timeZone_.__str__(),
                               "state":_timeStockExchange(date),
                                "hours":timeConvert(StockExchange_),
                                "localHours":timeHoraLocal(date)})
    return stock_Exchange

def aux_timeHoraLocal(zona,extTime, hour):
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    fmt2 = '%H:%M:%S'
    data = zona.localize(datetime(extTime.year,
                                      extTime.month,
                                      extTime.day,
                                      hour.hour,
                                      hour.minute,
                                      hour.microsecond), is_dst=False)
    return data.astimezone(get_localzone()).strftime(fmt2)


def timeHoraLocal(data):
    [zone_,hours]=data
    extTime = datetime.now(zone_).now()
    [open_,close_]=hours
    isOpenPlus =hours[open_]
    isClosePlus = hours[close_]
    if len(isOpenPlus)>1:
        timeHoraLocal_={ open_: [],
        close_:[]}
        for opening in isOpenPlus:
            timeHoraLocal_[open_].append(aux_timeHoraLocal(zone_, extTime, opening))
        for closed in isClosePlus:
            timeHoraLocal_[close_].append(aux_timeHoraLocal(zone_, extTime, closed))
        return timeHoraLocal_

    [opening]=hours[open_]
    [closed]=hours[close_]

    openLocal_= aux_timeHoraLocal(zone_,extTime,opening)
    closedLocal_ = aux_timeHoraLocal(zone_,extTime,closed)
    #return [openLocal_,closedLocal_]
    return {open_:openLocal_,close_:closedLocal_}

if __name__ == '__main__':
    mytime = datetime.now()
    old_time =timezone('Australia/Sydney')
    #dt.time(9, 30, 00)
    new_time = timezone('America/Caracas')
    a =datetime.now(240)





    print(
        a
    #stateStockExchange()

    )



