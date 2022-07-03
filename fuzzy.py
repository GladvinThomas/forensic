from ssdeep import ssdeep
from dist import edit_dist


def hash_function(path):
	f=open(path,'r')
	data=f.read()
	f.close()

	hash1=ssdeep(data)
	return hash1

def check_hash(hash1,hash2):
	print(hash1,hash2,'======')
	n=edit_dist(hash1,hash2)
	return n  


    


if __name__=="__main__":

    s1 = 'some long text'  # or open('first.txt').read()
    hash1 = spamsum(s1)
    hash2 = spamsum('somewhat long telegram')
    hash3=spamsum('some long text')


    