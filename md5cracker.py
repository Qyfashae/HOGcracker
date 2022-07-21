import hashlib 

wordlist = str(input('Enter wordlist location: '))
hash_input = str(input('Enter hash to be cracked: '))

with open(wordlist, 'r') as file:
	for line in file.readlines():
		hash_ob = hashlib.md5(line.strip().encode())
		hashed_pass = hash_ob.hexdigest()
		if hashed_pass == hash_input:
			print("Cracked successfully! " + line.strip())
			exit(0)
