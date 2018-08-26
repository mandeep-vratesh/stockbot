from multiprocessing import Pool, TimeoutError
import multiprocessing
import time
import os
from nsetools import Nse
from datetime import datetime
import json

#initializations
nse = Nse()

def f(x):
	try:
		stock_data = nse.get_quote(x)
	except Exception as e:
		pass


if __name__ == '__main__':
	p = Pool(multiprocessing.cpu_count())
	print("start", datetime.now())
	p.map(f, list(nse.get_stock_codes().keys()))
	# p.map(f, ['INFY','TITAN','ARCHIES','TATAINVEST','DIVISLAB','UCOBANK','VASWANI','BAJAJHLDNG','TRIDENT','PFOCUS','RAINBOWPAP','MODIRUBBER','BANARBEADS','GMRINFRA','ZEEL','GVKPIL','BALRAMCHIN','WIPRO','KANANIIND','HTMEDIA','SBIN','MAGNUM','SARDAEN','ZYLOG','JPASSOCIAT','LOTUSEYE','PAGEIND','SOUTHBANK','APLLTD','PTL','FAIRCHEM','NATNLSTEEL','VSTIND','HPL','LAKSHMIEFL','RECLTD','FMGOETZE','KOHINOOR','SHRIRAMEPC','KSBPUMPS','NRAIL','JKLAKSHMI','HEG','IL&FSENGG','BFINVEST','LGBFORGE','TFL','SURANAIND','MAHAPEXLTD','INOXLEISUR','SPLIL','GLOBALVECT','TTL','KRBL','KARURVYSYA','MUTHOOTCAP','GABRIEL','NILKAMAL','WEIZFOREX','ALICON','UJAAS','GULFOILLUB','IVP','GSS','NTPC','HERCULES','ESABINDIA','AXISBANK','ICSA','FCONSUMER','PSB'])

	print("end", datetime.now())

	print("start", datetime.now())
	# for x in ['INFY','TITAN','ARCHIES','TATAINVEST','DIVISLAB','UCOBANK','VASWANI','BAJAJHLDNG','TRIDENT','PFOCUS','RAINBOWPAP','MODIRUBBER','BANARBEADS','GMRINFRA','ZEEL','GVKPIL','BALRAMCHIN','WIPRO','KANANIIND','HTMEDIA','SBIN','MAGNUM','SARDAEN','ZYLOG','JPASSOCIAT','LOTUSEYE','PAGEIND','SOUTHBANK','APLLTD','PTL','FAIRCHEM','NATNLSTEEL','VSTIND','HPL','LAKSHMIEFL','RECLTD','FMGOETZE','KOHINOOR','SHRIRAMEPC','KSBPUMPS','NRAIL','JKLAKSHMI','HEG','IL&FSENGG','BFINVEST','LGBFORGE','TFL','SURANAIND','MAHAPEXLTD','INOXLEISUR','SPLIL','GLOBALVECT','TTL','KRBL','KARURVYSYA','MUTHOOTCAP','GABRIEL','NILKAMAL','WEIZFOREX','ALICON','UJAAS','GULFOILLUB','IVP','GSS','NTPC','HERCULES','ESABINDIA','AXISBANK','ICSA','FCONSUMER','PSB']:
	for x in nse.get_stock_codes().keys():
		try:
			stock_data = nse.get_quote(x)
		except Exception as e:
			pass
	print("end", datetime.now())
