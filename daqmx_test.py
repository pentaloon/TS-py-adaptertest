import nidaqmx

class DAQmxTest:

	def ai_read_single(self, device_id):
		with nidaqmx.Task() as task:
			task.ai_channels.add_ai_voltage_chan(device_id)
			return task.read()

	def ai_read_nsamples(self, device_id, n_samples):
		with nidaqmx.Task() as task:
			task.ai_channels.add_ai_voltage_chan(device_id)
			return task.read(number_of_samples_per_channel=int(n_samples))

	def di_read_lines(self, device_id, negate):
		from nidaqmx.constants import LineGrouping
		with nidaqmx.Task() as task:
			task.di_channels.add_di_chan(device_id, line_grouping=LineGrouping.CHAN_PER_LINE)
			line_states=task.read()
			return [not l for l in line_states] if negate else line_states
			
	def ctr_write(self, device_id):
		from nidaqmx.types import CtrTime
		with nidaqmx.Task() as task:
			task.co_channels.add_co_pulse_chan_time(device_id)
			sample = CtrTime(high_time=0.001, low_time=0.001)
			task.write(sample)
	
	def ao_write(self, device_id):
		with nidaqmx.Task() as task:
			task.ao_channels.add_ao_voltage_chan(device_id)
			task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)