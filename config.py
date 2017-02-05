class accesstoken():
	def assign_token(self):
		token="EwD4Aq1DBAAUGCCXc8wU/zFu9QnLdZXy+YnElFkAAcGS8kiKBrAnC8LewjfIcClFK4VwjekjhlKbyHYTx95/EzcEN/9ugsr9R/xsSfNMxnMcsxMdwLkPEGWuTjvRlso+6HXU7dUlIYiFooBReBRLxYPxnIdr9zgX677c+P7UNdr1YpgxqS1o4QpjSjt4HYzBqr9HowS6jg1BUP8y/5YfCFW1Fntyxr57anCivEh2wM3BJH7+mAiK2zMUbGTPCtxwyl0KqirrCsysU8omdTr3/WrkVUr6wBFtNfyHFYOcL6lSV9GnP8bIEUaoiwJbvCzly/hicgJ4dfO3rOA/n5AS30ewYGfkr0h5B8y/liru0l+v7at2YIaAX2o00sKS2IQDZgAACJQNClRoQUuxyAGUqiBNC+cVdoWJ9yt2reJls8bpCAjDI+1+5Kha0AFP3ZX+5WZOmAAKrSup2QmxWM7rJj4CiGDTniIddKDyzUhFqWHHPd53GJmFfduFbYuihaUCjsdg4qvKxYP9e15zVWKPw/1qPdvhh2/nwoG303rxtR38mBTBJhVo/qt91gZnIevjlHlzNFAQtNovkXM081aeiCX8lXq8ep0MqG+TndgKZcHJ9mv5zXF9MiO9hgtfnmbyVGJnSKVlwfwspLhACGw4VqPkTNCaDTxO5u7MnXk3Qp63XNRF+f6NeKgG+cPagkf14n7wh7LwkLIKP/h4a2yg1HFEx3fNsneSjqFFs5dnubMlbadK0jFDh4rIE6WtgWxTo/xYR7Tg134zVCSwSu+ucT2D23mhjmx5uDbgxjKRjHJPkavsq8bRZupfYQYy088WPAAupyA5Rgtd2x1CTWzNoT5uLbWhJbcfkUfSalHQjo3rhCtLQPua+uogen/VKcEGqIBxsqeY7UQQ5uSszobH9F4UhZOpx/n+fddEEffEOzBkMdsLuhq2TlybpTOj9mODWbNjBjuT/Gnv2keggt+UAPUTVf1ySE7AppsiLRwQOk+uf/MD1mn9AQ=="
		return token

class dbconnect():
	def db_config(self):
		db = {
	    	'host':'localhost',
	    	'database':'codefundoapp',
	    	'user':'root',
	    	'password':'deepak'
		}		
		return db