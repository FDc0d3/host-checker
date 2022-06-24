try:
	import sys, httpx, random, threading
	import colorama
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET

class HostCheck:
	def __init__(self, url):
		self.url = url
		self.count = 0
	def status(self):
		try:
			while True:
				try:
					self.count += 1
					resp = httpx.get(self.url)
					code = resp.status_code
					if code == 200:
						print(f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (OK)")
					elif code == 301:
						print(f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Moved Permanently)")
					elif code == 302:
						print(f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Found)")
					elif code == 303:
						print(f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (See Other)")
					elif code == 307:
						print(Color.LY+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Temporary Redirect)")
					elif code == 400:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Bad Request)")
					elif code == 401:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Unauthorized)")
					elif code == 403:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Forbidden)")
					elif code == 404:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Not Found)")
					elif code == 408:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Request Timeout)")
					elif code == 410:
						print(f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Gone)")
					elif code == 429:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Too Many Requests)")
					elif code == 500:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Internal Server Error)")
					elif code == 502:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Bad Gateway)")
					elif code == 503:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Service Unavailable)")
					elif code == 504:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Gateway Timeout)")
					elif code == 507:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Insufficient Storage)")
					elif code == 508:
						print(Color.LR+f"[{self.count}] Status from {self.url} | {code} | {round(resp.elapsed.total_seconds(), 3)} Seconds | (Loop Detected)")
					else:
						print(Color.LR+f"[{self.count}] Status from {self.url} | (Connection Timeout)")
				except httpx.TimeoutException:
					print(Color.LR+f"[{self.count}] Status from {self.url} | (Connection Timeout)")
				except httpx.ConnectError:
					print(Color.LC+f"[{self.count}] Invalid URL")
		except KeyboardInterrupt:
			pass

class Process():
	def __init__(self, obj):
		self.obj = threading.Thread(target=obj)
	def __enter__(self):
		return self.obj
	def __exit__(self, type, value, traceback):
		if self.obj.is_alive():
			raise RuntimeError("Thread Error")
		else:
			return True

def main():
	if len(sys.argv[1:]) != 1:
		print("> HostChecker | Made By FDc0d3")
		sys.exit(f"Usage:\npython3 {__file__} <url>")
	with Process(obj=HostCheck(sys.argv[1]).status()) as ready:
		try:
			ready.start()
		except RuntimeError() as E:
			print(E)

if __name__ == '__main__':
	# make a simple, but mighty
	main()
