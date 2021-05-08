import nidmm

def dmm_read(device_id):
	with nidmm.Session(device_id) as session:
		session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10, 5.5)
		return session.read()